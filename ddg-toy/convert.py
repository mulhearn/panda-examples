
# Python environment requires: root_base root_pandas pyarrow
# from conda-forge:
# conda config --add channels conda-forge
# I had to install in steps:
# conda create -n goodbye_root root_base
# conda activate goodbye_root
# conda install root_pandas 
# conda install pyarrow

from root_pandas import read_root

df = read_root("on_top_of_feedthrough.root", "ncapture")
df.to_feather("neutrons.feather")
