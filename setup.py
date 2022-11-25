from setuptools import find_packages, setup

setup(
    name="pcsb",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        pcsb=pcsb:cli
    """,
)
