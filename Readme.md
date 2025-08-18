# Gaslighting and manipulating leds
git int :P

todo:
- write up on how daisy chained max7219 work with 8x8 led matrices

- using in major col order, where each row represents on off light in 8 bit 0b00001111, where 1 is on 0 is off (ofc haha)

- x value can be int divided by 8 to get strip no.

- y value can be int divided by 8 to get which matrix to write.

- data can only be latched when CS pin is on rising edge, so to write to any n matrix in ith strip, feed data till nth matrix and latch it, rest of the data is ignored in other matrices

wat is this todo i lit explained it all