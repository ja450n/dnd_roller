let listDiceSides = [4, 6, 8, 10, 12, 20]
let currIdxValue = 0
let dicePipMaxValue = 4
let currDiceValue = 0
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    basic.showNumber(currDiceValue)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    
    if (currIdxValue > 0) {
        currIdxValue -= 1
    } else {
        currIdxValue = 5
    }
    
    dicePipMaxValue = listDiceSides[currIdxValue]
    basic.showNumber(dicePipMaxValue)
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    
    if (currIdxValue < 5) {
        currIdxValue += 1
    } else {
        currIdxValue = 0
    }
    
    dicePipMaxValue = listDiceSides[currIdxValue]
    basic.showNumber(dicePipMaxValue)
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    if (dicePipMaxValue == 10) {
        currDiceValue = randint(1, dicePipMaxValue) * 10
    } else {
        currDiceValue = randint(1, dicePipMaxValue)
    }
    
    basic.showNumber(currDiceValue)
})
