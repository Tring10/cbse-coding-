function charging () {
    for (let index = 0; index < 1; index++) {
        basic.showLeds(`
            . . . . .
            # # # # .
            # # . . #
            # # # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # # # . #
            # # # # .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # # # # .
            # # # # #
            # # # # .
            . . . . .
            `)
    }
}
let distance = 0
basic.showString("Hello!")
let thresh = 0
basic.forever(function () {
    distance = pins.digitalReadPin(DigitalPin.P1)
    if (distance == 1) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.showLeds(`
            . . . . .
            # # # # .
            # . . . #
            # # # # .
            . . . . .
            `)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1, 4566, 255, 0, 1500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        basic.pause(1000)
        charging()
    } else if (distance == 0) {
        basic.showIcon(IconNames.Happy)
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
})
