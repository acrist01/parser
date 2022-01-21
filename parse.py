import sys

def parse_cron() -> None:
    
    try:    
        arguments = sys.argv[1].split()
        command_format = '<minute> <hour> <day of month> <month> <day of week> <command>'
        if len(arguments) != 6:
            print(f"Invalid command. There should be 6 arguments, following the pattern: {command_format}")
            return
        
        result = {
            'minutes' : get_minute_frequency(arguments[0]),
            'hour': get_hour_frequency(arguments[1])
        }

    except IndexError:
        print(f"Invalid command. The command should be ran with a string of arguments.")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return

def get_minute_frequency(minute_string: str) -> str:
    
    if '*/' in minute_string:
        minute_string = minute_string.replace('*/', '')
        minutes_list = [str(i) for i in range(0, 60, int(minute_string))]
        return ' '.join(minutes_list)
    return minute_string

def get_hour_frequency(hour_string: str) -> str:

    if '*/' in hour_string:
        hour_string = hour_string.replace('*/', '')
        hours_list = [str(i) for i in range(0, 24, int(hour_string))]
        return ' '.join(hours_list)
    return hour_string

if __name__ == '__main__':
    parse_cron()