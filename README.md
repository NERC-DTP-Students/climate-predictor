[![codecov](https://codecov.io/gh/NERC-DTP-Students/climate-predictor/branch/main/graph/badge.svg?token=B7FWJCAPWX)](https://codecov.io/gh/NERC-DTP-Students/climate-predictor)
![Unit tests on multiple python versions](https://github.com/NERC-DTP-Students/climate-predictor/actions/workflows/unit-tests.yml/badge.svg)
![Unit tests on multiple operating systems](https://github.com/NERC-DTP-Students/climate-predictor/actions/workflows/os-tests.yml/badge.svg)




# Climate Predictor Package 
<p>
      <a href="https://climate-predictor.readthedocs.io/en/latest/index.html"><strong>Explore the docs </strong></a>
    <br/>
    <br/>
      .
      <a href="https://github.com/NERC-DTP-Students/climate-predictor/issues">Report Bug</a>
      .
      <a href="https://github.com/NERC-DTP-Students/climate-predictor/issues">Request Feature</a>
</p>

## Basics

This package predicts planet surface temperature as the result of changing cloud cover, land usage and the atmosphere CO\u2082 concentration over a chosen period of time. The package is a standalone executable file that runs on Mac, Windows and Linux operating systems. All parameters can be changed within a GUI so there is no need to be familiar with coding.

### Two modes for customised use
The default mode is for a investigating surface temperatures of the Earth. 
**Parameters**
+ CO2 concentration
+ Percentage cloud cover
+ Land usage propotions (ice, water, forest, desert)  
For each parameter the user sets an initial value and a change with time. A timeframe is selected and global temperatures over time is plotted.

The advanced option is for investigating surface temperatures of a generic planet.
**Paramters**
+ Albedo
+ epsilon_1 - emissivity of the first atmospheric layer
+ epsilon_2 - emissivity of the second atmospheric layer
+ S_0 - flux from the star (defaults to present day Sun)

### Adjustable and easy to use plotting tool
A plot will be generated based on the user inputs. This plot can then be saved by the user by pressing one button.
**Options**
+ X-axis (time, or any other parameter which changes with time)
+ Y-axis (any combination of surface temperature, temperature of layer one and temperature of layer two)



## Installation

## Scientific Background

## Example

## Documentation
The package is fully documented on <a href="https://climate-predictor.readthedocs.io/en/latest/index.html"><strong>ReadTheDocs</strong></a>

## Contributing
This package was developed by students on the NERC DTP as part of the Software Engineering module run by the University of Oxford Doctoral Training Centre (DTC). If you wish to contribute to this package please contact one of the listed contributors.

## Acknowledgements

+ Basic model inspired based on <a href='https://biocycle.atmos.colostate.edu/shiny/2layer'>this diagram </a>
+ GUI theme based on: <a href='https://github.com/rdbende/Sun-Valley-ttk-theme'> this template.<\a>

## Issues
This project is still in development - for a full list of ongoing issues or to report a bug please see the <a href='https://github.com/NERC-DTP-Students/climate-predictor/issues'>Issues</a> tab.   
  

