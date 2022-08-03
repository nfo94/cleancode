class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


class Rectangle:
    def __init__(self, origin, width, hight):
        self.origin = origin
        self.width = width
        self.hight = hight

    def get_area(self):
        return self.width * self.hight

    def print_coordinates(self):
        top_right = self.origin.coord_x + self.width
        bottom_left = self.origin.coord_y + self.hight
        print('Starting Point (X)): ' + str(self.origin.coord_x))
        print('Starting Point (Y)): ' + str(self.origin.coord_y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.get_area())
rectangle.print_coordinates()
