

Welcome to Climate Predictor's documentation!
=============================================
This documentation is for the 2-Layer Atmosphere Model predicting planet surface temperatures based on cloud cover and CO2. 
See below for How to Start.

Scientific background
------------------------
This TCL and Python library visualizes predicted planet surface temperatures based on changing cloud cover and land usage proportions(ice, water, forest, desert)
up to 50 years. 
The model assumes two layers of atmosphere and a single layer of surface, and that the solar radiation warms the surface without affecting the atmosphere. 
The warm surface then heats the overlying atmosphere via thermal radiation and upward convective heat flux. 

More detail on this model can be found .. _here: https://biocycle.atmos.colostate.edu/shiny/2layer/


Quickstart
-------------------------
Running on the vscode 

1. Open the Terminal
2. Run the following code:
.. example-code::
   .. code-block:: python
      python3 -m venv venv
      source venv/bin/activate            #setting up a virtual environment 
      git clone https://github.com/NERCT-DTP-Students/climate-predictor
      cd climate-predictor                #go to the climate-predictor directory
      code .                              #opens VScode with the file directory 
      
3. Open gui.py in the climatepredictor file 
4. Run gui.py 

Exploration
-------------------------

.. toctree::
   :hidden:
   
   exploration

The :doc:'Exploration' section contains the documentation for the classes and the functions within the package 


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
