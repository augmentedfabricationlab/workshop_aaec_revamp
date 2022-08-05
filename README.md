# Robotic 3D Printing on Knitted Formwork

## Requirements 
* [Rhinoceros 3D 7.0](https://www.rhino3d.com/): Update Rhino to the newest version

**Quick links:** [compas docs](https://compas-dev.github.io/main/) | [compas_fab docs](https://gramaziokohler.github.io/compas_fab/latest/)

* [Rhinoceros 3D 7.0](https://www.rhino3d.com/)
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))
* [VS Code](https://code.visualstudio.com/) with the following `Extensions`:
  * `Python` (official extension)
  * `EditorConfig for VS Code` (optional)
  * `Docker` (official extension, optional)

## Set-up and Installation

### 1. Setting up the Anaconda environment with COMPAS

#### Execute the commands below in Anaconda Prompt as Administator:
	
    (base) conda config --add channels conda-forge
    (base) conda create -n revamp compas_fab --yes
    (base) conda activate revamp
    
#### Verify Installation
    (revamp) pip show compas_fab

####
    Name: compas-fab
    Version: 0.xx
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

#### Install on Rhino

    (revamp) python -m compas_rhino.install -v 7.0


### 2. Installation of Dependencies

    (revamp) conda install git

#### Robotic Knitcrete
    
    (revamp) python -m pip install git+https://github.com/augmentedfabricationlab/robotic_knitcrete@master#egg=robotic_knitcrete
    (revamp) python -m compas_rhino.install -p robotic_knitcrete -v 7.0
    
NOTE: If you are not using Rhino 6.0, after the above statement, add `-v` followed by the version of your Rhino software (i.e `-v 5.0` or `-v 7.0`)

### 3. Cloning and installing the Course Repository

* Create a workspace directory: C:\Users\YOUR_USERNAME\workspace
* Open Github Desktop, clone the [workshop_aaec_revamp](https://github.com/augmentedfabricationlab/workshop_aaec_revamp) repository into you workspace folder 
* Install within your env (in editable mode):

```
(revamp) cd C:\Users\YOUR_USERNAME\workspace
(revamp) python -m pip install -e workshop_aaec_revamp
(revamp) python -m compas_rhino.install -p workshop_aaec_revamp -v 7.0
```

### 4. Notes on RPC:

Careful: RPC (Remote Procedure Call) for calling numpy functions from within Rhino, is using the CPython Interpreter of the latest installed environment, not defined specifically. If another interpreter should be used, this can be defined when creating the Proxy object.

### Credits

