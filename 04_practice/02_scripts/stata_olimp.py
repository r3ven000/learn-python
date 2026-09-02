balls = [85, 90, 78, 92, 60, 88]
normal_ball = 0
average_ball = 0

for ball in balls:
    normal_ball += ball / len(balls)

for ball in balls:
    if ball > normal_ball:
        average_ball += 1


print(
    f"Max: {max(balls)}, Min: {min(balls)}, Normal: {normal_ball}, Above average: {average_ball} "
)
