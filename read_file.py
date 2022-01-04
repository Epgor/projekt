import numpy as np

#klasa śłużąca na operowaniu danymi, niezbędna do aplikacji okienkowej


class FileOperator:
    def __init__(self, file_name,):
        self.file_name = file_name
        self.data = []

    def default(self):
        self.data = np.array([
            ["Karta", 1, 100],
            ["Rower", 10, 2000],
            ["Telefon", 2, 1000],
            ["bułka", 3, 10],
            ["dropsy", 5, 100],
            ["hulajnoga", 10, 2000],
            ["laptok", 2, 1000],
            ["kamien szlachetny", 1, 500],
            ["maseczki", 1, 100],
            ["skuter", 15, 8000],
            ["iphon", 2, 4000],
            ["ziemniak", 3, 10],
        ])

    def save(self):
        try:
            file = open(self.file_name, "wb")
            np.save(file, self.data)
            file.close
        except:
            print("Błąd przy zapisie")

    def read(self):
        try:
            file = open(self.file_name, "rb")
            self.data = np.load(file)
            file.close
        except:
            print("Błąd przy odczycie")

    def get(self):
        return self.data

    def set(self, data):
        self.data = data

    def append_record(self, record):
        try:
            self.data = np.r_[self.data,[record]]
        except:
            print("Błąd przy dodawaniu rekordu")

    def delete_record(self, record):
        try:
            self.data = np.delete(self.data, record, 0)
        except:
            print("Błąd przy usuwaniu rekordu")


#przykładowe użytkowanie
'''
dupa = FileOperator("ciekawy")
dupa.default()
print(dupa.get())
dupa.append_record(["Witaminy", 2, 50])
print(dupa.get())
dupa.save()
dupa.delete_record(1)
print(dupa.get())
new_data = np.array([
            ["Karta", 1, 100],
            ["Karta", 1, 100]])
dupa.set(new_data)
print(dupa.get())
dupa.read()
print(dupa.get())

'''

