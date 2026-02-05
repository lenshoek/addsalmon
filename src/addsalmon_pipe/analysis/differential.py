from anrna_pipe.core import run_cmd

def run_deseq2(args):
    print(f"\n>>> Running Differential Expression (Mode: {args.mode})")
    print(f"    Using metadata: {args.metadata}")
    run_cmd(["Rscript", "run_deseq2.R", args.mode, args.metadata])
    print(">>> Analysis Finished")