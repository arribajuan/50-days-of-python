# Day 4: Only Floats

Write a function called only_floats.

* it takes two parameters: a and b
* returns 2 if both arguments are floats
* returns 1 if only one argument is a float
* returns 0 if neither argument is a float

For example if you pass (12.1, 23) as an argument, your function should return a 1.

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day04 python=3.10 
conda activate 50dop-day04
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
pytest only_floats_test.py
```


