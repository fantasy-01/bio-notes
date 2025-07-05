##Ctrl + K快捷键进行提交。
####25.7.5.完成了基本的配置并建立本地-远程ssh连接，将来的笔记都将在github保持同步。

####   grep "^A" genome.fa  显示所有带A的行
####   grep -c "^A" genome.fa 计数这样的行有多少

####  awk '$3 == "gene"' genes.gtf > genes-only.gtf
####  用 awk 来筛选 GTF 文件中 type 是 "gene" 的注释行，并把它们保存为一个新文件 genes-only.gtf。
#  因为一个 GTF 文件每行是chr1  HAVANA  exon  11869 12227 . + . gene_id "ENSG..."; transcript_id "ENST...";
#  其中第 3 列 $3 表示注释类型，gene是基因本体。执行后生成的文件实则只含基因。不含 transcript、exon、CDS 等内容。
#  使用grep -c "gene" genes-only.gtf来计数有多少基因存在。

#### sort -k2,2 genome_data.txt>sorted_data.txt
#### 按第二列排序并将其输出到新文件中。
##gene1  chr3-----gene2  chr1
##gene2  chr1     gene3  chr2
##gene3  chr2     gene1  chr3

####   cut -f1 file.txt
####   提取第一列。默认分隔是制表符Tab
####   cut -d',' -f2 file.csv
####   用冒号分隔提取第二列。

####   cut -f1 genomic.gff | sort | uniq | wc -l
####   具有实用意义的组合拳。cut -f1提取第一列，一般是chr名称；sort进行排序；uniq去重复，最后按行数数。
