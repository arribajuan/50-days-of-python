# Day 1 - Division and Square-root

Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by 5.

For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

## Conda environment

### Create conda environment

``` bash
conda create --name 50dop-day01 python=3.10 
conda activate 50dop-day01
```

### Save environment to a file

``` bash
conda list --explicit > environment.txt
```

### Create environment from a file

``` bash
conda env create --file environment.txt
```

## Install libraries

``` bash
conda install -c anaconda pytest
```

## Run tests

``` bash
pytest divide_or_square_test.py
```

## Run code

``` bash
python3 day01-solution.py
```
