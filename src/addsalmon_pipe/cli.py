import argparse
import sys
from addsalmon_pipe.branches import alignment, salmon
from addsalmon_pipe.analysis import differential, plotting

def main():
    parser = argparse.ArgumentParser(prog="rnasalmon-pipe", description="anRNALab RNA-Seq Suite With Salmon")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Preprocessing & Alignment Branch
    align_parser = subparsers.add_parser("align", help="Run standard alignment branch")
    align_parser.add_argument("--input", required=True)
    align_parser.add_argument("--index", required=True)
    
    # 2. Salmon Branch
    salmon_parser = subparsers.add_parser("salmon", help="Run quasi-mapping branch")
    salmon_parser.add_argument("--input", required=True)
    salmon_parser.add_argument("--index", required=True)

    # 3. Differential Expression
    de_parser = subparsers.add_parser("diffexp", help="Run DESeq2 statistical analysis")
    de_parser.add_argument("--mode", choices=["align", "salmon"], required=True)
    de_parser.add_argument("--metadata", required=True)

    args = parser.parse_args()

    if args.command == "align":
        alignment.run_full_alignment_flow(args)
    elif args.command == "salmon":
        salmon.run_salmon_quant(args)
    elif args.command == "diffexp":
        differential.run_deseq2(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()