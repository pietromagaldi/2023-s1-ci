import pytest

from .exceptions import (
    MinimumLengthException,
    NoDigitException,
    NoLowerCaseException,
    EspecialCharacterException,
    NoUpperCaseException,
    ProhibitedCharacterException
)
from .models import PasswordValidator, ValidationResponse


def test_empty_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="")
    with pytest.raises(MinimumLengthException):  # then
        # when
        validator.password_validate()


def test_7_chars_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="1@Ab1@A")
    with pytest.raises(MinimumLengthException):  # then
        # when
        validator.password_validate()


def test_8_chars_password_should_validate():
    # given
    expected_response = ValidationResponse(message="OK")
    # when
    actual_response = PasswordValidator(content="1@Ab1@Ab").password_validate()
    # then
    assert expected_response == actual_response


def test_9_chars_password_should_validate():
    # given
    expected_response = ValidationResponse(message="OK")
    # when
    actual_response = PasswordValidator(content="1@Ab1@Ab1").password_validate()
    # then
    assert expected_response == actual_response


def test_8_chars_with_no_digit_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="C@Abc@Ab")
    with pytest.raises(NoDigitException):  # then
        # when
        validator.password_validate()


def test_8_chars_with_no_lower_case_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="1@AB1@AB")
    with pytest.raises(NoLowerCaseException):  # then
        # when
        validator.password_validate()


def test_8_chars_with_no_especial_character_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="1eAB1eAB")
    with pytest.raises(EspecialCharacterException):  # then
        # when
        validator.password_validate()


def test_8_chars_with_no_upper_case_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="c@abc@a1")
    with pytest.raises(NoUpperCaseException):  # then
        # when
        validator.password_validate()

def test_8_chars_with_prohibited_character_password_should_raise_exception():
    # given
    validator = PasswordValidator(content="1@a^1@A!")
    with pytest.raises(ProhibitedCharacterException):  # then
        # when
        validator.password_validate()
