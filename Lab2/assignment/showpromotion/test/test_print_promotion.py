import pytest
import source.print_promotion as print_promotion

def test_print_promotion():
    result = print_promotion.print_promotion(200)
    assert result == NO_GIFT

    