class KData:
    LIMIT_UP = 1
    LIMIT_DOWN = 0

    STEP_DEFAULT = 0.1

    @staticmethod
    def round(value):
        return round(value, 2)


class Data:
    def __init__(self, year: int, data: list[float]):
        self.year = year,
        self.data = data
        