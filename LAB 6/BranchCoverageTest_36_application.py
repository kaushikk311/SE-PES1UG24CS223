
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# 1. Invalid axle count (True branch)
def test_invalid_axle_count():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


# 2. Valid axle count (False branch of invalid condition)
def test_valid_axle_count():
    assert toll_for(2, False, False) == 100


# 3. Axle count exists in BASE_TOLL
@pytest.mark.parametrize("axles, expected", [
    (2, 100),
    (3, 150),
    (4, 250)
])
def test_base_toll_axles(axles, expected):
    assert toll_for(axles, False, False) == expected


# 4. Axle count does not exist in BASE_TOLL
def test_unknown_axle_count():
    assert toll_for(5, False, False) == 400


# 5. Peak hour condition (True branch)
def test_peak_hour():
    assert toll_for(2, True, False) == 125


# 6. Non-peak hour condition (False branch)
def test_non_peak_hour():
    assert toll_for(2, False, False) == 100


# 7. FASTag condition (True branch)
def test_fastag():
    assert toll_for(2, False, True) == 90


# 8. FASTag condition (False branch)
def test_no_fastag():
    assert toll_for(2, False, False) == 100


# 9. FASTag with 2 axles (True branch)
def test_fastag_two_axles():
    assert toll_for(2, False, True) == 90


# 10. FASTag with more than 2 axles (False branch)
def test_fastag_other_axles():
    assert toll_for(3, False, True) == 142.5


# 11. Exempt vehicle condition (True branch)
def test_ambulance_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_exempt():
    assert toll_charge("fire_engine", 2, False, False) == 0


# 12. Non-exempt vehicle condition (False branch)
def test_normal_vehicle():
    assert toll_charge("car", 2, False, False) == 100


# 13. Pass advice: cost greater than pass price
def test_buy_pass():
    assert pass_advice([(False, False)], 2, 90) == "buy_pass"


# 14. Pass advice: cost equal to pass price
def test_either_option():
    assert pass_advice([(False, False)], 2, 100) == "either"


# 15. Pass advice: cost less than pass price
def test_pay_per_trip():
    assert pass_advice([(False, False)], 2, 110) == "pay_per_trip"


# 16. Multiple trips (loop executes multiple times)
def test_multiple_trips():
    trips = [(False, False), (True, False)]
    assert pass_advice(trips, 2, 200) == "buy_pass"


# 17. Empty trips (loop executes zero times)
def test_empty_trips():
    assert pass_advice([], 2, 100) == "pay_per_trip"
