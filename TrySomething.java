public class TrySomething{
	public static void main(String[] args) {
		Walrus man = new Walrus(24, "Hacker");
		System.out.println(man);
		int age = 53;

		doSomething(man, age);
		System.out.println(man);
		System.out.println(age);
	}

	public static void doSomething(Walrus obj, int x){
		obj.weight -= 10;
		x = x - 25;

	}
}


class Walrus {
	int weight;
	String name ;
	Walrus(int weight, String username){
		this.weight = weight;
		name = username;
	}

	public String toString(){
		return "[age: " + weight + ": name " + name + "]";
	}
}