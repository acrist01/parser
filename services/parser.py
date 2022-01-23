class Parser(object):

    def __init__(self, calendar, formatter):
        self._calendar = calendar
        self._formatter = formatter
        self._special_cases = [',', '-']
    
    def parse(self, arguments: list) -> dict:

        result = {
            'minutes' : self.get_frequency(arguments[0], 'minutes'),
            'hour': self.get_frequency(arguments[1], 'hour'),
            'day of month': self.get_day(arguments[2], 'month'),
            'month': self.get_month(arguments[3]),
            'day of week': self.get_day(arguments[4], 'week'),
            'command': arguments[5]
        }

        return self._formatter.format(result)

    def get_frequency(self, frequency: str, type: str) -> str:

        stop = 60 if type == 'minutes' else 24
        if '*' == frequency:
            frequency_list = [str(i) for i in range(0, stop)]
            return ' '.join(frequency_list)

        if '*/' in frequency:
            frequency = frequency.replace('*/', '')
            frequency_list = [str(i) for i in range(0, stop, int(frequency))]
            return ' '.join(frequency_list)

        return frequency

    def get_day(self, frequency: str, type: str) -> str:
        
        stop = 7 if type == 'week' else self._calendar.get_days_in_month()
        if '*' == frequency:
            frequency_list = [str(i) for i in range(1, stop + 1)]
            return ' '.join(frequency_list)
        if any(case in frequency for case in self._special_cases):
            return self.get_special_cases(frequency)
        
        return frequency
    
    def get_month(self, frequency: str) -> str:
        if '*' == frequency:
            frequency_list = [str(i) for i in range(1, 13)]
            return ' '.join(frequency_list)

        if any(case in frequency for case in self._special_cases):
            return self.get_special_cases(frequency)

        return frequency
    
    def get_special_cases(self, frequency: str):
        if ',' in frequency:
            return ' '.join(frequency.split(','))
        
        if '-' in frequency:
            frequency_list = frequency.split('-')
            frequency_list = [str(i) for i in range(int(frequency_list[0]), int(frequency_list[1]) + 1)]
            return ' '.join(frequency_list)