class Animal {
    private String name;
    private int legs;
    private int age;

    // Constructor
    public Animal(String name, int legs, int age) {
        this.name = name;
        this.legs = legs;
        this.age = age;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getLegs() {
        return legs;
    }

    public int getAge() {
        return age;
    }

    // Setters
    public void setName(String name) {
        this.name = name;
    }

    public void setLegs(int legs) {
        this.legs = legs;
    }

    public void setAge(int age) {
        this.age = age;
    }
}


