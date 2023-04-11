

def charge(dist: number):
    while dist <= 3:
        basic.show_leds("""
            . . . . .
                        # # # # .
                        # . . . #
                        # # # # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # # # # .
                        # # . . #
                        # # # # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # # # # .
                        # # # . #
                        # # # # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # # # # .
                        # # # # #
                        # # # # .
                        . . . . .
        """)
        if distance > 3:
            basic.show_icon(IconNames.YES)
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    5000,
                    1,
                    255,
                    0,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                SoundExpressionPlayMode.UNTIL_DONE)
distance = 0
basic.show_string("Hello!")

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P2, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance <= 3:
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.show_leds("""
            . . . . .
                        # # # # .
                        # . . . #
                        # # # # .
                        . . . . .
        """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                1,
                4566,
                255,
                0,
                1500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.pause(1000)
        charge(distance)
    else:
        basic.show_icon(IconNames.HAPPY)
        pins.digital_write_pin(DigitalPin.P0, 1)
basic.forever(on_forever)
