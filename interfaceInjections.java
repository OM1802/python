interface Engine{
  void start();
}

class OilCar implements Engine{
  public void start(){
    System.out.println("OIL-CAR ENGINE START");
  }
}

class ElectricCar implements Engine{
  public void start(){
    System.out.println("ELECTRIC-CAR ENGINE START");
  }
}

class Car{
  private Engine engine;

  Car(Engine engine){
    this.engine=engine;
  }

  void startCar(){
    engine.start();
    System.out.println("CAR ENGINE START");
  }
}

class Main{
  public static void main(String[] args){
    Engine e1=new OilCar();
    Car c1=new Car(e1);
    c1.startCar();

    Engine e2=new ElectricCar();
    Car c2=new Car(e2);
    c2.startCar();
  }
}