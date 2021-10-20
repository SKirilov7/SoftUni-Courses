class Integer:
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000,
             'IV': 4,
             'IX': 9,
             'XL': 40,
             'XC': 90,
             'CD': 400,
             'CM': 900}

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) == float:
            return cls(int(value))
        return "value is not a float"


    @classmethod
    def from_roman(cls, value):
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in Integer.roman:
                num += Integer.roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += Integer.roman[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"
        return "wrong type"

    def add(self, integer):
        if hasattr(integer, 'value'):
            self.value += integer.value
            return self.value
        return "number should be an Integer instance"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))






