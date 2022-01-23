import unittest
from unittest.mock import MagicMock

from services.formatter import Formatter
from services.calendar import Calendar
from services.parser import Parser

calendar = Calendar()
formatter = Formatter(14)
parser = Parser(calendar, formatter)

def test_get_minutes_frequency_with_star():
   
    result = parser.get_frequency('*', 'minutes')
    expected = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59'
    assert result == expected

def test_get_minutes_frequency_with_star_pattern():
   
    result = parser.get_frequency('*/15', 'minutes')
    expected = '0 15 30 45'
    assert result == expected

def test_get_hour_frequency_with_star():
   
    result = parser.get_frequency('*', 'hour')
    expected = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23'
    assert result == expected

def test_get_hour_frequency_with_star_pattern():
   
    result = parser.get_frequency('*/5', 'hour')
    expected = '0 5 10 15 20'
    assert result == expected

def test_get_frequency_with_single_value():

    result = parser.get_frequency('15', 'hour')
    expected = '15'
    assert result == expected

def test_get_day_in_month_with_star():

    calendar.get_days_in_month = MagicMock(return_value=10)
    result = parser.get_day('*', 'month')
    expected = '1 2 3 4 5 6 7 8 9 10'
    assert result == expected

def test_get_day_in_month_with_special_cases():

    calendar.get_days_in_month = MagicMock(return_value=10)
    parser.get_special_cases = MagicMock(return_value='it does not matter what it returns here')
    result = parser.get_day('1,5', 'month')
    expected = 'it does not matter what it returns here'
    assert result == expected

def test_get_day_in_week_with_star():

    result = parser.get_day('*', 'week')
    expected = '1 2 3 4 5 6 7'
    assert result == expected

def test_get_day_in_week_with_special_cases():

    parser.get_special_cases = MagicMock(return_value='it does not matter what it returns here')
    result = parser.get_day('1,5', 'week')
    expected = 'it does not matter what it returns here'
    assert result == expected

def test_get_day_with_single_value():

    result = parser.get_day('5', 'month')
    expected = '5'
    assert result == expected

def test_get_month_with_star():

    result = parser.get_month('*')
    expected = '1 2 3 4 5 6 7 8 9 10 11 12'
    assert result == expected

def test_get_month_with_special_cases():

    parser.get_special_cases = MagicMock(return_value='it does not matter what it returns here')
    result = parser.get_month('1,4')
    expected = 'it does not matter what it returns here'
    assert result == expected

def test_get_month_with_single_value():

    result = parser.get_month('3')
    expected = '3'
    assert result == expected

