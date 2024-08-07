def check_color_exists(color, color_tuple):
    for sub_color_tuple in color_tuple:
        if color in sub_color_tuple:
            return True
    return False

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)

user_color = input("Enter a color : ")

if check_color_exists(user_color, colors):
    print(f"{user_color} exists in the tuple.")
else:
    print(f"{user_color} does not exist in the tuple.")
