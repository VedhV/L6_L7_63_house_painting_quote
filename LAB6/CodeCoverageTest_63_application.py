import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days

def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500

def test_distemper_minimum():
    assert painting_quote("distemper", 100, 1, False) == 5000

def test_emulsion_quote():
    assert painting_quote("emulsion", 300, 1, False) == 6000

def test_large_area_discount():
    assert painting_quote("emulsion", 2500, 1, False) == 45000

def test_invalid_paint():
    with pytest.raises(ValueError):
        painting_quote("unknown", 100, 1, False)

def test_invalid_area():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 1, False)

def test_invalid_coats():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 100, 0, False)

def test_exterior_distemper():
    with pytest.raises(ValueError):
        painting_quote("distemper", 100, 1, True)

def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2

def test_rough_litres():
    assert paint_litres(120, 1, "rough") == 2

def test_litres_rounding():
    assert paint_litres(101, 1, "smooth") == 2

def test_unknown_surface():
    with pytest.raises(ValueError):
        paint_litres(100, 1, "unknown")

def test_crew_days():
    assert crew_days(800, 2, False) == 1

def test_crew_days_rounding():
    assert crew_days(801, 2, False) == 2

def test_wallpaper_removal():
    assert crew_days(800, 2, True) == 3

def test_invalid_painters():
    with pytest.raises(ValueError):
        crew_days(800, 0, False)
