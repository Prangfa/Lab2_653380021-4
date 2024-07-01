import pytest
import source.print_promotion as print_promotion

def test_print_promotion():
    result = print_promotion.print_promotion(200)
    assert result == "Thank you and see you next time"

def test_print_promotion():
    result = print_promotion.print_promotion(500)
    assert result == "Free ice cream cone = 1" 
    
def test_print_promotion():
    result = print_promotion.print_promotion(700)
    assert result == "Free chocolate cake = 1"

def test_print_promotion():
    result = print_promotion.print_promotion(1200)
    assert result == "Free ice cream cone = 1 and chocolate cake = 1" 

def test_print_promotion():
    result = print_promotion.print_promotion(2400)
    assert result == "Free ice cream cone = 2 and chocolate cake = 2"

def test_print_promotion():
    result = print_promotion.print_promotion(3500)
    assert result == "Free ice cream cone = 3 and chocolate cake = 2" 

def test_print_promotion():
    result = print_promotion.print_promotion(699)
    assert result == "Free ice cream cone = 1"

def test_print_promotion():
    result = print_promotion.print_promotion(-100)
    assert result == KeyError

def test_print_promotion():
    result = print_promotion.print_promotion(ABC)
    assert result == KeyError




    