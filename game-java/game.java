import java.util.Scanner;

public class game {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Добро пожаловать в игру угадай число!");
    System.out.println("Угадайте число от 1 до 100: ");
    int target = (int) (Math.random() * 100) + 1;
    int guess = 0;
    while (guess != target) {
      guess = scanner.nextInt();
      if (guess < target) {
        System.out.println("Слишком мало, попробуйте еще раз: ");
      } else if (guess > target) {
        System.out.println("Слишком много, попробуйте еще раз: ");
      }
    }
    System.out.println("Вы выиграли!");
    scanner.close();
  }
}
