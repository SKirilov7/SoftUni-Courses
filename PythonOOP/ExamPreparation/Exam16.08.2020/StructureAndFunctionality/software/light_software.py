from StructureAndFunctionality.software.software import Software


class LightSoftware(Software):
    DEFAULT_TYPE = 'Light'

    def __init__(self, name, capacity_consumption, memory_consumption):
        memory_consumption = memory_consumption // 2
        capacity_consumption = int(1.5 * capacity_consumption)
        super().__init__(name, LightSoftware.DEFAULT_TYPE, capacity_consumption, memory_consumption)
