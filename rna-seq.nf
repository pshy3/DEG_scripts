#!/usr/bin/env nextflow

reads_input = "$workflow.launchDir/"+params.reads
reads_dir = "$workflow.launchDir/"+params.reads_dir

workflow {
    // species_ch = Channel.value(params.species)
    // data_dir_ch = Channel.value(params.data_dir)
    reads_qc_ch = Channel.fromPath(reads_dir)
    reads_ch = Channel.fromFilePairs(reads_input, size: 2)

    get_reference_genome(params.species, params.data_dir)
        .set { genome_ch}

    run_fastqc(reads_qc_ch)
        .set { fastqc_ch }

    // run_multiqc(fastqc_ch.collect())

    build_hisat2_index(genome_ch.fasta)
        .set { index_ch }
}

process get_reference_genome {
    conda 'lftp' // install lftp
    conda 'gunzip' // install gunzip

    input:
    val species
    val data_dir

    output:
    path("*.dna.toplevel.fa", emit: 'fasta')
    path("*.gff3", emit: 'gff3')

    publishDir "${workflow.workDir}/../results/reference", mode: 'copy'

    script:
    if (data_dir != 'default') {
        """
        cp ${data_dir}/* .
        """
    } else {
        """
        echo "Downloading reference genome for ${species} from Ensembl FTP server..."
        mkdir -p reference
        lftp -c "open -e 'mget -c /pub/current_fasta/${species}/dna_index/*dna.toplevel.fa.gz' ftp://ftp.ensembl.org"
        lftp -c "open -e 'mget -c /pub/current_gff3/${species}/*chr.gff3.gz' ftp://ftp.ensembl.org"
        gunzip *.gz
        """
    }
}

process run_fastqc {
    conda 'fastqc' // install fastqc

    input:
    path reads_qc_ch

    output:
    path("*_fastqc.zip", emit: 'zip')
    path("*_fastqc.html", emit: 'html')

    publishDir "${workflow.workDir}/../results/fastqc_untrimmed", mode: 'copy'

    script:
    """
    fastqc ${reads_qc_ch} -o .
    """
}

process run_multiqc {
    input:
    path "*"

    output:
    path("multiqc_report.html")

    publishDir "${workflow.workDir}/../results/multiqc_untrimmed", mode: 'copy'

    """
    multiqc . -o .
    """
}

process build_hisat2_index {
    conda 'hisat2' // install hisat2

    input:
    path fasta

    output:
    path("assembly", emit: 'index')

    script:
    """
    hisat2-build ${fasta} assembly
    """
}

process run_hisat2 {
    tag "Alignment on ${sample_id}"

    input:
    path index
    tuple val(sample_id), path(reads)

    output:
    path "alignment/*"

    script:
    """
    mkdir -p alignment
    hisat2 -x ${index}/assembly -1 ${reads[0]} -2 ${reads[1]} -S alignment/${sample_id}.sam
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

