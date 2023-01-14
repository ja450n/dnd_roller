listDiceSides = [4, 6, 8, 10, 12, 20]
currIdxValue = 0
dicePipMaxValue = 4
currDiceValue = 0;

def on_button_pressed_ab():
    global currDiceValue
    basic.show_number(currDiceValue)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_a():
    global currIdxValue
    global dicePipMaxValue

    if currIdxValue > 0:
        currIdxValue -= 1
    else:
        currIdxValue = 5
    dicePipMaxValue = listDiceSides[currIdxValue]
    basic.show_number(dicePipMaxValue)
    pass    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global currIdxValue
    global dicePipMaxValue

    if currIdxValue < 5:
        currIdxValue += 1
    else:
        currIdxValue = 0
    dicePipMaxValue = listDiceSides[currIdxValue]
    basic.show_number(dicePipMaxValue)
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global currDiceValue

    if dicePipMaxValue == 10:
        currDiceValue = randint(1, dicePipMaxValue) * 10
    else:
        currDiceValue = randint(1, dicePipMaxValue)
    basic.show_number(currDiceValue)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
