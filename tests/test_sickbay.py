import pytest

from sickbay import (
    average_temperature,
    fever_patients,
    find_patient,
    greet,
    has_fever,
    pick_random,
    to_celsius,
    ward_report,
)


@pytest.mark.parametrize(
    "value, unit, expected",
    [
        (38.5, "C", 38.5),
        (101.3, "F", 38.5),
        (311.65, "K", 38.5),
    ],
)
def test_to_celsius(value, unit, expected):
    assert to_celsius(value, unit) == pytest.approx(expected)


def test_to_celsius_unknown_unit():
    with pytest.raises(ValueError):
        to_celsius(100, "X")


def test_has_fever():
    assert has_fever(38.5) is False
    assert has_fever(37.0) is False
    assert has_fever(38.0) is True


def test_fever_patients():
    patients = {
        "Captain Vega": 37.1,
        "Lt. Byte": 38.6,
        "Cmdr. Nova": 36.8,
        "Ensign Pixel": 39.2,
    }
    assert fever_patients(patients) == ["Ensign Pixel", "Lt. Byte"]


def test_fever_patients_empty():
    assert fever_patients({}) == []


def test_find_patient():
    patients = {"Captain Vega": 37.1, "Lt. Byte": 38.6}
    assert find_patient("byte", patients) == "Lt. Byte"
    assert find_patient("CAPTAIN", patients) == "Captain Vega"
    assert find_patient("unknown", patients) is None


def test_average_temperature():
    assert average_temperature([36.0, 38.0]) == 37.0
    assert average_temperature([]) == "n/a"


def test_pick_random():
    items = ["Apple", "Banana", "Kiwi"]
    assert pick_random(items) in items


def test_pick_random_empty():
    with pytest.raises(IndexError):
        pick_random([])


def test_greet():
    patients = {"Lt. Byte": 38.6}
    assert greet("byte", patients) == ("Quack, LT. BYTE! Dr. Honk will see you now.")


def test_greet_unknown_patient():
    with pytest.raises(AttributeError):
        greet("unknown", {})


def test_ward_report():
    patients = {
        "Captain Vega": 37.1,
        "Lt. Byte": 38.6,
        "Cmdr. Nova": 36.8,
        "Ensign Pixel": 39.2,
    }
    assert ward_report(patients) == (
        "Patients: 4\n"
        "Average temperature: 37.9 °C\n"
        "  FEVER: Ensign Pixel\n"
        "  FEVER: Lt. Byte"
    )
