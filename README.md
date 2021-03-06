# Experimental results of AMCMC and MCINTYRE comparisons

## Table of contents

[](TOC)

- [Experimental results of AMCMC and MCINTYRE comparisons](#experimental-results-of-amcmc-and-mcintyre-comparisons)
  - [Table of contents](#table-of-contents)
  - [References](#references)
  - [License](#license)
  - [Hardware](#hardware)
  - [Key](#key)
    - [The *Summary* tables](#the-summary-tables)
    - [The *Software versions* tables](#the-software-versions-tables)
  - [Experiments](#experiments)
    - [Experiment 0](#experiment-0)
    - [Experiment 1](#experiment-1)
    - [Experiment 2](#experiment-2)
    - [Experiment 3](#experiment-3)
    - [Experiment 4](#experiment-4)
    - [Experiment 5](#experiment-5)
    - [Experiment 6](#experiment-6)
    - [Experiment 7](#experiment-7)
    - [Experiment 8](#experiment-8)
    - [Experiment 9](#experiment-9)
    - [Experiment 10](#experiment-10)
    - [Experiment 11](#experiment-11)
    - [Experiment 12](#experiment-12)
    - [Experiment 13](#experiment-13)
    - [Experiment 14](#experiment-14)
    - [Experiment 15](#experiment-15)
  - [New experiments](#new-experiments)
    - [Experiment 16](#experiment-16)
    - [Experiment 17](#experiment-17)
    - [Experiment 18](#experiment-18)
    - [Experiment 19](#experiment-19)
    - [Experiment 20](#experiment-20)
    - [Experiment 21](#experiment-21)
    - [Experiment 22](#experiment-22)
    - [Experiment 23](#experiment-23)
    - [Experiment 24](#experiment-24)
    - [Experiment 25](#experiment-25)
  - [Experiments to keep](#experiments-to-keep)
    - [Experiment 26](#experiment-26)
    - [Experiment 27](#experiment-27)
    - [Experiment 28](#experiment-28)
    - [Experiment 29](#experiment-29)
    - [Experiment 30](#experiment-30)
    - [Experiment 31](#experiment-31)
    - [Experiment 32](#experiment-32)
    - [Experiment 33](#experiment-33)
    - [Experiment 34](#experiment-34)
    - [Experiment 35](#experiment-35)
    - [Experiment 36](#experiment-36)
    - [Experiment 37](#experiment-37)
    - [Experiment 38](#experiment-38)
    - [Experiment 39](#experiment-39)
    - [Experiment 40](#experiment-40)
  - [In paper](#in-paper)
    - [Experiment 41](#experiment-41)
    - [Experiment 42](#experiment-42)
    - [Experiment 43](#experiment-43)
    - [Experiment 44](#experiment-44)
    - [Experiment 45](#experiment-45)
    - [Experiment 46](#experiment-46)
    - [Experiment 47](#experiment-47)
    - [Experiment 48](#experiment-48)
    - [Experiment 49](#experiment-49)
    - [Experiment 50](#experiment-50)
    - [Experiment 51](#experiment-51)
    - [Experiment 97 (49 and 51)](#experiment-97-49-and-51)
    - [Experiment 98 (48 and 50)](#experiment-98-48-and-50)
    - [Experiment 99 (44 and 45, truncated at 4200 samples)](#experiment-99-44-and-45-truncated-at-4200-samples)

[](TOC)

## References

See https://github.com/frnmst/mcmc-comparisons/blob/master/README.md

## License

See the [LICENSE](LICENSE) file.

## Hardware

| Computer id | Processor cores | Threads per core | Memory (GB) | Swap (GB) | Virtual machine | OS | comment |
|-------------|-----------------|------------------|-------------|-----------|-----------------|----|---------|
| 0 | 4 | 1 | 14 | 1 | yes | Parabola GNU/Linux-libre x86-64 | |
| 1 | ? | ? | ? | ? | ? | ? | COKA UNIFE |

## Key

An explanation of the structure of the tables.

### The *Summary* tables

|  -   | Name | Computer id | Command | Data | Comment |
|------|------|-------------|---------|------|---------|
| Comment | the experiment name as used in the command | the computer in the *Hardware* table that executed the experiment | the CLI command | a link to the CSV file containing the results | other relevant information |
| Type | str | int | str:verbatim | str:link | str |

### The *Software versions* tables

|   -     | cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|---------|--------|------------------|----------------|------------|------------|
| Comment | git SHA-1 commit | git SHA-1 commit | git SHA-1 commit | version number | version number |
| Type    | str:link | str:link | str:link | str:verbatim | str:verbatim | 

Software which has not been used for an experiment is marked with a dash 
character such as `-`

## Experiments

The important experiments are the ones below *[In paper](#in-paper)*.

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

### Experiment 8

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh --repetitions=16 -p -t arithm_sample -g -M 28000` | [data/experiment-0008/arithm_sample.csv](data/experiment-0008/arithm_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [19c5513](https://github.com/frnmst/mcmc-comparisons/tree/19c5513230d43800732b6bf153bd12e25e2d64ee) | - | `8.0.1` | - |

#### Plots

![data/experiment-0008/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0008/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0008/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0008/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 9

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_rejection_sample | 0 | `./run.sh -p -t arithm_rejection_sample -g -M 28000` | [data/experiment-0009/arithm_rejection_sample.csv](data/experiment-0009/arithm_rejection_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [19c5513](https://github.com/frnmst/mcmc-comparisons/tree/19c5513230d43800732b6bf153bd12e25e2d64ee) | - | `8.0.1` | - |

#### Plots

![data/experiment-0009/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png](data/experiment-0009/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png)

![data/experiment-0009/plot_arithm_rejection_sample_mh_vs_gibbs_times.png](data/experiment-0009/plot_arithm_rejection_sample_mh_vs_gibbs_times.png)

### Experiment 10

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_rejection_sample | 0 | `./run.sh --repetitions=16 -p -t arithm_rejection_sample -g -M 28000` | [data/experiment-0010/arithm_rejection_sample.csv](data/experiment-0010/arithm_rejection_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [19c5513](https://github.com/frnmst/mcmc-comparisons/tree/19c5513230d43800732b6bf153bd12e25e2d64ee) | - | `8.0.1` | - |

#### Plots

![data/experiment-0010/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png](data/experiment-0010/plot_arithm_rejection_sample_mh_vs_gibbs_probs.png)

![data/experiment-0010/plot_arithm_rejection_sample_mh_vs_gibbs_times.png](data/experiment-0010/plot_arithm_rejection_sample_mh_vs_gibbs_times.png)

### Experiment 11

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh --repetitions=16 -p -t arithm_sample -g -M 54000` | [data/experiment-0011/arithm_sample.csv](data/experiment-0011/arithm_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [19c5513](https://github.com/frnmst/mcmc-comparisons/tree/19c5513230d43800732b6bf153bd12e25e2d64ee) | - | `8.0.1` | - |

#### Plots

![data/experiment-0011/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0011/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0011/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0011/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 12

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 1 | `./run.sh -S --partition longrun -M 28000` | [data/experiment-0012/arithm_sample.csv](data/experiment-0012/arithm_sample.csv) | using the `amcmc` branch in cplint and first experiment using COKA |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [9eb43fb](https://github.com/frnmst/mcmc-comparisons/tree/9eb43fb5cd172b4f26afdd1d4535bc4d41f68697) | - | `8.1.5` | - |

#### Plots

![data/experiment-0012/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0012/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0012/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0012/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 13

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh --repetitions=128 -p -t arithm_sample -g -M 10000` | [data/experiment-0013/arithm_sample.csv](data/experiment-0013/arithm_sample.csv) | using the `amcmc` branch in cplint with a total of 128*4=512 runs |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [973d464](https://github.com/frnmst/mcmc-comparisons/tree/973d464ae89578d3de21bd605c213d2fa20d4d81) | - | `8.0.1` | - |

#### Plots

![data/experiment-0013/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0013/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0013/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0013/plot_arithm_sample_mh_vs_gibbs_times.png)

### Experiment 14

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| test33_sample | 0 | `./run.sh --repetitions=16 -p -t test33_sample -g -M 28000` | [data/experiment-0014/test33_sample.csv](data/experiment-0014/test33_sample.csv) | using the `amcmc` branch in cplint |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [9eb43fb](https://github.com/frnmst/mcmc-comparisons/tree/9eb43fb5cd172b4f26afdd1d4535bc4d41f68697) | - | `8.0.1` | - |

#### Plots

![data/experiment-0014/plot_test33_sample_mh_vs_gibbs_probs.png](data/experiment-0014/plot_test33_sample_mh_vs_gibbs_probs.png)

![data/experiment-0014/plot_test33_sample_mh_vs_gibbs_times.png](data/experiment-0014/plot_test33_sample_mh_vs_gibbs_times.png)

### Experiment 15

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample | 0 | `./run.sh -p -t arithm_sample -g -M 28000` | [data/experiment-0015/arithm_sample.csv](data/experiment-0015/arithm_sample.csv) | using the `amcmc` branch in cplint and `mc_gibbs_sample(eval(2,4),eval(1,3),Samples,Prob,[block(2),mix(100)]),` |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [f4b4b47](https://github.com/friguzzi/cplint/tree/f4b4b471fb4913aa882fb0621ca4e64f2ad06c4e) | [65844c8](https://github.com/frnmst/mcmc-comparisons/tree/65844c8a9b241000bcb7f5ca1c49472ad3f5bc68) | - | `8.0.1` | - |

#### Plots

![data/experiment-0015/plot_arithm_sample_mh_vs_gibbs_probs.png](data/experiment-0015/plot_arithm_sample_mh_vs_gibbs_probs.png)

![data/experiment-0015/plot_arithm_sample_mh_vs_gibbs_times.png](data/experiment-0015/plot_arithm_sample_mh_vs_gibbs_times.png)

## New experiments

### Experiment 16

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -p -t arithm_sample_three -g -M 10000 -m 100 -s 100 -r 8 && ./run.sh --graph-only --first-experiment-only -t arithm_sample_three` | [data/experiment-0016/arithm_sample_three.csv](data/experiment-0016/arithm_sample_three.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [08cc5c3](https://github.com/frnmst/mcmc-comparisons/tree/08cc5c3327a38f0df48e14501a3758949ee67f57) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0016/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0016/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0016/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0016/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0016/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0016/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0016/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0016/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0016/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0016/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 17

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -p -t arithm_sample_three -g -m 10100 -M 14100 -r 8 && ./run.sh --graph-only --first-experiment-only -t arithm_sample_three` | [data/experiment-0017/arithm_sample_three.csv](data/experiment-0017/arithm_sample_three.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [68a8c3f](https://github.com/frnmst/mcmc-comparisons/tree/68a8c3f495e738ae74988504a57ad4c16b287be1) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0017/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0017/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0017/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0017/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0017/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0017/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0017/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0017/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0017/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0017/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 18

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -p -t arithm_sample_three -g -m 10100 -M 14100 -s 100 -r 8 && ./run.sh --graph-only --first-experiment-only -t arithm_sample_three` | [data/experiment-0018/arithm_sample_three.csv](data/experiment-0018/arithm_sample_three.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [37638cc](https://github.com/frnmst/mcmc-comparisons/tree/37638cc37b02607281bd9815ebd88322de293ca1) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0018/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0018/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0018/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0018/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0018/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0018/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0018/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0018/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0018/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0018/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 19

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 0 | `./run.sh -p -t hmm_sample_three -g -M 10000 -m 100 -s 100 -r 8 && ./run.sh --graph-only --first-experiment-only -t hmm_sample_three` | [data/experiment-0019/hmm_sample_three.csv](data/experiment-0019/hmm_sample_three.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [2cbcb13](https://github.com/frnmst/mcmc-comparisons/tree/2cbcb13c41fc68255885a55e98d45242e861097) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0019/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0019/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0019/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0019/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0019/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0019/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0019/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0019/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0019/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0019/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 20

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 0 | `./run.sh -p -t hmm_sample_three -g -m 10100 -M 28100 -s 100 -r 8 && ./run.sh --graph-only --first-experiment-only -t hmm_sample_three` | [data/experiment-0020/hmm_sample_three.csv](data/experiment-0020/hmm_sample_three.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [2cbcb13](https://github.com/frnmst/mcmc-comparisons/tree/2cbcb13c41fc68255885a55e98d45242e861097) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0020/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0020/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0020/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0020/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0020/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0020/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0020/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0020/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0020/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0020/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 21

Failed due to 8 hour timeout.

### Experiment 22

Failed due to 8 hour timeout.

### Experiment 23

failed

### Experiment 24

ignore

### Experiment 25

ignore

## Experiments to keep

### Experiment 26

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 0 | `./run.sh -S -t hmm_sample_three -M 10000 -m 100 -s 100 --partition=normal` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-198.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-198.csv --first-experiment-only` | [data/experiment-0026/job-198.csv](data/experiment-0026/job-198.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0026/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0026/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0026/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0026/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0026/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0026/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0026/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0026/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0026/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0026/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 27

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 0 | `./run.sh -S -t hmm_sample_three -m 10100 -M 28100 -s 100 --partition=normal` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-200.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-200.csv --first-experiment-only` | [data/experiment-0027/job-200.csv](data/experiment-0027/job-200.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0027/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0027/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0027/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0027/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0027/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0027/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0027/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0027/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0027/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0027/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 28

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 1 | `./run.sh -S -t hmm_sample_three -M 10000 -m 100 -s 100 --partition=longrun` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1876790.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1876790.csv --first-experiment-only` | [data/experiment-0028/job-1876790.csv](data/experiment-0028/job-1876790.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0028/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0028/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0028/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0028/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0028/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0028/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0028/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0028/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0028/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0028/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 29

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 1 | `./run.sh -S -t hmm_sample_three -m 10100 -M 28100 -s 100 --partition=longrun` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1876791.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1876791.csv --first-experiment-only` | [data/experiment-0029/job-1876791.csv](data/experiment-0029/job-1876791.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0029/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0029/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0029/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0029/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0029/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0029/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0029/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0029/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0029/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0029/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 30

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -S -t arithm_sample_three -M 10000 --partition=normal` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-202.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-202.csv --first-experiment-only` | [data/experiment-0030/job-202.csv](data/experiment-0030/job-202.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0030/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0030/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0030/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0030/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0030/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0030/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0030/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0030/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0030/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0030/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 31

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -S -t arithm_sample_three -m 10000 -M 20000 --partition=normal` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-203.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-203.csv --first-experiment-only` | [data/experiment-0031/job-203.csv](data/experiment-0031/job-203.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0031/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0031/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0031/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0031/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0031/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0031/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0031/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0031/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0031/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0031/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 32

Failed due to 8 hour timeout.

### Experiment 33

Expected to failed due to 8 hour timeout.

`./run.sh -S -t arithm_sample_three -m 10000 -M 20000 --partition=longrun`

### Experiment 34

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -S -t arithm_sample_three -M 10000 -m 100 -s 100 --partition=normal` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-204.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-204.csv --first-experiment-only` | [data/experiment-0034/job-204.csv](data/experiment-0034/job-204.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [caec3f4](https://github.com/frnmst/mcmc-comparisons/tree/caec3f4fb75183072f410ada011d5ea2edf31e58) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0034/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0034/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0034/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0034/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0034/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0034/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0034/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0034/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0034/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0034/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 35

Failed due to 8 hour timeout.

### Experiment 36

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 0 | `./run.sh -S -t hmm_sample_three -m 28200 -M 48200 -s 100 --partition=normal` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-215.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-215.csv --first-experiment-only` | [data/experiment-0036/job-215.csv](data/experiment-0036/job-215.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment). Swap memory on the host machine was disabled |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [a264f5a](https://github.com/frnmst/mcmc-comparisons/tree/a264f5a422602b89f66ce7ac5e163e612d6fa3cf) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0036/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0036/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0036/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0036/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0036/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0036/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0036/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0036/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0036/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0036/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 37

Failed probably to insufficient memory. Host crashed and the virtual machine's hard 
drive was corrupted. This was the command: `$ ./run.sh -S -t arithm_sample_three -m 10000 -M 15000 -s 100 --partition=normal`

### Experiment 38

Failed because of insufficient memory: `./run.sh -S -t arithm_sample_three -m 10 -M 10000 -s 10 --partition=normal`

### Experiment 39

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -S -t arithm_sample_three -m 10 -M 3000 -s 10 --partition=normal` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-218.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-218.csv --first-experiment-only` | [data/experiment-0039/job-218.csv](data/experiment-0039/job-218.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [a264f5a](https://github.com/frnmst/mcmc-comparisons/tree/a264f5a422602b89f66ce7ac5e163e612d6fa3cf) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0039/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0039/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0039/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0039/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0039/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0039/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0039/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0039/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0039/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0039/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 40

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 0 | `./run.sh -S -t arithm_sample_three -M 4010 -m 3010 -s 10 --partition=normal` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-222.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-222.csv --first-experiment-only` | [data/experiment-0040/job-222.csv](data/experiment-0040/job-222.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [5f8dabe](https://github.com/frnmst/mcmc-comparisons/tree/5f8dabe2c24a7195cde180b53aa2e39f25c12f78) | - | `8.0.1` | - |

#### Plots

#### Average

![data/experiment-0040/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0040/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0040/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0040/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0040/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0040/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0040/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0040/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0040/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0040/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

## In paper

### Experiment 41

Failed.

`./run.sh -S -t arithm_sample_three -m 100 -M 10000 -s 100 --partition=shortrun --memory=12gb`

```
srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
slurmstepd: error: *** JOB 1877485 ON node02 CANCELLED AT 2019-05-23T16:46:32 DUE TO TIME LIMIT ***
slurmstepd: error: *** STEP 1877485.0 ON node02 CANCELLED AT 2019-05-23T16:46:32 DUE TO TIME LIMIT ***
srun: error: node02: tasks 0-3: Terminated
```

### Experiment 42

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 1 | `./run.sh -S -t hmm_sample_three -m 100 -M 10000 -s 100 --partition=shortrun --memory=12gb` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877486.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877486.csv --first-experiment-only` | [data/experiment-0042/job-1877486.csv](data/experiment-0042/job-1877486.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0042/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0042/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0042/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0042/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0042/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0042/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0042/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0042/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0042/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0042/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 43

Failed.

`./run.sh -S -t arithm_sample_three -m 100 -M 10000 -s 100 --partition=longrun --memory=12gb`

```
srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
slurmstepd: error: *** STEP 1877505.0 ON node01 CANCELLED AT 2019-05-24T00:12:33 DUE TO TIME LIMIT ***
slurmstepd: error: *** JOB 1877505 ON node01 CANCELLED AT 2019-05-24T00:12:33 DUE TO TIME LIMIT ***
srun: error: node01: tasks 0-3: Terminated
```

### Experiment 44

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 1 | `./run.sh -S -t arithm_sample_three -m 100 -M 3000 -s 100 --partition=longrun --memory=12gb` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877557.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877557.csv --first-experiment-only` | [data/experiment-0044/job-1877557.csv](data/experiment-0044/job-1877557.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0044/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0044/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0044/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0044/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0044/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0044/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0044/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0044/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0044/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0044/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 45

Failed. See the raw data [here](data/experiment-0045).

`./run.sh -S -t arithm_sample_three -m 3100 -M 5100 -s 100 --partition=longrun --memory=12gb`

### Experiment 46

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 1 | `./run.sh -S -t hmm_sample_three -m 100 -M 10000 -s 100 --partition=shortrun --memory=12gb` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877895.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877895.csv --first-experiment-only` | [data/experiment-0046/job-1877895.csv](data/experiment-0046/job-1877895.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0046/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0046/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0046/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0046/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0046/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0046/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0046/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0046/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0046/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0046/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 47

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| hmm_sample_three | 1 | `./run.sh -S -t hmm_sample_three -m 100 -M 10000 -s 100 --partition=shortrun --memory=12gb` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877896.csv` ; `./run.sh --graph-only -t hmm_sample_three --output-file=job-1877896.csv --first-experiment-only` | [data/experiment-0047/job-1877896.csv](data/experiment-0047/job-1877896.csv) | [using a patched version for mcintyre of hmm.pl](https://github.com/frnmst/mcmc-comparisons#the-hmm-experiment) |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0047/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0047/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

![data/experiment-0047/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png](data/experiment-0047/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_hmm_sample_three.png)

#### First run only

![data/experiment-0047/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0047/plot_time_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0047/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0047/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

![data/experiment-0047/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png](data/experiment-0047/plot_prob_over_time_mh_vs_gibbs_vs_rejection_hmm_sample_three.png)

### Experiment 48

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 1 | `./run.sh -S -t arithm_sample_three -m 100 -M 3000 -s 100 --partition=longrun --memory=12gb` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877897.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877897.csv --first-experiment-only` | [data/experiment-0048/job-1877897.csv](data/experiment-0048/job-1877897.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0048/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0048/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0048/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0048/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0048/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0048/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0048/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0048/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0048/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0048/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 49

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 1 | `./run.sh -S -t arithm_sample_three -m 100 -M 3000 -s 100 --partition=longrun --memory=12gb` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877898.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877898.csv --first-experiment-only` | [data/experiment-0049/job-1877898.csv](data/experiment-0049/job-1877898.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0049/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0049/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0049/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0049/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0049/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0049/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0049/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0049/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0049/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0049/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 50

#### Summary

| Name | Computer id | Command | Data | Comment |
|------|-------------|---------|------|---------|
| arithm_sample_three | 1 | `./run.sh -S -t arithm_sample_three -m 3100 -M 4200 -s 100 --partition=longrun --memory=12gb` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877899.csv` ; `./run.sh --graph-only -t arithm_sample_three --output-file=job-1877899.csv --first-experiment-only` | [data/experiment-0050/job-1877899.csv](data/experiment-0050/job-1877899.csv) | |

#### Software Versions

| cplint | mcmc-comparision | Adapative-MCMC | SWI Prolog | XSB Prolog |
|--------|------------------|----------------|------------|------------|
| [fe60804](https://github.com/friguzzi/cplint/tree/fe60804fd63e3ac41804e1d8e618415144c61fd3) | [50ec327](https://github.com/frnmst/mcmc-comparisons/tree/50ec32740601ada4d8328c07f78067e88676bab0) | - | `8.1.5` | - |

#### Plots

#### Average

![data/experiment-0050/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0050/plot_time_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

![data/experiment-0050/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png](data/experiment-0050/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_avg_of_arithm_sample_three.png)

#### First run only

![data/experiment-0050/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0050/plot_time_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0050/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0050/plot_prob_over_sample_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

![data/experiment-0050/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png](data/experiment-0050/plot_prob_over_time_mh_vs_gibbs_vs_rejection_arithm_sample_three.png)

### Experiment 51

Run 3 failed. See the raw data [here](data/experiment-0051).

`./run.sh -S -t arithm_sample_three -m 3100 -M 4200 -s 100 --partition=longrun --memory=12gb`

### Experiment 97 (49 and 51)

### Experiment 98 (48 and 50)

### Experiment 99 (44 and 45, truncated at 4200 samples)
