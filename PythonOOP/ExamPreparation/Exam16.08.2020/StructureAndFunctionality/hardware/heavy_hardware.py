from StructureAndFunctionality.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    DEFAULT_TYPE = 'Heavy'

    def __init__(self, name, capacity, memory):
        memory = int(0.75 * memory)
        super().__init__(name, HeavyHardware.DEFAULT_TYPE, capacity * 2, memory)
