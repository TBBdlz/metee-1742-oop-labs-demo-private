interface X {
	void show();
}

public class TestLambda {
	public static void main(String[] args) {
		X obj = () -> {
			System.out.println("Hello");
		};
	}

}
