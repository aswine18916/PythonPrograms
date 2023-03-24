def design(n):
        for i in range(1, n + 1):
            print("+", end="")
            for i in range(1, n+1):
                print("-",end="")
            print("\n")
            print("|"+(" ")*(n), end="")

design(5)