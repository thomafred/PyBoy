# -*- encoding: utf-8 -*-
#
# Authors: Asger Anders Lund Hansen, Mads Ynddal and Troels Ynddal
# License: See LICENSE file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import CPU, RAM, Cartridge, BootROM, LCD, Timer, CoreDump

class Motherboard():
    from MemoryManager import __getitem__, __setitem__, transferDMAtoOAM
    from StateManager import saveState, loadState
    from Coordinator import calculateCycles, setSTATMode, checkLYC, tickFrame
    from CPU.flags import TIMER

    def __init__(self, gameROMFile, bootROMFile, window, interaction):
        self.MainWindow = window

        self.timer = Timer.Timer()
        self.interaction = interaction
        self.cartridge = Cartridge.Cartridge(gameROMFile)
        self.bootROM = BootROM.BootROM(bootROMFile)
        self.ram = RAM.RAM(random=False)
        self.cpu = CPU.CPU(self)
        self.lcd = LCD.LCD(self)

        self.bootROMEnabled = True

        CoreDump.RAM = self.ram
        CoreDump.CPU = self.cpu

    def buttonEvent(self, key, state):
        #self.interaction.keyEvent(key)
        self.cpu.setInterruptFlag(self.cpu.HightoLow)

