# Experimental results of AMCMC and MCINTYRE comparisons

## Table of contents

[](TOC)

- [Experimental results of AMCMC and MCINTYRE comparisons](#experimental-results-of-amcmc-and-mcintyre-comparisons)
  - [Table of contents](#table-of-contents)
  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Materials and methods](#materials-and-methods)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Key](#key)
    - [The *Summary* tables](#the-summary-tables)
    - [The *Software versions* tables](#the-software-versions-tables)
  - [Experiments](#experiments)
    - [Experiment 0](#experiment-0)
      - [Summary](#summary)
      - [Software versions](#software-versions)
      - [Plots](#plots)
    - [Experiment 1](#experiment-1)
      - [Summary](#summary-1)
      - [Software Versions](#software-versions-1)
      - [Plots](#plots-1)
    - [Experiment 2](#experiment-2)
      - [Summary](#summary-2)
      - [Software Versions](#software-versions-2)
      - [Plots](#plots-2)
    - [Experiment 3](#experiment-3)
      - [Summary](#summary-3)
      - [Software Versions](#software-versions-3)
      - [Plots](#plots-3)
    - [Experiment 4](#experiment-4)
      - [Summary](#summary-4)
      - [Software Versions](#software-versions-4)
      - [Plots](#plots-4)
    - [Experiment 5](#experiment-5)
      - [Summary](#summary-5)
      - [Software Versions](#software-versions-5)
      - [Plots](#plots-5)
    - [Experiment 6](#experiment-6)
      - [Summary](#summary-6)
      - [Software Versions](#software-versions-6)
      - [Plots](#plots-6)
    - [Experiment 7](#experiment-7)
      - [Summary](#summary-7)
      - [Software Versions](#software-versions-7)
      - [Plots](#plots-7)

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

| Computer id | Processor cores | Threads per core | Memory (GB) | Swap (GB) | Virtual machine | OS | comment |
|-------------|-----------------|------------------|-------------|-----------|-----------------|----|---------|
| 0 | 4 | 1 | 14 | 1 | yes | Parabola GNU/Linux-libre x86-64 | |
| 1 | ? | ? | ? | ? | ? | ? | COKA UNIFE |

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

## Key

An explanation of the structure of the tables.

### The *Summary* tables

|  -   | Name | Computer id | Command | Data | Comment |
|------|------|-------------|---------|------|---------|
| Comment | the experiment name as used in the command | the computer that executed the experiment | the CLI command or file | a link to the raw CSV file containing the results | other relevant information |
| Type | str | int | str:verbatim | str:link | str |

### The *Software versions* tables

|   -     | cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|---------|--------|------------------|----------------|------------|------------|
| Comment | git SHA-1 commit | git SHA-1 commit | git SHA-1 commit | version number | version number |
| Type    | str:link | str:link | str:link | str:verbatim | str:verbatim | 

Software which has not been used for an experiment is marked with a dash 
character such as `-`

## Experiments

### Experiment 0

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh --repetitions=16 -p -t arithm_sample -g -M 28000` | [data/experiment-0000/arithm_sample.csv](data/experiment-0000/arithm_sample.csv) | |

#### Software versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [077a951](https://github.com/friguzzi/cplint/tree/077a951b866a7433236cfa0ef622a3b936fd57a6) | [aa6106b](https://github.com/frnmst/mcmc-comparisons/tree/aa6106bfefab31aced4e7962c2d4863ea3d0e19f) | - | `7.7.19` | - |

#### Plots

![data/experiment-0000/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0000/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0000/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0000/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 1

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| test33_sample | 0 | `./run.sh --repetitions=16 -p -t test33_sample -g -M 50000` | [data/experiment-0001/test33_sample.csv](data/experiment-0001/test33_sample.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [077a951](https://github.com/friguzzi/cplint/tree/077a951b866a7433236cfa0ef622a3b936fd57a6) | [aa6106b](https://github.com/frnmst/mcmc-comparisons/tree/aa6106bfefab31aced4e7962c2d4863ea3d0e19f) | - | `7.7.19` | - |

#### Plots

![data/experiment-0001/plot_test33_sample_mh_vs_gibbs_probs.png](data/experiment-0001/plot_test33_sample_mh_vs_gibbs_probs.png)

![data/experiment-0001/plot_test33_sample_mh_vs_gibbs_times.png](data/experiment-0001/plot_test33_sample_mh_vs_gibbs_times.png)

### Experiment 2

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_cond_prob | 0 | `./run.sh -p -t arithm_cond_prob --repetitions=16 -y xsb -g -M 100000` | [data/experiment-0002/arithm_cond_prob.csv](data/experiment-0002/arithm_cond_prob.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| - | [4fa657c](https://github.com/frnmst/mcmc-comparisons/tree/4fa657c3317e09524c6f081d7fe9b26bac7f877f) | [db4e371](https://github.com/frnmst/Adaptive-MCMC/tree/db4e37120d60680cb0302b05c18aee815fe54c72) | - | `3.8.0` |

#### Plots

![data/experiment-0002/plot_arithm_cond_prob_adapt_on_vs_adapt_off_probs.png](data/experiment-0002/plot_arithm_cond_prob_adapt_on_vs_adapt_off_probs.png)

![data/experiment-0002/plot_arithm_cond_prob_adapt_on_vs_adapt_off_times.png](data/experiment-0002/plot_arithm_cond_prob_adapt_on_vs_adapt_off_times.png)

### Experiment 3

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh --repetitions=64 -p -t arithm_sample -g -M 28000` | [data/experiment-0003/arithm_sample.csv](data/experiment-0003/arithm_sample.csv) | compared to experiment 0, the standard deviation decreased a little because of the increased number of experiments |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [077a951](https://github.com/friguzzi/cplint/tree/077a951b866a7433236cfa0ef622a3b936fd57a6) | [4fa657c](https://github.com/frnmst/mcmc-comparisons/tree/4fa657c3317e09524c6f081d7fe9b26bac7f877f) | - | `7.7.19` | - |

#### Plots

![data/experiment-0003/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0003/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0003/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0003/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 4

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_rejection_sample | 0 | `./run.sh --repetitions=16 -p -t arithm_rejection_sample -g -M 28000` | [data/experiment-0004/arithm_rejection_sample.csv](data/experiment-0004/arithm_rejection_sample.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [077a951](https://github.com/friguzzi/cplint/tree/077a951b866a7433236cfa0ef622a3b936fd57a6) | [f0e6b2d](https://github.com/frnmst/mcmc-comparisons/tree/f0e6b2de5800f9f74f8b73e2178e22fc64e76b08) | - | `8.0.1` | - |

#### Plots

![data/experiment-0004/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png](data/experiment-0004/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png)

![data/experiment-0004/plot_arithm_rejection_sample_mh_vs_gibbs_times.png](data/experiment-0004/plot_arithm_rejection_sample_mh_vs_gibbs_times.png)

### Experiment 5

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_rejection_sample | 0 | `./run.sh -p -t arithm_rejection_sample -g -M 28000` | [data/experiment-0005/arithm_rejection_sample.csv](data/experiment-0005/arithm_rejection_sample.csv) | using the `simplegibbs` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [b2b4b49](https://github.com/friguzzi/cplint/tree/b2b4b49d486fc276cc3ab43b5e3f350b571a3541) | [c97f9c7](https://github.com/frnmst/mcmc-comparisons/tree/c97f9c74b7a5733e97fe393857bc5d94db305fb3) | - | `8.0.1` | - |

#### Plots

![data/experiment-0005/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png](data/experiment-0005/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png)

![data/experiment-0005/plot_arithm_rejection_sample_mh_vs_gibbs_times.png](data/experiment-0005/plot_arithm_rejection_sample_mh_vs_gibbs_times.png)

### Experiment 6

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh -p -t arithm_sample -g -M 28000` | [data/experiment-0006/arithm_sample.csv](data/experiment-0006/arithm_sample.csv) | using the `simplegibbs` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [b2b4b49](https://github.com/friguzzi/cplint/tree/b2b4b49d486fc276cc3ab43b5e3f350b571a3541) | [c97f9c7](https://github.com/frnmst/mcmc-comparisons/tree/c97f9c74b7a5733e97fe393857bc5d94db305fb3) | - | `8.0.1` | - |

#### Plots

![data/experiment-0006/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0006/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0006/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0006/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 7

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh -p -t arithm_sample -g -M 28000` | [data/experiment-0007/arithm_sample.csv](data/experiment-0007/arithm_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [c97f9c7](https://github.com/frnmst/mcmc-comparisons/tree/c97f9c74b7a5733e97fe393857bc5d94db305fb3) | - | `8.0.1` | - |

#### Plots

![data/experiment-0007/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0007/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0007/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0007/plot_arithm_sample_mh_vs_gibbs_times.png)
