import java.util.Set;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;

class Main{
  public static void main(String[] args){
    Set<Integer> n=new HashSet<>();//unique && no guarantee of order of elements
    n.add(10);
    n.add(20);
    n.add(30);
    n.add(10);
    n.add(20);
    n.add(30);

    System.out.println(n);
    System.out.println(n.add(55));
    System.out.println(n.add(10));
    System.out.println(n);

    Set<Integer> n2=new LinkedHashSet<>();// uniques && order of elements guaranteed same as input
    n2.add(10);
    n2.add(20);
    n2.add(30);
    n2.add(10);
    n2.add(20);
    n2.add(30);

    System.out.println(n2);

    Set<Integer> n3=new TreeSet<>();// unique && in sorted order by default
    n3.add(80);
    n3.add(20);
    n3.add(10);
    n3.add(10);
    n3.add(1000);
    n3.add(1);

    System.out.println(n3);
    System.out.println(n3.contains(20));
    System.out.println(n3.contains(5));
  }
}