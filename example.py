from geometry_shapes import Circle, Triangle, calculate_area, is_right_angle

def main():
    # Пример использования для круга
    circle = Circle(5)
    circle_area = calculate_area(circle)
    print("Площадь круга:", circle_area)  # 78.53981633974483
    circle_right_angle = is_right_angle(circle)
    print("Является ли круг прямоугольным треугольником:", circle_right_angle)  # False

    # Пример использования для треугольника
    triangle = Triangle(3, 4, 5)
    triangle_area = calculate_area(triangle)
    print("Площадь треугольника:", triangle_area)  # 6.0
    triangle_right_angle = is_right_angle(triangle)
    print("Является ли треугольник прямоугольным:", triangle_right_angle)  # True

if __name__ == "__main__":
    main()
