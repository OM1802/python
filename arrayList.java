import java.util.ArrayList;

class Main{
  public static void main(String[] args){
    ArrayList<Integer> numbers= new ArrayList<>();
    numbers.add(10);
    numbers.add(20);
    numbers.add(30);
    numbers.add(40);
    numbers.add(50);

    for(int i=0; i<5; i++){
      System.out.println(numbers.get(i));
    }
    System.out.println(numbers.size());

    numbers.remove(1);
    numbers.set(0,50);
    for(int i=0; i<numbers.size(); i++){
      System.out.println(numbers.get(i));
    }

    System.out.println(numbers.size());
  }


}
