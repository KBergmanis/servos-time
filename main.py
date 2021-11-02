def on_button_pressed_a():
    servos.P1.set_angle(0)
    basic.show_number(0)
    basic.pause(500)
    servos.P1.set_angle(90)
    basic.show_number(90)
    basic.pause(500)
    servos.P1.set_angle(180)
    basic.show_number(180)
    basic.pause(500)
    servos.P1.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P1.set_angle(180)
    basic.show_number(180)
    basic.pause(500)
    servos.P1.set_angle(90)
    basic.show_number(90)
    basic.pause(500)
    servos.P1.set_angle(0)
    basic.show_number(0)
    basic.pause(500)
    servos.P1.stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("SERVO TIME", 65)
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")