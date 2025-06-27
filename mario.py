def main():
    print_column(3)
    print_row(4)
    
def print_column(h):
    print("# \n" * h, end="")
    
def print_row(w):
    print("?" * w)

main()
    