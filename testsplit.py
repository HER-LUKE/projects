def split_line(segment, position):
    part1 = segment[:position]
    part2 = segment[position:]
    return part1, part2
segment = "1648226040.566446 IP NULL> NULL: Flags [P.], NULL], length 36"
position = 15

part1, part2 = split_line(segment, position)
print("Part 1: " + part1)
print("Part 2: " + part2)