class Engine{
  void start(){
    System.out.println("ENGINE STARTS");
  }
}

class Car{
  private Engine engine;

  Car(Engine engine){
    this.engine=engine;
  }

  void startCar(){
    engine.start();
    System.out.println("CAR ENGINE STARTS");
  }
}

class Main{
  public static void main(String[] args){
    Engine engine=new Engine();
    Car car=new Car(engine);
    car.startCar();
  }
}