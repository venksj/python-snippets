from gasp import *

begin_graphics(800, 800, title="Catch", background=color.YELLOW)
set_speed(120)

ball_x = 20
ball_y = 300
ball = Circle((ball_x, ball_y), 10, filled=True)

dx = 10
dy = random_between(-2, 4)

mitt_x = 780
mitt_y = 300
mitt = Circle((mitt_x, mitt_y), 20)

while True:
    if ball_x < 700:
        ball_x += dx
        if (ball_y < 100 or ball_y > 700):
            dy *= dy
        ball_y += dy
        move_to(ball, (ball_x, ball_y))

    if key_pressed('k') and mitt_y <= 580:
        mitt_y += 5
    elif key_pressed('j') and mitt_y >= 20:
        mitt_y -= 5

    if key_pressed('escape'):
        break
    move_to(mitt, (mitt_x, mitt_y))

    #update_when('key_pressed')
    update_when('next_tick')


end_graphics()
