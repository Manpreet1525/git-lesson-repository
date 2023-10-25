diamond_height = 6

# for i in range(2 * diamond_height):
#     if i < diamond_height:  # Top half of the diamonds
#         spaces_before = diamond_height - i
#         stars = i
#     else:  # Bottom half of the diamonds
#         spaces_before = i - diamond_height
#         stars = 2 * diamond_height - i

#     # Constructing one complete line
#     line = " " * spaces_before + "* " * stars
#     line += " " * (2 * spaces_before) + "* " * stars
#     line += " " * (2 * spaces_before) + "* " * stars

#     print(line)