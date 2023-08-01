from datetime import date, datetime

import pytest
from pydantic import ValidationError

from metaboatrace.models.race import RaceInformation
from metaboatrace.models.stadium import StadiumTelCode


@pytest.mark.parametrize(
    "race_holding_date,stadium_tel_code,race_number,title,number_of_laps,deadline_at,is_course_fixed,use_stabilizer,expected",
    [
        # valid case
        (date.today(), StadiumTelCode.HEIWAJIMA, 1, "Race 1", 3, datetime.now(), True, False, True),
        # invalid cases
        (
            date.today(),
            StadiumTelCode.HEIWAJIMA,
            1,
            "Race 1",
            4,
            datetime.now(),
            True,
            False,
            False,
        ),  # invalid number_of_laps
    ],
)
def test_race_information(  # type: ignore
    race_holding_date,
    stadium_tel_code,
    race_number,
    title,
    number_of_laps,
    deadline_at,
    is_course_fixed,
    use_stabilizer,
    expected,
):
    data = {
        "race_holding_date": race_holding_date,
        "stadium_tel_code": stadium_tel_code,
        "race_number": race_number,
        "title": title,
        "number_of_laps": number_of_laps,
        "deadline_at": deadline_at,
        "is_course_fixed": is_course_fixed,
        "use_stabilizer": use_stabilizer,
    }
    if expected:
        race_information = RaceInformation(**data)
        assert race_information.race_holding_date == data["race_holding_date"]
        assert race_information.stadium_tel_code == data["stadium_tel_code"]
        assert race_information.race_number == data["race_number"]
        assert race_information.title == data["title"]
        assert race_information.number_of_laps == data["number_of_laps"]
        assert race_information.deadline_at == data["deadline_at"]
        assert race_information.is_course_fixed == data["is_course_fixed"]
        assert race_information.use_stabilizer == data["use_stabilizer"]
    else:
        with pytest.raises(ValidationError):
            race_information = RaceInformation(**data)
