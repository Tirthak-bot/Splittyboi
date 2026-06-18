# Splittyboi
A Split keyboard with low profile switches, Coded with KMK Firmware.

<img width="286.0" height="400.0" alt="Split keeb Zine Page" src="https://github.com/user-attachments/assets/d236c32e-1033-4947-9b12-0187164524aa" />
<img width="476.855" height="400" alt="Untitled design (1)" src="https://github.com/user-attachments/assets/e0057221-b03b-4537-b2a0-e4b139ad9b9c" />


Making this because i want to try a split keeb :3

Using this is pretty straight forward obviously blehh, just connect it to the computer, flash the firmware once and it should just work like a regular keeb moving forward :)





# Schematic
This is the schematic for a single side, both sides are made identically.

<img width="750.2" height="400" alt="Screenshot 2025-12-12 141900" src="https://github.com/user-attachments/assets/5943f881-8383-4003-9961-4293534d74a1" />

# Layout
The layout was designed on https://www.keyboard-layout-editor.com/, The firmware hasn't yet been edited to match this layout and is currently sitting with placeholders.

<img width="852" height="358" alt="Screenshot 2025-12-08 145546" src="https://github.com/user-attachments/assets/a2b045e3-95ad-4469-b070-cdb056cac2ad" />


# PCB
The PCB was designed in Kicad. The matrix wasn't properly aligned to make the look of the PCB More intresting, it will be coded in properly afterwards (Once I make it IRL).

<img width="908.52" height="400" alt="Screenshot 2025-12-10 205500" src="https://github.com/user-attachments/assets/8e9e1b33-0806-4f8d-a38c-48ddb7c8c56d" />
<img width="986.85" height="400" alt="Screenshot 2025-12-10 205553" src="https://github.com/user-attachments/assets/3a9efc3f-3d46-40cc-9621-6be8b1f2a20e" />

# Case
The case was designed in Fusion. Both sides of the case are based on the same footprint but once it is extruded in the positive axis and once in negetive axis to get a identical case accommodating both right and left sides.

You just drop the pcb in place :) and for the both halfs of the case, they join using magnets!

The magnets are glue and drop, not press fit! So the thin walls around the magnet holes won't cause any problems!


<img width="1366" height="573" alt="Split_keeb_final_assembly_2026-Jun-13_07-47-10AM-000_CustomizedView16534653009" src="https://github.com/user-attachments/assets/f26ff9a4-9aaa-48ad-89bb-86868efa6049" />

# Firmware
As mentioned above, the firmware is written in python using the KMK Libraries. It will be pushed to the microcontroller using circuit python.

# BOM
|SR.NO|ITEMS|QUANTITY|UNIT PRICE|TOTAL PRICE|URL|
|-----|-----|--------|-----------|-----------|---|
|1|PCB (From JLCPCB)|5 (Minimun)|$10 (Including Shipping)|$50|In my Cart|
|2|Seeed XIAO nRF52840|2 (One for each side)|$12.50 (Including Shipping)|$25|https://robocraze.com/products/seeed-studio-xiao-nrf52840-development-board-supports-bluetooth-5-0|
|3|Gateron LP 2.0 Switches|70|$0.185 (Including Shipping)|$13|https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-low-profile-2-0-mechanical-switch-3pin/|
|4|Blank DSA Keycaps 1U|70|$0.207 (Including Shipping)|$14.5|https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/|
|5|3.7V LiPo Batteries|2 (One for each side)|$1.615 (Including Shipping)|$3.23|https://quartzcomponents.com/products/3-7v-1000mah-li-po-rechargeable-battery|
|6|1N4148WS T4 Switching Diode|70|$0.025 (Including Shipping)|$1.78|https://quartzcomponents.com/collections/smd-diodes/products/1n4148ws-t4-switching-diode-sod-123-smd-package|
|7|3D Prints|4 Files|idk|idk|Self printed|
|8|Magnets|14|$0|$0|Self sourced|
|Total:|||-|$110||
