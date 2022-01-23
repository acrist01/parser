from services.formatter import Formatter

formatter = Formatter(14)

def test_formatter():
    mocked_parsed_cron = {
        'minutes': '0 15 30 45',
        'hour': '10'
    }
    result = formatter.format(mocked_parsed_cron)
    expected = f"minutes{7*' '}0 15 30 45\nhour{10*' '}10\n"
    assert result == expected
