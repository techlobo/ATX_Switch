# DIY PiKVM v2 (single ATX) Section



<p align="center">
<img src=".\Images\DIY_PiKVM_v2_attr1_subject_attr1.png" alt="DIY PiKVM v2 3D printed case" width="500"/>
</p>

The *DIY PiKVM v2* consists of:

## Hardware

- [3D printed case](./Case/README.md)
- Pi4 (suitable for PiKVM)
- [Power splitter](https://www.tindie.com/products/8086net/usb-cpwr-splitter/) from 8086.com
  - Barrel jack version not required, although will fit.

- [Angled USB-C cable](https://www.startech.com/en-gb/cables/r2ccr-15c-usb-cable) connecting Power splitter to Pi4 USC-C power supply port
  - Other cables / adaptors can potentially be used but I found this item to be best for the available space / bend.

- [C790](https://geekworm.com/products/c790) to provide HDMI-CSI2 video capture 
  - FPC 15-pin cable should also be supplied 
  - (audio if required using supplied I2S cable)

- [ATX connector](./ATX_connector_board_for_Pi/README.md) (RJ45 configured as per standard PiKVM ATX socket)
- [0.91 inch OLED screen](https://www.aliexpress.com/item/1005005281308478.html) (typically white / yellow / blue)
  - 4-pin female-to-female dupont ribbon cable

- 4x 2mm silicone cushion mat self adhesive rubber feet
- **Optional** - 40x40x10 fan (preferably PWM). Few types tested:
  - [Noctua NF-A4x10 5V PWM](https://noctua.at/en/nf-a4x10-pwm)
  - [Pi5 PWM fan](https://thepihut.com/products/4010-cooler-black-fan-for-raspberry-pi-5?variant=42684803907779)
  - [GeeekPi PWM fan](https://www.amazon.co.uk/GeeekPi-Raspberry-Adjustable-40x40x10mm-Radiator/dp/B092ZF995F?th=1)
  - There are others, but not tested.


The case construction allows for mainly tool-less assembly, however the following bolts / connectors **are** used in the build of the unit:

- 2x M3 35mm bolts for connecting the front and back of the case together.
  - I used [black hex socket head bolts](https://www.aliexpress.com/item/1005005832717344.html) (to match in with the black PLA) together with [M3(OD4.5) 6mm heat inserts](https://www.aliexpress.com/item/1005006042691803.html) in the case back to provide a good fit that can be opened / closed easily. The use of heat inserts is not compulsory but the inner diameter of the mounting hole on the back case will probably need to be adjusted if M3 screws (or bolts) are to be used on their own.
- 4x M3 15mm bolts / nuts to fasten the fan into place
  - I used [black D4(M3) screw book binding post screws](https://www.aliexpress.com/item/32789781458.html) together with rubber washers to provide a good looking finish with the Noctua NF-A4x10 5V PWM fan.
- **Optional** - depending on preference, an M2.5 brass standoff spacer (18mm) can be used in conjunction with 2x M2.5 6mm low flat screws to fasten the ATX Switch connector board to the Raspberry Pi4. This is not essential as the case construction will hold the components together, but may provide rigidity during assembly.



Hardware assembly and software is basically the same as for [DIY_PiKVM](../DIY_PiKVM/README.md), although the ATX Switch scripts are not required if only using this as a 1:1 v2 ipKVM device. The ATX Switch scripts do need to be installed if intending to use this device in conjunction with the [ATX Switch Interface adaptor](../ATX_Switch_Interface_adaptor/README.md) (see relevant installation notes).

