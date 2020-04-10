import pytest
@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    from potential_class import potential
    from QHO import quantum_harmonic_oscilator 
    import wavefunction_generator 
    from analytical_E_levels import analytical_E