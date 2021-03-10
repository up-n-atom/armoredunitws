#Corrects far pointer
#@author up-n-atom <up-n-atom@eleventwentytwo.com>
#@category Data Types
#@keybinding F6

from ghidra.program.model.data import Pointer32DataType
from ghidra.program.model.symbol import RefType
from ghidra.program.model.address import SegmentedAddress

data = createData(currentAddress, Pointer32DataType.dataType)

print(currentLocation)
print(data.getValue())
print(format(data.getValue().getSegmentOffset(), '04x') + ":" + format(data.getValue().getSegment(), '04x'))

data.removeValueReference(data.getValue().getPhysicalAddress())

createMemoryReference(data, toAddr("{0:04x}:{1:04x}".format(data.getValue().getSegmentOffset(), data.getValue().getSegment())), RefType.DATA)
