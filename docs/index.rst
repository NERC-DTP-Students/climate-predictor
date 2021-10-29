

Welcome to Climate Predictor's documentation!
=============================================
This documentation is for the 2-Layer Atmosphere Model predicting planet surface temperatures based on cloud cover and land use. 

This TCL and Python library visualizes predicted planet surface temperatures based on changing cloud cover and land usage proportions(ice, water, forest, desert)
over a chosen time period. 

More detail on this model can be found in the Scientific Background and Model Implementation section.


Quickstart
-------------------------

The model can be used by running a stand alone executable file downloadable from the github repository https://github.com/NERC-DTP-Students/climate-predictor

Alternatively the model can be run in a Python editor of your choice by cloning the repository and running gui.py using the follwing steps.

1. Open the Terminal
2. Run the following code:

   .. code-block:: python

      python3 -m venv venv
      source venv/bin/activate            #setting up a virtual environment 
      git clone https://github.com/NERC-DTP-Students/climate-predictor
      cd climate-predictor                #go to the climate-predictor directory
      code .                              #opens VScode with the file directory 
      
3. Open gui.py in the climatepredictor file 
4. Run gui.py 

Usage 
-------

..toctree::
  :hidden:

  usage

The :doc:`usage` section contains the documentation for the classes and the functions within the package. 

Exploration
-------------------------

.. toctree::
   :hidden:
   
   exploration

The :doc:`exploration` section contains the documentation for the classes and the functions within the package. 


Scientific Background
-----------------------

.. toctree::
   :hidden:

   scientificbackground

See the :doc:`scientificbackground` section for background to the model.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
