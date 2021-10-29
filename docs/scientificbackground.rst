Scientific background
======================

.. toctree::
   :hidden:

This package is for modelling the greenouse effect for a two layer model of the atmosphere. The atmosphere is assumed transparent to incoming radiation (in the visible range), but with a certain proportion reflected (set by the albedo, :math:`\alpha`;). The atmosphere absorbs and reradiates a proportion of the outgoing radiation (in the infrared range) set by the emissivity (:math:`\varepsilon`) of the two atmospheric layers. The package solves for the temperature of the surface and the two layers in the atmosphere.

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
+ :math:`\varepsilon` :sub:`1` and :math:`\varepsilon` :sub:`2` emissivity of the two atmospheric layers

For every input variable an initial value and change per time interval can be chosen. The overall length of time to be considered is also chosen. All input variables default to present day values.

**Output Variables**

Temperature of the surface, T :sub:`s` , and the two atmospheric layers, T :sub:`1` and T :sub:`2`.

**Implementation**

The model creates timesteps which are one tenth of the chosen time interval. At each timestep the model uses a matrix to solve a series of simultaneous equations for Tb:sub:`s` , T :sub:`1` and T :sub:`2` The varying quantities are then incremented by one tenth of the change per chosen time interval and the process repeats to build a smooth curve of global temperatures with time/varying quantity. The model solves for the temperature based on a snapshot of atmospheric properties at a given time. It does not account for transport processes in the atmosphere or thermal properties such as specific heat capacity which may delay the heating or cooling of the atmosphere.