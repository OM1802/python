import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scanner=new Scanner(System.in);
    System.out.print("ENTER YOUR NAME PLEASE: ");
    String name=scanner.nextLine();
    System.out.print("YOUR NAME IS "+ name);
    scanner.close();
  }
}