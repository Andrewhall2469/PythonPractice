class Results:
    phy = 0
    che = 0
    mat = 0
    def showResults(self):
        total = self.phy + self.che + self.mat
        print("Result =", total)
        print("Average Result =", total // 3)
        if total < 70:
            print("Failed")
        else:
            print("Passed")

smith = Results()
peter = Results()

peter.phy = 75
peter.che = 100
peter.mat = 90

smith.phy = 55
smith.che = 90
smith.mat = 66

print("Peters results:")
peter.showResults()

print("-------------------------")

print("Smiths results:")
smith.showResults()