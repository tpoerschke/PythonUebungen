
# Mathematisch: f(n) = n + f(n-1)
def sequence1(n):
    if n == 1:
        return 1
    else:
        return n + sequence1(n-1)

# Mathematisch: f(n) = f(n-2) - f(n-1)
def sequence2(n):
    if n == 1 or n == 2:
        return n
    else:
        return sequence2(n-2) - sequence2(n-1)

def main():
    print("sequence1(8) =", sequence1(8))
    print("sequence2(8) =", sequence2(8))

if __name__ == "__main__":
    main()