# Allele Study
## What
This code will generate a number of individuals bearing a pair of allele markers that are determined by a text file called "genes.txt". Each of the allele pairs in genes.text will be combined with another one in their generation and used to create another set of 4 individuals using the punnett square functionality. It runs for 5 (by default) generations and then the rest is compared for similarities, which in a closed breeding pool is a marker for genetic mutation, with the number of similarities printed as a percentage of the whole.

## How

Run the file like any python script. You can specify the number of generations to generate with the `--num-gens=` flag, and the genes.txt file path with `--file`. For example:
```shell
python genetics.py --num-gens 5 --file genes.txt
```

## Genes file
```
A a
B b
C c
D d
```
This is an example of genes.txt. 
