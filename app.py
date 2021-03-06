import sys

from services.calendar import Calendar
from services.parser import Parser
from services.formatter import Formatter

def parse_cron() -> None:
    
    try:    
        arguments = sys.argv[1].split()
        command_format = '<minute> <hour> <day of month> <month> <day of week> <command>'
        if len(arguments) != 6:
            print(f"Invalid command. There should be 6 arguments, following the pattern: {command_format}")
            return
        
        column_size = 14

        calendar = Calendar()
        formatter = Formatter(column_size)
        parser = Parser(calendar, formatter)
        result = parser.parse(arguments)
        print(result)

    except IndexError:
        print(f"Invalid command. The command should be ran with a string of arguments.")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return        


if __name__ == '__main__':
    parse_cron()