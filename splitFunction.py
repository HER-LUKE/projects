def split_line(segment, position):
    part1 = segment[:position]
    part2 = segment[position:]
    return part1, part2
segment = "This is an example string that can be split using this function"
position = 15

part1, part2 = split_line(segment, position)
print("Part 1: " + part1)
print("Part 2: " + part2)
