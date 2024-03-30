# Lecture-OSESM-2024

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/tschmdt/lecture-spring-2024/blob/main/LICENSE)

First assignment for the course "Open Source Energy System Modelling" at TU Wien

The code can be seen as a base for a techno-economic sensitivity analysis of wind turbines. Here, parameters of the Vestas V90 Onshore Turbine are considered.
Function #1 takes the desired capacity to be installed as input and returns the number of turbines that need to be installed.
Function #2 calculates the energy output of a wind farm (several single turbines) over the lifetime. Variable parameters are the desired intalled capacity (of the wind farm), average wind speed at the location and full load hours.
The code can be adaped to compare diffrent turbines, locations (wind speed) or technologies at certain locations (solar vs wind ws biomass). Also carbon paybacktime and more can be added to this base code.
