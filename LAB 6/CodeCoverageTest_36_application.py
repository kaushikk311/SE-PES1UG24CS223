
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# Test 1: Invalid axle count
def test_invalid_axle_count():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


# Test 2: Base toll for 2 axles
def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


# Test 3: Base toll for 3 axles
def test_three_axle_base_toll():
    assert toll_for(3, False, False) == 150


# Test 4: Base toll for 4 axles
def test_four_axle_base_toll():
    assert toll_for(4, False, False) == 250


# Test 5: Axle count not present in BASE_TOLL
def test_other_axle_count():
    assert toll_for(5, False, False) == 400


# Test 6: Peak hour charge
def test_peak_hour_charge():
    assert toll_for(2, True, False) == 125


# Test 7: FASTag discount for 2 axles
def test_fastag_two_axles():
    assert toll_for(2, False, True) == 90


# Test 8: FASTag discount for more than 2 axles
def test_fastag_other_axles():
    assert toll_for(3, False, True) == 142.5


# Test 9: Peak hour with FASTag
def test_peak_with_fastag():
    assert toll_for(2, True, True) == 112.5


# Test 10: Ambulance exemption
def test_ambulance_exemption():
    assert toll_charge("ambulance", 2, False, False) == 0


# Test 11: Fire engine exemption
def test_fire_engine_exemption():
    assert toll_charge("fire_engine", 3, False, False) == 0


# Test 12: Normal vehicle toll charge
def test_normal_vehicle_charge():
    assert toll_charge("car", 2, False, False) == 100


# Test 13: Buy pass when total cost is greater
def test_buy_pass():
    assert pass_advice([(False, False)], 2, 90) == "buy_pass"


# Test 14: Either option when costs are equal
def test_either_option():
    assert pass_advice([(False, False)], 2, 100) == "either"


# Test 15: Pay per trip when pass is more expensive
def test_pay_per_trip():
    assert pass_advice([(False, False)], 2, 150) == "pay_per_trip"


# Test 16: Multiple trips
def test_multiple_trips():
    trips = [(False, False), (True, False)]
    assert pass_advice(trips, 2, 200) == "buy_pass"
