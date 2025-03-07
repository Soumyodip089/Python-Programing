# 1.Write a python program to display the first ten terms of the following series 2 5 10 17

def series(n):
    terms = []
    for i in range(1, n + 1):
        term = i**2 + 1 
        terms.append(term)
    return terms

def main():
    n = int(input("Enter a range :")) 
    terms = series(n)
    print(f"First {n} Terms of the series:")
    for i, term in enumerate(terms):
        print(f"Term {i + 1} : {term}")

if __name__ == "__main__":
    main()