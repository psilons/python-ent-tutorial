import pandas


# this class is to cache date parsing because pandas parsing is very slow
class CachedDateParser:
    def __init__(self, date_format):
        self._date_format = date_format
        self._cache = {}  # str -> date

    def parse(self, date_str: str):
        if date_str in self._cache:
            return self._cache[date_str]

        # no need to cache this, no gain
        # dt = datetime.datetime.strptime(date_str, self._date_format)

        dt = pandas.to_datetime(date_str, format=self._date_format)  # very slow

        # dt = pandas.to_datetime(date_str, format=self._date_format,
        #                         infer_datetime_format=True)
        self._cache[date_str] = dt

        return dt
