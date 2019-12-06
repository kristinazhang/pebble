# Pebble Fuel Cell
This repository contains information of creating pebble fuel cell using OpenMC

## Description
Pebble fuel cell is a nuclear fuel with thousands of Tristructural-isotropic (TRISO) coated particles inside. The design use in this repository is from HTR-10.

![Illustration of fuel pebble and TRISO coated particles](https://github.com/kristinazhang/pebble/blob/master/pebbledescription.png?raw=true)

Source : William K.T. *Evaluation of The Initial Critical Configuration of the HTR-10 Pebble-Bed Reactor*. Idaho: Idaho National laboratory; 2006


## OpenMC
OpenMC is an open-source Monte Carlo transport simulation code developed by members of the Computational Reactor Physics Group at the Massachusetts Institute of Technology.
All information regarding OpenMC can be found in [here](https://github.com/openmc-dev/openmc/tree/7a4c5b47342b175b3f113c6a6e28db10e0bc8ae7).

## How to Run
This code works with python3 and the latest OpenMC v0.11.0
To execute just simply type:
```
python3 pebble.py --type [selected lattice type]
```

## Result
The lattice type:
  1. random
![Random](https://github.com/kristinazhang/pebble/blob/master/PEBBLE_xy_random.png?raw=true)
  
  2. rectanguler
![Rectanguler](https://github.com/kristinazhang/pebble/blob/master/PEBBLE_xy_rectanguler.png?raw=true)

  3. hexagonal
![Hexagonal](https://github.com/kristinazhang/pebble/blob/master/PEBBLE_xy_hexagonal.png?raw=true)
