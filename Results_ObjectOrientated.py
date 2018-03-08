class results:
    def marks(self, a, b, c):
        self.phy = a
        self.che = b
        self.math = c
    def show_result(self):
        total = self.phy + self.che + self.math
        print("Overall Result:", total)

Peter = results()
Peter.marks(70,70,70)
print(Peter.phy)
print(Peter.che)
print(Peter.math)
Peter.show_result()
