class Chicken extends Animal {
    // Constructor
    public Chicken(String name, int legs, int age) {
        super(name, legs, age);
    }

    // Additional methods
    public void walk() {
        System.out.println(getName() + " is walking.");
    }

    public void eat() {
        System.out.println(getName() + " is eating.");
    }
}

public class Main {
    public static void main(String[] args) {
        Chicken chicken = new Chicken("Chicken", 2, 1);
        chicken.walk();  // Output: "Chicken is walking."
        chicken.eat();  // Output: "Chicken is eating."
    }
}
