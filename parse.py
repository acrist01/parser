import sys

def parse_cron():
    
    try:    
        arguments = sys.argv[1].split()
        command_format = '<minute> <hour> <day of month> <month> <day of week> <command>'
        if len(arguments) != 6:
            print(f"Invalid command. There should be 6 arguments, following the pattern: {command_format}")
            return
    except IndexError:
        print(f"Invalid command. The command should be ran with a string of arguments.")
        return
    except Exception:
        print('Something went wrong!')
        return

if __name__ == '__main__':
    parse_cron()