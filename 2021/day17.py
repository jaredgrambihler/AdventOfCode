# this is very broken

with open("2021/input/day17input.txt") as f:
    input_text = f.read().strip()

input_text = "target area: x=20..30, y=-10..-5"

x, y = input_text.split(":")[1].split(",")
min_x, max_x = x.split("=")[1].split("..")
min_x = int(min_x)
max_x = int(max_x)
min_y, max_y = y.split("=")[1].split("..")
min_y = int(min_y)
max_y = int(max_y)


def hits_target(x_velocity, y_velocity) -> bool:
    x = 0
    y = 0
    while True:
        x += x_velocity
        y += y_velocity
        if x_velocity != 0:
            x_velocity -= (x_velocity / abs(x_velocity))
        y_velocity -= 1
        # check if we're in the target
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            return True
        # check if we overshot
        if y < min_y or (x > max_x and x_velocity > 0) or (x < min_x and x_velocity < 0):
            break
    return False


def get_max_height(mix_x, max_x, min_y, max_y):
    # total x distance is  initial_x_vel + initial_x_vel - 1 + ... + 1, then it never changes
    # so if we get the x pos to the desired range is the given number of steps, we can give a range of x velocities that will always hit
    # y distance is initial_y_vel + (initial_y_vel - 1) + (initial_y_vel - 2) + ...
    # another way to view this sum at step is n is (initial_y_vel * n) + (-1 + -2 + -3... + - (n -1)) = (intial_y_vel * n) - (1 + 2 + 3 + ... + n - 1)
    # so at step n, y_pos = initial_y_vel * n - (n -1) * n / 2

    # we can control the x to land in the target no matter what, and finding the highest arc would involve and x_vel of 0 at the end
    # we need the y velocity to be as high as possible, but the velocity when it hits the target again can't overshoot it
    # we can guarantee this by making sure that abs(y_vel) <= length_of_target when it lands in it
    # we can work back from this ending speed to how many steps down we have and therefore the arcs peak
    max_ending_y_vel = abs(min_y - max_y)
    # length down to the target is 1 + 2 + 3 + ... + max_ending_y_vel
    vert_distance_from_end = max_ending_y_vel * (max_ending_y_vel + 1) / 2
    min_peak = vert_distance_from_end + min_y
    max_peak = vert_distance_from_end + max_y
    # find a starting velocity that gets us b / w min and max peaks
    max_height = 0
    cur_vel = 1
    while max_height < max_peak:
        cur_max_height = cur_vel * (cur_vel + 1) / 2
        if cur_max_height > max_peak:
            break
        max_height = max(cur_max_height, max_height)
        cur_vel += 1
    return max_height


print("Part 1")
print(f"Max height: {get_max_height(0, 30, -10, -5)}")
print(f"Max height: {get_max_height(min_x, max_x, min_y, max_y)}")
