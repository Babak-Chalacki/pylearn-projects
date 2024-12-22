class Carpet:
    def __init__(self, n):
        self.n = n
        self.pattern = []

    def create(self):
        if self.n % 2 == 0:
            raise ValueError("عدد ورودی باید فرد باشد.")
        
        self.pattern = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == j or i + j == self.n - 1 or i == self.n // 2 or j == self.n // 2:
                    row.append('*')
                else:
                    row.append('-')
            self.pattern.append(''.join(row))
        
        return self

    def display(self):
        if not self.pattern:
            return "قالیچه هنوز ساخته نشده است."
        return '\n'.join(self.pattern)

try:
    n = int(input("لطفاً یک عدد فرد وارد کنید: "))
    carpet = Carpet(n)
    print(carpet.create().display())
except ValueError as e:
    print(e)
