class Coordinate:
    def __init__(self, start_point, end_point, coord_y):
        self.start = start_point
        self.end = end_point
        self.y = coord_y

    def get_point_by_percent_on_segment(self, percent):
        flag_point_x = self.calculate_x(percent)
        return [flag_point_x, self.y, 0]

    def calculate_x(self, percent):
        part = percent / 100
        start_x = self.start[0]
        end_x = self.end[0]
        return start_x + ((end_x - start_x) * part)
