from StructureAndFunctionality.hardware.hardware import Hardware


class PowerHardware(Hardware):
    DEFAULT_TYPE = 'Power'

    def __init__(self, name, capacity, memory):
        capacity = int(capacity * 0.25)
        memory = int(memory * 1.75)
        super().__init__(name, PowerHardware.DEFAULT_TYPE, capacity, memory)
