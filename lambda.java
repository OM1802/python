interface addition{
  int add(int a, int b);
}

class Main{
  public static void main(String[] args){
    addition a= (n1, n2)-> n1+ n2;

    System.out.println(a.add(5,12));
  }
}