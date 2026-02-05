from setuptools import setup, find_packages

setup(
    name="addsalmon_pipe",
    version="0.1.0",
    # This looks into the 'src' directory for your code
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            # This creates the terminal command 'addsalmon-pipe'
            "addsalmon-pipe=addsalmon_pipe.cli:main",
        ],
    },
)