import sys

def parse_cron() -> None:
    
    try:    
        arguments = sys.argv[1].split()
        command_format = '<minute> <hour> <day of month> <month> <day of week> <command>'
        if len(arguments) != 6:
            print(f"Invalid command. There should be 6 arguments, following the pattern: {command_format}")
            return
        
        result = {
            'minutes' : get_frequency(arguments[0], 'minutes'),
            'hour': get_frequency(arguments[1], 'hour')
        }
        print(result)

    except IndexError:
        print(f"Invalid command. The command should be ran with a string of arguments.")
        return
    except Exception as e:
        print(f"Something went wrong: {e}")
        return

def get_frequency(freq: str, type: str) -> str:
    
    if '*/' in freq:
        freq = freq.replace('*/', '')
        stop = 60 if type == 'minutes' else 24
        freq_list = [str(i) for i in range(0, stop, int(freq))]
        return ' '.join(freq_list)
    return freq


if __name__ == '__main__':
    parse_cron()