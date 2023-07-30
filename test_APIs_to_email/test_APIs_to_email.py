#for running tests used "python3 -m pytest test_APIs_to_email.py", 
#in my environment running "pytest" was not recognized (it's installed)
import pytest
from APIs_to_email import valid_email, command_line_input, API_validation

def test_command_line_input():
    argv = ["script.py", "example@gmail.com", "https://meowfacts.herokuapp.com/"]
    assert command_line_input(argv) == (
        "example@gmail.com",
        "https://meowfacts.herokuapp.com/",
    )
    argv = [
        "script.py",
        "test@gmail.com",
        "http://dog-api.kinduff.com//api/facts?number=1",
    ]
    assert command_line_input(argv) == (
        "test@gmail.com",
        "http://dog-api.kinduff.com//api/facts?number=1",
    )
    argv = ["script.py", "missing@gmail.com"]
    with pytest.raises(SystemExit) as excinfo:
        command_line_input(argv)
    assert "Missing command line arguments" in str(excinfo.value)


def test_valid_email():
    assert valid_email("example@gmail.com") == "example@gmail.com"
    assert valid_email("test123@gmail.com") == "test123@gmail.com"
    with pytest.raises(SystemExit) as excinfo:
        valid_email("email.com")
    assert "Provided email address is not valid" in str(excinfo.value)


def test_API_validation():
    cats_url = "https://meowfacts.herokuapp.com/"
    dogs_url = "http://dog-api.kinduff.com//api/facts?number=1"
    assert API_validation(cats_url, cats_url, dogs_url) == (cats_url, "cats")
    assert API_validation("API_cats", cats_url, dogs_url) == (cats_url, "cats")
    assert API_validation(dogs_url, cats_url, dogs_url) == (dogs_url, "dogs")
    assert API_validation("API_dogs", cats_url, dogs_url) == (dogs_url, "dogs")
    with pytest.raises(SystemExit) as excinfo:
        API_validation("http://unexpected.api.adress.com", cats_url, dogs_url)
    assert "Provided API is unrecognized" in str(excinfo.value)
