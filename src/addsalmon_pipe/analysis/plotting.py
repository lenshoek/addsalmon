from anrna_pipe.core import run_cmd

def run_viz(args):
    print(f"\n>>> Generating Plots for Gene: {args.gene}")
    run_cmd(["python", "gene_heatmap.py", "--input", "norm_counts.tsv"])
    if args.isoform:
        run_cmd(["Rscript", "gene_isoform.R", "--gene", args.gene])