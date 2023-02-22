class Coordinate:
    """
        A class to calculate coordinates.
        --Attributes
            start_point : list
                first point coordinate
            end_point : list
                second point coordinate
        --Methods
            get_point_by_percent_on_segment(percent)
                takes in percent
                :return coordinate of the percent on segment
            divide_segment_into_equal_parts(parts):
                takes in parts quantity, into which must be divided
                :return coordinate of the parts on segment
    """
    def __init__(self, start_point, end_point):
        self.start_point_x = start_point[0]
        self.end_point_x = end_point[0]
        self.point_y = start_point[1]

    def get_point_by_percent_on_segment(self, percent):
        part = percent / 100
        part_x = self.start_point_x + (self.__calculate_points_distance() * part)
        return self.__coordinate(part_x)

    def divide_segment_into_equal_parts(self, parts):
        part_length = self.__calculate_points_distance() / parts
        parts_coordinates = []
        for i in range(1, parts):
            part_x = self.start_point_x + part_length * i
            parts_coordinates.append(self.__coordinate(part_x))
        return parts_coordinates

    def __calculate_points_distance(self):
        return self.end_point_x - self.start_point_x

    def __coordinate(self, x):
        return [x, self.point_y, 0]
