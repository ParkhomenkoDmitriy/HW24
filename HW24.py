class String(str):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)

    def __add__(self, other):
        return String(self.value + str(other))

    def __sub__(self, other):
        string_1 = self.value
        string_2 = str(other)

        if string_2 in string_1:
            result = string_1.replace(string_2, "", 1)
        else:
            result = string_1

        return String(result)

    def __str__(self):
        return self.value


output = "\n".join([
    str(String('New') + String(890)),
    str(String(1234) + 5678),
    str(String('New') + 'castle'),
    str(String('New') + 77),
    str(String('New') + True),
    str(String('New') + ['s', ' ', 23]),
    str(String('New') + None),
    20 * '-',
    str(String('New bala7nce') - 7),
    str(String('New balance') - 'bal'),
    str(String('New balance') - 'Bal'),
    str(String('pineapple apple pine') - 'apple'),
    str(String('New balance') - 'apple'),
    str(String('NoneType') - None),
    str(String(55678345672) - 7)
])
print(output)

