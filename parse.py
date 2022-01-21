import sys

def parse_cron() -> None:
    
    try:    
        arguments = sys.argv[1].split()
        command_format = '<minute> <hour> <day of month> <month> <day of week> <command>'
        if len(arguments) != 6:
            print(f"Invalid command. There should be 6 arguments, following the pattern: {command_format}")
            return
        
        result = {
            'minutes' : get_minutes(arguments[0])
        }

    except IndexError:
        print(f"Invalid command. The command should be ran with a string of arguments.")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return

def get_minutes(minute_string: str) -> str:
    
    if '*/' in minute_string:
        minute_string = minute_string.replace('*/', '')
        minutes_list = [str(i) for i in range(0, 60, int(minute_string))]
        return ' '.join(minutes_list)
    return minute_string

if __name__ == '__main__':
    parse_cron()