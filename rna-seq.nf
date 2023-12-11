#!/usr/bin/env nextflow

params.reads = "$workflow.launchDir/reads/*_{1,2}.fq.gz"
params.assembly = "$workflow.launchDir/assembly/assembly.fasta"

println "$workflow.launchDir"

process get_reference_genome{
    output:
    file "assembly/assembly.fasta" into assembly

    script:
    """
    wget -r -nd --no-parent https://ftp.ensembl.org/pub/current_fasta/mus_musculus/dna_index/
    gunzip *.dna.toplevel.fa.gz
    mv GCF_000006745.1_ASM674v1_genomic.fna assembly/assembly.fasta
    """
}

process run_fastqc {
    input:
    file reads from reads

    output:
    file "fastqc/*_fastqc.html" into fastqc

    script:
    """
    fastqc -o fastqc ${reads}
    """
}

process run_multiqc {
    input:
    file fastqc_reports from fastqc

    output:
    file "multiqc_report.html" into multiqc

    script:
    """
    multiqc fastqc_reports
    """
}

process build_hisat2_index {
    input:
    file assembly from assembly

    output:
    file "index/*" into index

    script:
    """
    hisat2-build ${assembly} index/assembly
    """
}

process run_hisat2 {
    input:
    file reads from reads
    file index from index

    output:
    file "alignment/*" into alignment

    script:
    """
    hisat2 -x ${index}/assembly -1 ${reads[0]} -2 ${reads[1]} -S alignment/alignment.sam
    """
}

process run_samtools {
    input:
    file sam from alignment

    output:
    file "alignment/*" into alignment

    script:
    """
    samtools view -bS ${sam} > alignment/alignment.bam
    samtools sort alignment/alignment.bam -o alignment/alignment.sorted.bam
    samtools index alignment/alignment.sorted.bam
    """
}

process run_counts {
    input:
    file bam from alignment

    output:
    file "counts/*" into counts

    script:
    """
    htseq-count -f bam -r pos -s no -i gene_id ${bam} assembly/assembly.fasta > counts/counts.txt
    """
}

process run_cufflinks {
    input:
    file bam from alignment

    output:
    file "cufflinks/*" into cufflinks

    script:
    """
    cufflinks -o cufflinks -p 8 -G assembly/assembly.fasta ${bam}
    """
}

process run_cuffdiff {
    input:
    file bam from alignment
    file gtf from cufflinks

    output:
    file "cuffdiff/*" into cuffdiff

    script:
    """
    cuffdiff -o cuffdiff -p 8 -L WT,MT -u ${gtf} ${bam[0]} ${bam[1]}
    """
}

process run_sorting {
    input:
    file bam from alignment

    output:
    file "alignment/*" into alignment

    script:
    """
    samtools sort ${bam} -o alignment/alignment.sorted.bam
    samtools index alignment/alignment.sorted.bam
    """
}

process move_diff {
    input:
    file diff from cuffdiff

    output:
    file "diff/*" into diff

    script:
    """
    mv ${diff} diff/diff.txt
    """
}

process run_edgeR {
    input:
    file counts from counts
    file diff from diff

    output:
    file "edgeR/*" into edgeR

    script:
    """
    Rscript edgeR.R ${counts} ${diff}
    """
}

process run_deseq2 {
    input:
    file counts from counts
    file diff from diff

    output:
    file "DESeq2/*" into DESeq2

    script:
    """
    Rscript DESeq2.R ${counts} ${diff}
    """
}

process email_completion {
    input:
    file multiqc_report from multiqc

    script:
    """
    echo "Your analysis is complete!" | mail -s "Analysis Complete" ${params.email}
    """
}

workflow {
    get_reference_genome()
    run_fastqc()
    run_multiqc(fastqc_reports)
    build_hisat2_index(assembly)
    run_hisat2(index)
    run_samtools(alignment)
    run_counts(alignment)
    run_cufflinks(alignment)
    run_cuffdiff(alignment, gtf)
    run_sorting(alignment)
    move_diff(diff)
    run_edgeR(counts, diff)
    run_deseq2(counts, diff)
    email_completion(multiqc_report)
}
