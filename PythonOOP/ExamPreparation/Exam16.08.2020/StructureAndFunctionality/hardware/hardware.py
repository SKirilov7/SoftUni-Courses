class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):

        if software.memory_consumption <= self.memory and software.capacity_consumption <= self.capacity:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    def __repr__(self):
        result = f"Hardware Component - {self.name}\n" \
                 f"Express Software Components: {len([software for software in self.software_components if software.__class__.__name__ == 'ExpressSoftware'])}\n" \
                 f"Light Software Components: {len([software for software in self.software_components if software.__class__.__name__ == 'LightSoftware'])}\n" \
                 f"Memory Usage: {sum([soft.memory_consumption for soft in self.software_components])} / {self.memory}\n" \
                 f"Capacity Usage: {sum([soft.capacity_consumption for soft in self.software_components])} / {self.capacity}\n" \
                 f"Type: {self.hardware_type}\n" \
                 f"Software Components: {', '.join([software.name for software in self.software_components]) if self.software_components else 'None'}\n"
        return result

