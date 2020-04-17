# phys389-2020-project-JP-Carr *(python 3.0+)*

## INSTRUCTIONS
- To generate a single set of wavefunctions *ψ* and energy eigenvalues *Eₙ*, run "wavefunction_generator.py", changing the value of "N" to the desired  number of integration steps (NOTE: Increases in "N" increase run time exponentially). 
- To generate a set of *ψ* and *Eₙ* results for multiple values of "N", run "multiprocess_generator.py" with "simulations" set to the number of desired simulations to be run. Simulation start at a value of "N"=50, which increase by 50 for each sucessive simulation.
- To view the generated wavefuncton and its comparison to an analytically generated wavefunction run "wavefunction_plotter.py", changing the variable "wave_function_csv" to the path of the desired csv located in "phys389-2020-project-JP-Carr\wavefunctions".  
 - e comparison

## CONTENTS
analytical_E_levels.py
analytical_psi.py
conftest.py
energy_comparison.py
energy_levels
error.py
linear_timer.py
multiprocess_generator.py
potential_class.py
probability_plotter.py
quantum_particle.py
README.md
test_scripts
time_plotter.py
wavefunctions
wavefunction_generator.py
wavefunction_plotter.py

## Required Modules
