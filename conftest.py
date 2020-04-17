import pytest
@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    """
    Imports modules required for the running of pytest test files

    """
    from potential_class import potential
    from quantum_particle import q_particle 
    import wavefunction_generator 
    from analytical_E_levels import analytical_E
    from probability_plotter import normalise