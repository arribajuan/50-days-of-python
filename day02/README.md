# Day 2 - Convert Add

Write a function called convert_add that takes a list of strings as an
argument and converts it to integers and sums the list. 

For example
[‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.


## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day02 python=3.10 
conda activate 50dop-day02
```

### Install libraries

``` bash
conda install -c anaconda pytest
```

# Conda environment import / export

### Save environment to a file

``` bash
conda list --explicit > environment.txt
```

### Create environment from a file

``` bash
conda env create --file environment.txt
```

# Run tests

``` bash
pytest convert_add_test.py
```