import 'dart:io';

void main() {
  stdout.write('Введите первое число: ');
  int num1 = int.parse(stdin.readLineSync()!);

  stdout.write('Введите второе число: ');
  int num2 = int.parse(stdin.readLineSync()!);

  stdout.write('Выберите операцию (+, -, *, /): ');
  String operator = stdin.readLineSync()!;

  int result;
  switch (operator) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      result = num1 ~/ num2;
      break;
    default:
      stdout.write('Invalid operator');
      return;
  }

  stdout.write('Результат: $result');
}
