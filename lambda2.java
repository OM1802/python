interface Calculator{
  int calculate(int a, int b);
}

class Main{
  public static void main(String[] args){
    Calculator addition=(n1, n2) -> n1 + n2;
    System.out.println(addition.calculate(20,56));
    Calculator substraction=(n1, n2) -> n1 - n2;
    System.out.println(substraction.calculate(20,56));
    Calculator multiplication=(n1, n2) -> n1 * n2;
    System.out.println(multiplication.calculate(20,56));
  }
}