# Dual-Branch RNA-Seq Pipeline Workflow

This workflow represents a modular approach to RNA-seq analysis, allowing for either traditional genomic alignment or rapid transcriptomic quasi-mapping using `Salmon`.

---

## step 1: Pre-processing (Shared)
**Script:** `run_cutadapt_fastp.py`
- **Inputs:** - Raw FASTQ files (`*_R1.fastq.gz`, `*_R2.fastq.gz`)
    - Adapter sequences (user provided file)
- **Outputs:** - Quality-controlled FASTQs: `*_fastp_R1.fastq.gz`, `*_fastp_R2.fastq.gz`
    - QC Reports: `fastp.html`, `fastp.json`
- **Data Flow:** Raw data is cleaned; these output files serve as the starting point for both Branch A and Branch B.

---

## Step 2: Quantification (Dual branch)

### Step 2 Branch A: Genomic Alignment (Standard HISAT2/STAR)
**i: Alignment**
- **Script:** `run_align.py`
- **Inputs:** Cleaned FASTQs + Genome Index (STAR or HISAT2)
- **Outputs:** Coordinate-sorted BAM files (`sample.bam`)

**ii: Deduplication (Optional)**
- **Script:** `parallel_dedup.py`
- **Inputs:** `sample.bam`
- **Outputs:** Deduplicated BAM files (`sample_dedup.bam`)

**iii: Gene-level Counting**
- **Script:** `run_feature_Counts.py`
- **Inputs:** BAM files + GTF Annotation file
- **Outputs:** `counts_matrix.tsv` (A single merged file for all samples)

---

### Step 2 Branch B: Quasi-mapping (Salmon)
**Script:** `run_salmon.py` (New Script)
- **Inputs:** Cleaned FASTQs + Salmon Transcriptome Index
- **Outputs:** Per-sample directories containing `quant.sf` (Transcript-level abundances)

---

## Step 3: Statistical Analysis (DESQ2)
**Script:** `run_DiffGeneExp.py` (modified script for Salmon compatibility)
- **Inputs (from Branch A):** `counts_matrix.tsv` + `metadata.tsv`
- **Inputs (from Branch B):** `quant.sf` files + `metadata.tsv` + `tx2gene.csv` (Transcript-to-Gene map)
- **Outputs:**
    - `normalized_counts.tsv` (Shared format for downstream visualization)
    - `differential_expression_results.csv`
    - PCA and Volcano Plots

---

## Step 4: Visualization
**Script A: Gene Expression Heatmaps**
- **Script:** `gene_heatmap.py`
- **Inputs:** `normalized_counts.tsv` (from either branch) + Target Gene List (user provodied)
- **Outputs:** `heatmap.pdf`

**Script B: Isoform Switching/Usage**
- **Script:** `gene_isoform.py` (New Script)
- **Inputs:** `quant.sf` folders (from Branch B) + `tx2gene.csv` + Specific Gene ID
- **Outputs:** `isoform_usage_plot.pdf` (Stacked bar charts showing transcript proportions)

---

## Summary Table of Data Flow

| Stage | Script Name | Input | Output |
| :--- | :--- | :--- | :--- |
| **QC** | `run_cutadapt_fastp.py` | Raw FASTQ | Clean FASTQ |
| **Branch A** | `run_align.py` | Clean FASTQ | BAM |
| **Branch A** | `run_feature_Counts.py` | BAM + GTF | `counts_matrix.tsv` |
| **Branch B** | `run_salmon.py` | Clean FASTQ | `quant.sf` files |
| **Stats** | `run_DiffGeneExp.py` | Counts OR `quant.sf` | `normalized_counts.tsv` |
| **Viz** | `gene_heatmap.py` | Normalized Counts | Heatmap PDF |
| **Viz** | `gene_isoform.py` | `quant.sf` | Isoform Plot PDF |

<img width="7097" height="8192" alt="Start Decision Option Flow-2026-02-05-032921" src="https://github.com/user-attachments/assets/c4714ade-32fb-4830-b436-23c41bcf17b0" />

