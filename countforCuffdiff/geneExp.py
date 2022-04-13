import pandas as pd
import glob

data = ["THE DEG's COUNT INFORMATION IS AS FOLLOWS: \n \n"]
for filenames in glob.glob('*/gene_exp.diff'):
    file = pd.read_csv(filenames,sep='\t')
    name = filenames.split('/gene_exp.diff')[0]
    significant = file[file['significant'] == 'yes']
    deg1 = file[((file['log2(fold_change)'] >= 1) | (file['log2(fold_change)'] <= -1)) & (file['q_value'] <= 0.05) & (file['significant'] == 'yes')]
    #deg2 = deg1[(deg1['q_value'] <= 0.05) & (deg1['significant'] == 'yes')]
    up = file[(file['log2(fold_change)'] >= 1) & (file['q_value'] <= 0.05) & (file['significant'] == 'yes')]
    down = file[(file['log2(fold_change)'] <= -1) & (file['q_value'] <= 0.05) & (file['significant'] == 'yes')]
    up.to_csv('./gene_exp/'+name+'_up.csv')
    down.to_csv('./gene_exp/'+name+'_down.csv')
    significant.to_csv('./gene_exp/'+name+'_significant.csv')
    deg1.to_csv('./gene_exp/'+name+'_deg.csv')
    up_count = len(up.index)
    down_count = len(down.index)
    significant_count = len(significant.index)
    data.append(name + ':\n')
    data.append('Significant Count                                      :\t' + str(significant_count) +'\n')
    data.append('UP Regulated with Q-Value <0.05 and Fold Change >= 1   :\t' + str(up_count) + '\n')
    data.append('DOWN Regulated with Q-Value <0.05 and Fold Change <= -1:\t' + str(down_count) + '\n')
    data.append('Total DEG\'s                                            :\t' + str(up_count+down_count) + '\n \n')
datafile = open('./gene_exp/Count_data.txt',"w")
datafile.writelines(data)
datafile.close
