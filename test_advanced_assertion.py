import pytest
import test_sample1

def test_advanced_assertion():
    result =  test_sample1.add(3, 5)
    assert result == 8, f"Expected 8 but got {result}"

# To skip some test use the below decorator
@pytest.mark.skip(reason="Not implemented yet")
def test_substract():
    result = test_sample1.substract(5, 2)
    assert result == 3

# We could also categorize test with category
#To run this pytest -m slow
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(2)
    assert True