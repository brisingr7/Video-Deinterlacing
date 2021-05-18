""" Full assembly of the parts to form the complete network """

import torch.nn.functional as F

from unet_parts import *


class UNet(nn.Module):
    def __init__(self, n_channels, bilinear=True):
        super(UNet, self).__init__()
        self.n_channels = n_channels
        self.bilinear = bilinear

        self.inc = DoubleConv(n_channels, 64*3//2)
        self.down1 = Down(64*3//2, 128*3//2)
        self.down2 = Down(128*3//2, 256*3//2)
        self.down3 = Down(256*3//2, 512*3//2)
        factor = 2 if bilinear else 1
        self.down4 = Down(512*3//2, 1024*3//2 // factor)
        self.up1 = Up(1024*3//2, 512*3//2 // factor, bilinear)
        self.up2 = Up(512*3//2, 256*3//2 // factor, bilinear)
        self.up3 = Up(256*3//2, 128*3//2 // factor, bilinear)
        self.up4 = Up(128*3//2, 64*3//2, bilinear)
        self.outc = OutConv(64*3//2, 3)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        logits = self.outc(x)
        return logits