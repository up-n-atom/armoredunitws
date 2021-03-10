#Beautify port access
#@author up-n-atom <up-n-atom@eleventwentytwo.com>
#@category References

io = (
  'DISPLAY_CTRL',
  '',
  'LCD_LINE',
  'LCD_INTERRUPT',
  'SPR_AREA',
  'SPR_START_NO',
  'SPR_CNT',
  'SCR_AREA',
  'SCR2_WIN_X1',
  'SCR2_WIN_Y1',
  'SCR2_WIN_X2',
  'SCR2_WIN_Y2',
  'SPR_WIN_X1',
  'SPR_WIN_Y1',
  'SPR_WIN_X2',
  'SPR_WIN_Y2',
  'SCR1_SCRL_X',
  'SCR1_SCRL_Y',
  'SCR2_SCRL_X',
  'SCR2_SCRL_Y',
  'LCD_IF_CTRL',
  'LCD_SEG_DATA',
  '',
  '',
  '',
  '',
  '',
  '',
  'LCD_GRAY_01',
  'LCD_GRAY_23',
  'LCD_GRAY_45',
  'LCD_GRAY_67',
  'SCR_LUT_0',
  'SCR_LUT_0',
  'SCR_LUT_1',
  'SCR_LUT_1',
  'SCR_LUT_2',
  'SCR_LUT_2',
  'SCR_LUT_3',
  'SCR_LUT_3',
  'SCR_LUT_4',
  'SCR_LUT_4',
  'SCR_LUT_5',
  'SCR_LUT_5',
  'SCR_LUT_6',
  'SCR_LUT_6',
  'SCR_LUT_7',
  'SCR_LUT_7',
  'SPR_LUT_0',
  'SPR_LUT_0',
  'SPR_LUT_1',
  'SPR_LUT_1',
  'SPR_LUT_2',
  'SPR_LUT_2',
  'SPR_LUT_3',
  'SPR_LUT_3',
  'SPR_LUT_4',
  'SPR_LUT_4',
  'SPR_LUT_5',
  'SPR_LUT_5',
  'SPR_LUT_6',
  'SPR_LUT_6',
  'SPR_LUT_7',
  'SPR_LUT_7',
  'GDMA_SOURCE_L',
  'GDMA_SOURCE_L',
  'GDMA_SOURCE_H',
  'GDMA_SOURCE_H',
  'GDMA_DESTINATION',
  'GDMA_DESTINATION',
  'GDMA_COUNTER',
  'GDMA_COUNTER',
  'GDMA_CTRL',
  '',
  'SDMA_SOURCE_L',
  'SDMA_SOURCE_L',
  'SDMA_SOURCE_H',
  'SDMA_SOURCE_H',
  'SDMA_COUNTER_L',
  'SDMA_COUNTER_L',
  'SDMA_COUNTER_H',
  'SDMA_COUNTER_H',
  'SDMA_CTRL',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'SYSTEM_CTRL2',
  '',
  'SYSTEM_CTRL3',
  '',
  'HYPERV_LL',
  'HYPERV_LH',
  'HYPERV_RL',
  'HYPERV_RH',
  'HYPERV_SL',
  'HYPERV_SH',
  'HYPERV_CTRL',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'f',
  'SND_FREQ_1',
  'SND_FREQ_1',
  'SND_FREQ_2',
  'SND_FREQ_2',
  'SND_FREQ_3',
  'SND_FREQ_3',
  'SND_FREQ_4',
  'SND_FREQ_4',
  'SND_VOL_1',
  'SND_VOL_2',
  'SND_VOL_3',
  'SND_VOL_4',
  'SND_SWEEP',
  'SND_SWEEP_TIME',
  'SND_NOISE_CTRL',
  'SND_WAVERAM',
  'SND_CH_CTRL',
  'SND_OUT_CTRL',
  'SND_RANDOM',
  'SND_RANDOM',
  'SND_VOL_CH2',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'SYSTEM_CTRL1',
  '',
  'TIMER_CTRL',
  'TIMER_CTRL',
  'H_BLANK_TIMER',
  'H_BLANK_TIMER',
  'V_BLANK_TIMER',
  'V_BLANK_TIMER',
  'H_BLANK_COUNTER',
  'H_BLANK_COUNTER',
  'V_BLANK_COUNTER',
  'V_BLANK_COUNTER',
  '',
  '',
  '',
  '',
  'INT_VECTOR',
  'SERIAL_DATA',
  'INT_ENABLE',
  'SERIAL_STATUS',
  'INT_CAUSE',
  'KEY_SCAN',
  'INT_CAUSE_CLEAR',
  'INT_NMI_CTRL',
  '',
  '',
  'IN_SERIAL_DATA',
  'IN_SERIAL_DATA',
  'IN_SERIAL_COM',
  'IN_SERIAL_COM',
  'IN_SERIAL_CTRL',
  'IN_SERIAL_CTRL',
  'LINEAR_ADDR_OFF',
  'RAM_BANK',
  'ROM_BANK_0',
  'ROM_BANK_1',
  'OUT_SERIAL_DATA',
  'OUT_SERIAL_DATA',
  'OUT_SERIAL_COM',
  'OUT_SERIAL_COM',
  'OUT_SERIAL_CTRL',
  'OUT_SERIAL_CTRL',
  'RTC_CTRL',
  'RTC_DATA',
  'IO_CTRL',
  'IO_SCAN',
  'MEMORY_CTRL',
  '',
  'RAM_BANK_L',
  'RAM_BANK_H',
  'ROM_BANK_0_L',
  'ROM_BANK_0_H',
  'ROM_BANK_1_L',
  'ROM_BANK_1_H',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  ''
)

block = currentProgram.memory.createUninitializedBlock('IOMEM', toAddr(0), 255, True)
block.setRead(True)
block.setWrite(True)
block.setExecute(False)
block.setVolatile(False)

for i, label in enumerate(io):
  if len(label):
    addr = currentProgram.addressFactory.getAddress("IOMEM::" + hex(i))
    createLabel(addr, label, False)
