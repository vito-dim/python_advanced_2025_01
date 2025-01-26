# def rectangle(length: int, width: int) -> str:
#     if not isinstance(length, int) or not isinstance(width, int):
#         return 'Enter valid values!'
#
#     def area():
#         calculated_area = length * width
#         return calculated_area
#
#     def perimeter():
#         calculated_perimeter = (2 * length) + (2 * width)
#         return calculated_perimeter
#
#     return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

def rectangle(length: int, width: int) -> str:
    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'

    def area():
        return length * width

    def perimeter():
        return (2 * length) + (2 * width)

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

print(rectangle(2, 10))
print(rectangle('2', 10))
