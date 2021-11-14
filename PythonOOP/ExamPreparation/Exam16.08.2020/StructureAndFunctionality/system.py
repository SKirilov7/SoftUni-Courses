from StructureAndFunctionality.hardware.heavy_hardware import HeavyHardware
from StructureAndFunctionality.hardware.power_hardware import PowerHardware
from StructureAndFunctionality.software.express_software import ExpressSoftware
from StructureAndFunctionality.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = System.find_searched_hardware(hardware_name)
        if not searched_hardware:
            return f"Hardware does not exist"
        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            searched_hardware.install(new_software)
            System._software.append(new_software)
        except Exception:
            return f"Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = System.find_searched_hardware(hardware_name)
        if not searched_hardware:
            return f"Hardware does not exist"
        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            searched_hardware.install(new_software)
            System._software.append(new_software)
        except Exception:
            return f"Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            searched_hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name][0]
            searched_software = \
            [software for software in searched_hardware.software_components if software_name == software.name][0]
            searched_hardware.uninstall(searched_software)
            System._software.remove(searched_software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {sum([software.memory_consumption for software in System._software])} / {sum([hardware.memory for hardware in System._hardware])}\n" \
                 f"Total Capacity Taken: {sum([software.capacity_consumption for software in System._software])} / {sum([hardware.capacity for hardware in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += repr(hardware)
        return result

    @staticmethod
    def find_searched_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware
