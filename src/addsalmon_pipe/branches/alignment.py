from anrna_pipe.core import run_cmd

def run_full_alignment_flow(args):
    print(f"\n>>> Starting Alignment Branch")
    # Step 1: Align
    run_cmd(["hisat2", "-x", args.index, "-U", args.input])
    # Step 2: Feature Counts
    run_cmd(["featureCounts", "-a", "genomic.gtf", "-o", "counts.txt", "aligned.bam"])
    print(">>> Alignment Branch Finished")