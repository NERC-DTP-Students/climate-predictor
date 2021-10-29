[![codecov](https://codecov.io/gh/NERC-DTP-Students/climate-predictor/branch/main/graph/badge.svg?token=B7FWJCAPWX)](https://codecov.io/gh/NERC-DTP-Students/climate-predictor)
![Unit tests on multiple python versions](https://github.com/NERC-DTP-Students/climate-predictor/actions/workflows/unit-tests.yml/badge.svg)
![Unit tests on multiple operating systems](https://github.com/NERC-DTP-Students/climate-predictor/actions/workflows/os-tests.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/climate-predictor/badge/?version=latest)](https://climate-predictor.readthedocs.io/en/latest/?badge=latest)




# Climate Predictor Package 
<div id="top"></div>
<p>
      <a href="https://climate-predictor.readthedocs.io/en/latest/"><strong>Explore the docs </strong></a>
    <br/>
    <br/>
      .
      <a href="https://github.com/NERC-DTP-Students/climate-predictor/issues">Report Bug</a>
      .
      <a href="https://github.com/NERC-DTP-Students/climate-predictor/issues">Request Feature</a>
</p>


<!-- TABLE OF CONTENTS alter this when readme is finalised -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#basics">Basics</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#scientific-background-and-model-implementation">Scienitific Background and Model Implementation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#example">Example</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#contributing">Contributing</a></li> 
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#issues">Issues</a></li>
  </ol>
</details>

## **Basics**

This package predicts planet surface temperature as the result of changing cloud cover and land usage over a chosen period of time. The package is a standalone executable file that runs on Mac, Windows and Linux operating systems. All parameters can be changed within a GUI so there is no need to be familiar with any programming languages.

### **Two modes for customised use**
The default mode is for a investigating surface temperatures of the Earth. 

**Parameters**

+ Percentage cloud cover
+ Land usage propotions (ice, water, forest, desert)  

For each parameter the user sets an initial value and a change with time. A timeframe is selected and the global surface temperature over time is plotted.

The advanced option is for investigating surface temperatures of a generic planet. Note that if the albedo is set to a non-zero value in the advanced option, the albedo overrides the cloud cover and land cover parameters in the default mode.

**Paramters**
+ Albedo
+ &#949; <sub>1</sub> - emissivity of the first atmospheric layer
+ &#949; <sub>2</sub> - emissivity of the second atmospheric layer
+ S<sub>0</sub> - flux from the star (defaults to present day Sun)

### **Adjustable and easy to use plotting tool**
A plot of temperature against a chosen input variable will be generated based on the user inputs. This plot can then be saved by the user by pressing one button. 

**Options**
+ X-axis (time, or any other parameter which changes with time)
+ Displayed temperature (any combination of surface temperature, temperature of atmospheric layer one and temperature of atmospheric layer two)

<p align="right">(<a href="#top">back to top</a>)</p>

## Installation

To install the software download the appropriate single executable file for your operating system from the repository. If you want to run the code directly clone this github repository and run gui.py.

<p align="right">(<a href="#top">back to top</a>)</p>

## Scientific Background and Model Implementation 
|![Two layer atmosphere!](examples/two_layer.png)|
|:--:|
|Two layer atmosphere model used in this program. Image credit <a href='https://biocycle.atmos.colostate.edu/shiny/2layer/'> here.</a>|

This package is for modelling the greenouse effect for a two layer model of the atmosphere. The atmosphere is assumed transparent to incoming radiation (in the visible range), but with a certain proportion reflected (set by the albedo, &alpha;). The atmosphere absorbs and reradiates a proportion of the outgoing radiation (in the infrared range) set by the emissivity (&varepsilon;) of the two atmospheric layers. The package solves for the temperature of the surface and the two layers in the atmosphere.

In the package the albedo is set by the cloud cover and land usage proportions or can be set manually by the user in advanced options. Different land surfaces have different albedos, for example ice reflects more incoming radiation than forest. The emissivity of the layers can be altered in advanced options as can the incoming stellar flux.

**Assumptions**
+ The Earth radiates as a black body
+ Atmospheric properties across the Earth are uniform (1D model)
+ The atmosphere consists of two layers with constant emissivities
+ Cloud cover is uniformly distributed across the surface (all land uses are equally blocked by clouds)

**Input Variables**

Basic
+ Land usage - fraction of surface covered by water, ice, forest, desert
+ Cloud cover - percentage surface coverage

Advanced
+ Albedo
+ &varepsilon;<sub>1</sub> and &varepsilon;<sub>2</sub> emissivity of the two atmospheric layers

For every input variable an initial value and change per time interval can be chosen. The overall length of time to be considered is also chosen. All input variables default to present day values.

**Output Variables**

Temperature of the surface, T<sub>surface</sub>, and the two atmospheric layers, T<sub>lower</sub> and T<sub>upper</sub>.

**Implementation**

The model creates timesteps which are one tenth of the chosen time interval. At each timestep the model uses a matrix to solve a series of simultaneous equations for T<sub>lower</sub>, T<sub>upper</sub> and T<sub>surface</sub>. The varying quantities are then incremented by one tenth of the change per chosen time interval and the process repeats to build a smooth curve of global temperatures with time/varying quantity. The model solves for the temperature based on a snapshot of atmospheric properties at a given time. It does not account for transport processes in the atmosphere or thermal properties such as specific heat capacity which may delay the heating or cooling of the atmosphere.

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

The usage instructions are the same when running the Python script or the stand alone executable file apart from the different options in step 1. 

1. To launch the GUI:
  + Python: Run <a href='https//:github.com/NERC-DTP-Students/climate-predictor/main/climatepredictor/gui.py'>gui.py</a>.
  + Exe: Double click on the gui icon

2. Once the GUI is running input the initial values and change with time for cloud cover.

3. Choose current and final land coverage using either the sliders or the entry boxes beneath. **Entries in the boxes must be inputted in descending order i.e forest then ice etc.)**

4. Choose timespan to be investigated either using the slider or the input box. If a parameter which has a maximum value (e.g. albedo) is changing with time, the maximum timespan that can be investigated is the time taken for that parameter to reach its maximum value.

5. In the plot options select an x-axis and how many temperatures you want to be displayed.

6. The plot will automatically update.

7. Press save plot to save the plot. The plot will save in the same directory as the GUI application. To alter this just write the relative path you want to save the file to into the entry box. The .png suffix is automatically added.

<p align="right">(<a href="#top">back to top</a>)</p>

## Example

In this simple example, shows change in surface temperature for a 10% increase in cloud cover every 50 years and all forest becoming desert over the same time period. _The numbers reference the steps in the Usage section above._

1. Launch the GUI

2. Input initial and change in cloud cover
![Input the cloud cover!](examples/set_clouds.png)

3. Input initial and final land usage
![Input land usage!](examples/set_land_use.png)

4. Choose time interval and timespan to be investigated
![Input the timespace!](examples/set_time.png)

5. Choose x axis and number of temperatures to be displayed
![Choose plot options!](examples/set_plot_options.png)

6. Plot automatically updates
![Resulting plot!](examples/graph.png)

7. Input your chosen filename and press Save to save the file
![Saving plot!](examples/save.png)

<p align="right">(<a href="#top">back to top</a>)</p>

## Documentation
The package is fully documented on <a href="https://climate-predictor.readthedocs.io/en/latest/index.html"><strong>ReadTheDocs</strong></a>. 
<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing
If you would like to contribute to the project, please get in touch with one of the members of the GitHub organisation <a href="https://github.com/NERC-DTP-Students/people">NERC-DTP-Students </a> and ask to be added as a collaborator.

This project and everyone participating is expected to follow a basic Code of Conduct:
+ Treat all others with respect and dignity.
+ Offer constructive feedback to others' contributions; never be deameaning or dismissive.

Contributors deemed to be in violation of the code of conduct will be removed from the repository.

The general workflow for contributing to the project is as follows:
+ Create an issue on GitHub.
+ Ensure your local copy of the repository is up to date, and branch the repository with a sensible name beginning with the issue number, e.g. '45-solver-broken'.
+ Fix the issue, commit your changes to the branch and push to GitHub. Ensure your commit message includes the issue number, e.g. "#45 Fixed Solver file"
+ Create a pull request for your branch to be merged with the master.
+ This will be reviewed by another collaborator, and then merged with the master.
+ The branch should now be deleted.

You can find the style information in the flake8 file in the repository.

If you have any questions, please contact one of the members of the organisation, as above.

<p align="right">(<a href="#top">back to top</a>)</p>

## License
This package is distributed under the MIT license. For more information see <a href='https://github.com/NERC-DTP-Students/climate-predictor/main/license'>LICENSE</a>.

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgements

+ Basic model inspired based on <a href='https://biocycle.atmos.colostate.edu/shiny/2layer'>this diagram </a>
+ GUI theme based on: <a href='https://github.com/rdbende/Sun-Valley-ttk-theme'> this template.</a>
+ Slider based on: <a href='https://github.com/MenxLi/tkSliderWidget'> this code. </a>

<p align="right">(<a href="#top">back to top</a>)</p>

## Issues
This project is still in development - for a full list of ongoing issues or to report a bug please see the <a href='https://github.com/NERC-DTP-Students/climate-predictor/issues'>Issues</a> tab.   
  
<p align="right">(<a href="#top">back to top</a>)</p>
