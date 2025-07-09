#tests/integration/test_main.py

from main import *
from fastapi import * 
import pytest 

def test_add_route(operation: OperationRequest):
    result = add(operation.a, operation.b)

    assert OperationResponse(result=result)

def test_subtract_route(operation: OperationRequest):
    result = subtract(operation.a, operation.b)

    assert OperationResponse(result=result)

def test_multiply_route(operation: OperationRequest):
    result = multiply(operation.a, operation.b)

    assert OperationResponse(result=result)

def test_divide_route(operation: OperationRequest):
    result = divide(operation.a, operation.b)

    assert OperationResponse(result=result)