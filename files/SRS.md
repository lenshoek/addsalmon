## Software Requirements Specification (SRS)
#### Project Name: Dual-Branch RNA-Seq Analysis Pipeline (Alignment & Quasi-mapping) for anRNALab
#### Authors: CW, KL, ChatGPT & Google Gemini
#### Date: Janurary 2026

**Purpose**: 
This dual-branch RNA-seq analysis pipeline serves as a modular command-line suite designed to process raw RNA-seq data. It offers two parallel analysis pathways within a single ecosystem:

1) **Standard Alignment Branch**: Uses traditional genome alignment (STAR/HISAT2), BAM processing (deduplication), and feature counting for genome-centric analysis
2) **Salmon Quasi-mapping Branch**: Uses `Salmon` for rapid, alignment-free quantification of transcripts, enabling high-resolution isoform-level analysis

Both branches converge into a unified `DESeq2` statistical framework to identify differentially expressed genes and transcripts, followed by specific visualization modules

---

**Project Goals**: 
+ **Reproducibility**: Parameterized Python scripts eliminate manual intervention and ensure consistent results across different datasets
+ **Modular Architecture**: A modular workflow where users can toggle between alignment and quasi-mapping based on the biological question
+ **Isoform Awareness**: Integration of Salmon and `tximport` allows the pipeline to transcend gene-level analysis and explore isoform switching
+ **Easy Visualization**: Automated generation of QC plots, heatmaps, and isoform usage charts using `matplotlib` and `ggplot2`.

---

### 1) Pre-processing (Shared Entry Point)
+ **Script**: `run_cutadapt_fastp.py`
+ **Input**: Raw FASTQ files (`_R1`, `_R2`).
+ **Functions**: 
    + Adapter trimming via `cutadapt`.
    + Quality filtering and UMI extraction via `fastp`.
+ **Output**: Cleaned, filtered FASTQ files organized in sample-specific subdirectories.

---

### 2.A) Branch A: Standard Alignment Pipeline
+ **Scripts**: `run_align.py`, `parallel_dedup.py`, `run_feature_Counts.py`
+ **Functions**:
    + **Alignment**: Map reads to the reference genome using HISAT2 or STAR.
    + **Deduplication**: Parallelized UMI deduplication using `umi_tools`.
    + **Quantification**: Summarize reads into gene-level counts using `featureCounts`.
+ **Output**: Merged `counts_matrix.tsv` and a metadata scaffold.

---

### 2.B) Branch B: Salmon Quasi-mapping Pipeline
+ **Script**: `run_salmon.py` 
+ **Input**: Cleaned FASTQ files and a Salmon Transcriptome Index.
+ **Functions**:
    + **Quasi-mapping**: Rapidly assign reads to transcripts without full alignment.
    + **Abundance Estimation**: Calculate TPM (Transcripts Per Million) and estimated counts.
+ **Output**: Per-sample `quant.sf` files containing transcript-level quantification.

---

### 3) Differential Expression (Statistical Convergence)
+ **Script**: `run_DiffGeneExp.py` (Modified for Dual-Input)
+ **Input**:
    + **Branch A**: `counts_matrix.tsv`
    + **Branch B**: Directory of `quant.sf` files + `tx2gene.csv` mapping file
+ **Functions**:
    + **Data Ingestion**: Uses `tximport` (for Salmon) or direct matrix reading (for featureCounts)
    + **Statistical Modeling**: Variance estimation and dispersion modeling via `DESeq2`
    + **Contrast Analysis**: Calculation of LOG2 Fold Changes and adjusted p-values
+ **Output**: `normalized_counts.tsv`, `DE_results.csv`, and global QC plots (PCA, Dispersion)

---

### 4) Visulization of Data 
+ **Script**: `gene_heatmap.py`
    + **Input**: `normalized_counts.tsv` and a target gene list (user provided)
    + **Functions**: Row-wise percentile scaling and replicate-averaged heatmaps with mean expression bars
    + **Output**: `gene_heatmap.pdf`

+ **Script**: `gene_isoform.py` 
    + **Input**: Salmon `quant.sf` directories and `tx2gene.csv`
    + **Functions**: Extracts transcript-level TPMs for a specific gene; calculates relative isoform proportions using `ggplot2`
    + **Output**: `isoform_usage_plot.pdf` (stacked bar charts showing isoform switching)

---

### System Requirements & Environment
+ **Environment Manager**: Conda (`environment.yml`).
+ **Key Dependencies**:
    + **Python 3.12**: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.
    + **R 4.4.3**: `DESeq2`, `tximport`, `ggplot2`, `pheatmap`.
    + **Bioinformatics**: `salmon`, `star`, `hisat2`, `subread`, `fastp`, `cutadapt`.
