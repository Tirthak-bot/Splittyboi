import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC, Key
from kmk.modules.split import Split, SplitType, SplitSide

# Pretty sure that left side is the master side.
# Need to add more libreries for adding diffrent functions and also obviously remap the keys.
# Note:  Matrix in my keyboard isn't perfectly alligned so some keys may not work as expected and the key mapping may need to be adjusted accordingly.

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D8, board.D9, board.D10)


keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_type=SplitType.BLE,
    split_side=SplitSide.LEFT
)
keyboard.modules.append(split)

keyboard.keymap = [ KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,KC.N6,
                    KC.N7, KC.N8, KC.N9, KC.A, KC.B, KC.C,
                    KC.D, KC.E, KC.F, KC.G, KC.H, KC.I,
                    KC.J, KC.K, KC.L, KC.M, KC.N, KC.O,
                    KC.P, KC.Q, KC.R, KC.S, KC.T, KC.U,
]

if __name__ == '__main__':
    keyboard.go()


