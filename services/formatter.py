class Formatter(object):

    def __init__(self, column_size: int) -> None:
        self._column_size = column_size
    
    def format(self, parsed_cron: dict) -> str:
        formatted_result = ''
        for key, value in parsed_cron.items():
            formatted_result += f"{key}{(self._column_size-len(key))*' '}{value}\n"
        return formatted_result