---
layout: page
title: Getting Started
---

### Requirements

* Rhino 7 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)
* [Docker Community Edition](https://www.docker.com/get-started): Download it for [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows). Leave "switch Linux containers to Windows containers" disabled.

### Dependencies

* [COMPAS](https://compas-dev.github.io/)
* [COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)
* [UR Fabrication Control](https://github.com/augmentedfabricationlab/ur_fabrication_control)

### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge

#### Windows
    (base) conda create -n revamp compas_fab=0.22.0 --yes
    (base) conda activate revamp

#### Mac
    (base) conda create -n revamp compas_fab=0.22.0 python.app --yes
    (base) conda activate revamp
    

#### Verify Installation

    (revamp) pip show compas_fab

    Name: compas-fab
    Version: 0.22.0
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

#### Install on Rhino

    (revamp) python -m compas_rhino.install -v 7.0


### 2. Installation of Dependencies

    (revamp) conda install git

#### UR Fabrication Control
    
    (revamp) python -m pip install git+https://github.com/augmentedfabricationlab/ur_fabrication_control@master#egg=ur_fabrication_control
    (revamp) python -m compas_rhino.install -p ur_fabrication_control -v 7.0


### 3. Cloning and installing the Course Repository

* Create a workspace directory: C:\Users\YOUR_USERNAME\workspace
* Open Github Desktop, clone the [workshop_aaec_revamp](https://github.com/augmentedfabricationlab/workshop_aaec_revamp) repository into you workspace folder 
* Install within your env (in editable mode):

```
(revamp) cd C:\Users\YOUR_USERNAME\workspace
(revamp) python -m pip install -e workshop_aaec_revamp
(revamp) python -m compas_rhino.install -p workshop_aaec_revamp -v7.0
```

### 4. Cloning and installing additional repositories

Simulation of the mobile platform:
* [rbvogui_common](https://github.com/RobotnikAutomation/rbvogui_common)
* [ewellix_description](https://github.com/RobotnikAutomation/ewellix_description)
* [robotnik_sensors](https://github.com/augmentedfabricationlab/robotnik_sensors)
* [mobile_fabrication_control](https://github.com/augmentedfabricationlab/mobile_fabrication_control)

Install mobile_fabrication_control

    (revamp) python -m pip install -e mobile_fabrication_control
    (revamp) python -m compas_rhino.install -p mobile_fabrication_control -v7.0


**Voilà! You can now go to VS Code, Rhino or Grasshopper to run the example files!**
