# This file is part of the HLA-PEPCLUST software package.
from warnings import filterwarnings
from rich.traceback import install
from ProtPeptigram.DataProcessor import PeptideDataProcessor
from ProtPeptigram.viz import ImmunoViz
install(show_locals=True)  # type: ignore

filterwarnings("ignore")
"""
Peptigram: peptides distribution across proteins

A Python package for mapping peptides to source protein and identifying high desnsity window to core prptides across diffrent source protein
"""

__version__ = "1.0.0-dev"
__author__ = "Sanjay Krishna,Prithvi Munday,Chen Li"
__email__ = "sanjay.sondekoppagopalakrishna@monash.edu"