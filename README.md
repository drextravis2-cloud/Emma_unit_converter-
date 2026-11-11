# Engineering Unit Converter

## What it does
A menu-driven Python program that converts between mm and inches, °C and °F, kg and lb, and km/h and m/s. It keeps running until the user quits and handles wrong input (like typing letters instead of numbers) without crashing.

## How to run it
Install Python 3, then run: python unit_converter.py

## Sample output
```
Choose an option: 3
Enter value in °C: 100
Result: 100 °C = 212.0000 °F

Choose an option: 1
Enter value in mm: abc
Invalid input. Please type a number, e.g. 25 or 3.5
Enter value in mm: 25.4
Result: 25.4 mm = 1.0000 inches

Choose an option: 9
--- Conversion history ---
1. 100 °C = 212.0000 °F
2. 25.4 mm = 1.0000 inches
```

## My own twist
- A **conversion history** (option 9) that lists every conversion done in the session.
- **Physical checks**: it rejects temperatures below absolute zero and negative lengths or masses.

## What I learned
- How to use `try/except` so the program does not crash on bad input.
- How to store functions in a dictionary to build a clean menu.

## Author
Emmanuel Okonye uchechukwu, ND1 Mechatronics Engineering, YabaTech.
