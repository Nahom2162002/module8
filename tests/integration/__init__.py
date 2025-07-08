#tests/integration/test_main.py

from main import app 
from fastapi import * 
import pytest 

def test_http_exception_handler(request: Request, exc: HTTPException):
    