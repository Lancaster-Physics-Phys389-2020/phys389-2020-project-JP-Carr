# phys389-2020-project-JP-Carr *(python 3.0+)*

## INSTRUCTIONS
- To generate a single set of wavefunctions *ψ* and energy eigenvalues *Eₙ*, run "wavefunction_generator.py", changing the value of "N" to the desired number of integration steps (NOTE: Increases in "*N*" increase run time exponentially). 
- To generate a set of *ψ* and *Eₙ* results for multiple values of "*N*", run "multiprocess_generator.py" with "simulations" set to the number of desired simulations to be run. Simulation start at a value of *N=50*, which increase by 50 for each successive simulation.
- To view the generated wavefuncton *ψ* and its comparison to an analytically generated wavefunction run "wavefunction_plotter.py", changing the variable "wave_function_csv" to the path of the desired csv located in "phys389-2020-project-JP-Carr\wavefunctions".  
- To view the comparisons of the numerically calculated energy eigenvalues *Eₙ* to their analytically generated counterparts, run "energy_comparison.py".

## CONTENTS
- **analytical_E_levels.py** - produces energy eigenvalues *Eₙ* as derived from the non-dimentional Scrödinger equation
- **analytical_psi.py** - produces wavefunction *ψ*, the solution the non-dimentional Scrödinger equation
- **conftest.py** - allows for modules relevent to test files to be loaded when running py.test command
- **energy_comparison.py** - compares energy levels produced by "wavefunction_generator.py" to those from "analytical_E_levels.py"
- **\energy_levels** - directory for CSV file containing energy eigenvalues *Eₙ* for differenct values of *N*
- **error.py** - facilitates the quick production of quick error messages with an audio que
- **linear_timer.py** - times "wavefunction_generator.py" at different values of *N*
- **multiprocess_generator.py** - runs "wavefunction_generator.py" at multiple values of *N* 
- **potential_class.py** - contains the "potential" class, which describes
- **probability_plotter.py**
- **quantum_particle.py**
- **\test_scripts**
   - e
- **time_plotter.py**
- **\wavefunctions** - 
- **wavefunction_generator.py**
- **wavefunction_plotter.py**
-

## Required Modules
-	Numpy
-	Matplotlib
-	Pandas
-	Scipy
-	OS
-	Math
-	Multiprocessing
-	Time
-	Copy
-	Pytest
-	Sys
-	Random

