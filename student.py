class STUDENT:
    def __init__(self, name, sname, year, marks):
        self.Name = name
        self.SName = sname
        self.Year = year
        self.Marks = marks
        self.AverMark = self.CalcAvMark()

    def CalcAvMark(self):
        if self.Marks:
            return sum(self.Marks) / len(self.Marks)
        return 0

    def DisplayAll(self):
        print(f"Ім'я: {self.Name}")
        print(f"Прізвище: {self.SName}")
        print(f"Рік народження: {self.Year}")
        print(f"Оцінки: {self.Marks}")
        print(f"Середня оцінка: {self.AverMark:.2f}")