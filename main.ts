input.onButtonPressed(Button.A, function () {
    servos.P1.setAngle(0)
    basic.showNumber(0)
    basic.pause(500)
    servos.P1.setAngle(90)
    basic.showNumber(90)
    basic.pause(500)
    servos.P1.setAngle(180)
    basic.showNumber(180)
    basic.pause(500)
    servos.P1.stop()
})
input.onButtonPressed(Button.B, function () {
    servos.P1.setAngle(180)
    basic.showNumber(180)
    basic.pause(500)
    servos.P1.setAngle(90)
    basic.showNumber(90)
    basic.pause(500)
    servos.P1.setAngle(0)
    basic.showNumber(0)
    basic.pause(500)
    servos.P1.stop()
})
basic.showString("SERVO TIME", 65)
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
