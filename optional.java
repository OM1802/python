import java.util.Optional;

class Main{
  public static void main(String[] args){
    Optional<String> name= Optional.empty();

    System.out.println(name); 

    Optional<String> name2= Optional.of("PRIME");

    System.out.println(name2.get());
    System.out.println(name2.get().length());

    Optional<String> name3=Optional.of("OPTIMUS");
    String name4=name3.orElse("OPTIMUS PRIME");
    System.out.println(name4);

    Optional<String> name5=Optional.empty();
    String name6=name5.orElse("OPTIMUS PRIME");
    System.out.println(name6);
  }
}