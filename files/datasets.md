1) **Data Identification and Requirements:**
To validate the pipeline, the input data must meet the following specifications:

  * Organism: Any eukaryote with a reference genome (FASTA) and annotation (GTF).

  * Data Type: RNA-Sequencing (Poly-A enriched or Ribo-depleted).

  * Format: FASTQ files gzipped (.fastq.gz).

  * Read Structure: Paired-end (PE) or Single-end (SE) reads.

  * Sequencing Depth: Minimum 10 million reads per sample recommended for differential expression; >30 million for isoform analysis.

  * Experimental Design: Minimum 2 biological replicates per condition

  *I will be using data generated from my lab -- paired-end RNA sequencing of wild-type, untreated human H1299 cells `H1299_untreat_1.fastq.gz` (will add info about read depth here when i can find it...) and H1299 cells treated with an inhibitor `H1299_inhib_1.fastq.gz`*
  
2) Subset of Data for Development

  * Use command line to extract first 1,000,000 reads from the `H1299_untreat_1.fastq.gz` and `H1299_inhib_1.fastq.gz` files.
  * Use the following to extract a subset for both the treated and untreated H1299 samples:
    
    `zcat Sample1_R1.fastq.gz | head -n 4000000 | gzip > subset/Sample1_R1.subset.fastq.gz`
    
    `zcat Sample1_R2.fastq.gz | head -n 4000000 | gzip > subset/Sample1_R2.subset.fastq.gz`

3) Full Dataset
  * Once development is complete using the subset dataset, the project will be validated using the full dataset. This will be 3 replicates each of:
    * H1299 Human Cells, wild type, untreated
    * H1299 Human Cells, wild type, treated with CDDO inhibitor
    * H1299 Human Cells, KEAP1 KO, untreated
   * Will add information about read counts ect when i can find them

