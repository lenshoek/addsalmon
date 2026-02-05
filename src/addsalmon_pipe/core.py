import shlex

def run_cmd(cmd):
    """Prints the command instead of running it for testing."""
    print(f"  [EXEC] {' '.join(shlex.quote(str(c)) for c in cmd)}")

def select_fastqs(sample_dir):
    """Dummy logic to simulate finding FASTQs."""
    print(f"  [CORE] Searching for FASTQs in {sample_dir}...")
    return "sample_R1.fastq.gz", "sample_R2.fastq.gz"