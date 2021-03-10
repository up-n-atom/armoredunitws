# Imports symbols from LSIC-86 map file
# @author up-n-atom <up-n-atom@eleventwentytwo.com>
# @category Data

from ghidra.app.util.bin import RandomAccessByteProvider

g_map_file = askFile("Choose MAP file", "Load Map File")

rbp = RandomAccessByteProvider(getProgramFile())

with open(str(g_map_file)) as map_file:
  for rline in map_file:
    sline = rline.strip()

    if not sline:
      head = next(map_file, '\n').strip().split()

      if head:
        try:
          while not sline:
            sline = next(map_file).strip()
        except:
          continue

    symbol = dict(zip(head, sline.split()))

    if 'Class' in symbol:
      for key in ['Start', 'Stop', 'Length']:
        symbol[key] = int(symbol[key][:-1], 16)

      if symbol['Length'] == 0:
        continue

      if symbol['Start'] >= 0x20000:
        block = createMemoryBlock(symbol['Name'], toAddr(symbol['Start']), rbp.getInputStream(symbol['Start'] - 0x80000), symbol['Length'], False)
        block.setWrite(False)
        block.setVolatile(False)
      else:
        block = currentProgram.memory.createUninitializedBlock(symbol['Name'], toAddr(symbol['Start']), symbol['Length'], False)
        block.setWrite(True)
        block.setVolatile(True)

      block.setRead(True)

      if symbol['Class'] in ['CODE', 'EXTRA']:
        block.setExecute(True)
      else:
        block.setExecute(False)

    if 'Address' in symbol:
      segment, offset = map(lambda x: int(x, 16), symbol['Address'].split(':'))
      address = (segment << 4) + offset

      createLabel(toAddr(address), symbol['Publics'], False)

      block = getMemoryBlock(toAddr(address))

      if block and block.isExecute():
        disassemble(toAddr(address))
