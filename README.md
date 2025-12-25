# Splittyboi
A Split keyboard with low profile switches,Coded with KMK Firmware.

Note: Couldn't get the render with all the parts together because my laptop kept crashing trying to load in all the parts in the same file. [ It has 4 gigs of RAM so please forgive it :) ]

# Schematic
This is the schematic for a single side, both sides are made identically.
<img width="979" height="522" alt="Screenshot 2025-12-12 141900" src="https://github.com/user-attachments/assets/5943f881-8383-4003-9961-4293534d74a1" />

# Layout
The layout was designed on https://www.keyboard-layout-editor.com/, The firmware hasn't yet been edited to match this layout and is currently sitting with placeholders.
<img width="852" height="358" alt="Screenshot 2025-12-08 145546" src="https://github.com/user-attachments/assets/a2b045e3-95ad-4469-b070-cdb056cac2ad" />


# PCB
The PCB was designed in Kicad. The matrix wasn't properly aligned to make the look of the PCB More intresting, it will be coded in properly afterwards.
<img width="1172" height="516" alt="Screenshot 2025-12-10 205500" src="https://github.com/user-attachments/assets/8e9e1b33-0806-4f8d-a38c-48ddb7c8c56d" />
<img width="1051" height="426" alt="Screenshot 2025-12-10 205553" src="https://github.com/user-attachments/assets/3a9efc3f-3d46-40cc-9621-6be8b1f2a20e" />

# Case
The case was designed in Fusion. Both sides of the case are based on the same footprint but once it is extruded in the positive axis and once in negetive axis to get a identical case accommodating both right and left sides.
<img width="526" height="381" alt="Screenshot 2025-12-12 134242" src="https://github.com/user-attachments/assets/6332d1f6-68be-4e72-b4e0-ffecc0fdff05" />
<img width="394" height="342" alt="Screenshot 2025-12-12 134156" src="https://github.com/user-attachments/assets/ac4336d5-e7d8-487a-9085-ac678daa6939" />

# Firmware
As mentioned above, the firmware is written in python using the KMK Libraries. It will be pushed to the microcontroller using circuit python.

# BOM

<img width="1333" height="221" alt="image" src="https://github.com/user-attachments/assets/992f687e-2d59-4528-9255-3a046401ac76" />
The Links:

Seeed XIAO nRF52840 : https://robocraze.com/products/seeed-studio-xiao-nrf52840-development-board-supports-bluetooth-5-0

Gateron LP 2.0 Switches : https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-low-profile-2-0-mechanical-switch-3pin/

Blank DSA Keycaps 1U : https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/

3.7V LiPo Batteries : https://quartzcomponents.com/products/3-7v-1000mah-li-po-rechargeable-battery

1N4148WS T4 Switching Diode : https://quartzcomponents.com/collections/smd-diodes/products/1n4148ws-t4-switching-diode-sod-123-smd-package

For the reviewer:
The shipping option i chose on JLCPCB:

<img width="758" height="595" alt="Screenshot_20251225-093345 (1)" src="https://github.com/user-attachments/assets/a40b42da-5cef-4b60-a4c6-2e08ec84051b" />

