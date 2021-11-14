from StructureAndFunctionality.software.software import Software


class ExpressSoftware(Software):
    DEFAULT_TYPE = 'Express'

    def __init__(self, name, capacity_consumption, memory_consumption):
        memory_consumption = 2 * memory_consumption
        super().__init__(name, ExpressSoftware.DEFAULT_TYPE, capacity_consumption, memory_consumption)
