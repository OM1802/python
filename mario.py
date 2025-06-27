def main():
    print_column(3)
    print_row(4)
    print_square(3)
    
def print_square(dim):
    for i in range(dim):
        for j in range(dim):
            print("-", end="")
        print()
    
def print_column(h):
    print("# \n" * h, end="")
    
def print_row(w):
    print("?" * w)

main()
    