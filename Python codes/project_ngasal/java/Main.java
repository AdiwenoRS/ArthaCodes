public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal("Chicken", 4, 10);
        
        // Set animal's second attribute from 4 to 2
        animal.setLegs(2);

        System.out.println(animal.getName());  // Output: "Chicken"
        System.out.println(animal.getLegs());  // Output: 2
        System.out.println(animal.getAge());  // Output: 10
        System.out.println("Animal: " + animal.getName() + " Have " + animal.getLegs() + " Legs");  // Output: "Animal: Chicken Have 2 Legs"
    }
}