# A Comparison between AMCMC and MCINTYRE

## Table of contents

[](TOC)

- [A Comparison between AMCMC and MCINTYRE](#a-comparison-between-amcmc-and-mcintyre)
  - [Table of contents](#table-of-contents)
  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Materials and methods](#materials-and-methods)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Experiments](#experiments)
    - [Experiment 0](#experiment-0)
      - [Summary](#summary)
      - [Software Versions](#software-versions)
      - [Plots](#plots)

[](TOC)

## Abstract

TODO

## Introduction

TODO

## Materials and methods

The independent variable is the number of *samples*, i.e. the number of steps 
to approximate the distribution. What we want to measure the dependent 
variable, time.

Every experiment is repeated on a different processor thread. The results of 
these experiments are grouped by sample size so it is possible to compute the 
average running times and standard deviations.

Once the data is saved on a CSV file and after some statistical 
computations, plotting is carried out.

### Hardware

Most of the experiments have been run in a virtual machine with 4 cores 
assigned and a total memory of 14 Gigabytes, 1 of which as swap.

| Computer id | Processor cores | Threads per core | Memory (GB) | Swap (GB) | Virtual machine | OS | comment |
|-------------|-----------------|------------------|-------------|-----------|-----------------|----|---------|
| 0 | 4 | 1 | 14  | 1 | yes | Parabola GNU/Linux-libre x86-64 | |
| 1 | 2 | 2 | 12 | 0 | no | Parabola GNU/Linux-libre x86-64 | |
| 2 | ? | ? | ? | ? | ? | COKA UNIFE | ? | ? |

### Software

Two prolog systems have been used:
- *SWI Prolog*
- *XSB Prolog*

See https://github.com/frnmst/mcmc-comparisons#dependencies

To measure the running times, the two prolog systems have been instructed to 
repeat a specific experiment, with fixed parameters, several number of times. 
This aspect is very important also because of the stochastic nature of these 
experiments. 

Plotting is handled by Matplotlib while some statitical computations are done 
by NumPy, both of which are Python libraries.

For each plot the standard deviation is represented by error bars.

## Experiments

### Experiment 0

#### Summary

| Experiment name | Computer id | Command | Raw data |
|-----------------|-------------|---------|----------|
| arithm_sample   | 0           | `./run.sh --repetitions=16 -p -t arithm_sample -g -M 28000` | [data/experiment-0/arithm_sample.csv](data/experiment-0/arithm_sample.csv) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [077a951b866a7433236cfa0ef622a3b936fd57a6](https://github.com/friguzzi/cplint/tree/077a951b866a7433236cfa0ef622a3b936fd57a6) | [aa6106bfefab31aced4e7962c2d4863ea3d0e19f](https://github.com/frnmst/mcmc-comparisons/tree/aa6106bfefab31aced4e7962c2d4863ea3d0e19f) | - | `7.7.19` | - |

#### Plots

![data/experiment-0/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0/plot_arithm_sample_mh_vs_gibbs_times.png)

