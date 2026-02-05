from anrna_pipe.core import run_cmd, select_fastqs

def run_salmon_quant(args):
    print(f"\n>>> Starting Salmon Branch")
    r1, r2 = select_fastqs(args.input)
    cmd = ["salmon", "quant", "-i", args.index, "-1", r1, "-2", r2, "-o", "dummy_out"]
    run_cmd(cmd)
    print(">>> Salmon Branch Finished")