import pytest
import uuid
from app.models.calculation import Calculation, AbstractCalculation, Addition, Subtraction, Multiplication, Division

def test_abstract_calculation_get_result_not_implemented():
    calc = Calculation(type="calculation", inputs=[1, 2])
    with pytest.raises(NotImplementedError):
        calc.get_result()

def test_calculation_create_invalid_type():
    with pytest.raises(ValueError, match="Unsupported calculation type: calculus"):
        Calculation.create("calculus", uuid.uuid4(), [1, 2])

@pytest.mark.parametrize("calc_class", [Addition, Subtraction, Multiplication, Division])
def test_calculation_invalid_input_type(calc_class):
    calc = calc_class(inputs="not a list")
    with pytest.raises(ValueError, match="Inputs must be a list of numbers."):
        calc.get_result()

@pytest.mark.parametrize("calc_class", [Addition, Subtraction, Multiplication, Division])
def test_calculation_insufficient_inputs(calc_class):
    calc = calc_class(inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        calc.get_result()

def test_calculation_repr():
    calc = Addition(inputs=[1, 2])
    repr_str = repr(calc)
    assert "type=addition" in repr_str
    assert "inputs=[1, 2]" in repr_str