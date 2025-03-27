# Explicatie cod - CRC (Cyclic Redundancy Check)

Acest document explica fiecare functie din codul care implementeaza algoritmul CRC pentru verificarea erorilor in transmisia de date.

## 1. Functia `xor_operation`
```python
    def xor_operation(dividend, divisor):
        result = list(dividend)
        for i in range(len(divisor)):
            result[i] = '0' if result[i] == divisor[i] else '1'
        return ''.join(result)
```
### Ce face:
Aceasta functie primeste doua siruri de caractere (`dividend` si `divisor`) si aplica operatia de XOR intre ele, bit cu bit. 

### Cum functioneaza:
- Converteste `dividend` intr-o lista de caractere pentru a putea fi modificat (deoarece sirurile sunt imutabile in Python).
- Parcurge fiecare caracter al `divisor` si aplica XOR:
  - Daca cei doi biti sunt egali (`0` si `0` sau `1` si `1`), rezultatul este `0`.
  - Daca sunt diferiti (`0` si `1` sau `1` si `0`), rezultatul este `1`.
- Returneaza rezultatul ca un sir de caractere.

---

## 2. Functia `divide_message`
```python
    def divide_message(message, generator):
        remainder = message[:len(generator)]
        steps = []

        while len(message) >= len(generator):
            if remainder[0] == '1':
                remainder = xor_operation(remainder, generator) + message[len(generator)] if len(message) > len(generator) else xor_operation(remainder, generator)
            else:
                remainder = remainder[1:] + (message[len(generator)] if len(message) > len(generator) else '')

            steps.append(remainder)
            message = message[1:]

        return remainder, steps
```
### Ce face:
Aceasta functie imparte mesajul folosind generatorul si aplica operatia de XOR iterativ pentru a calcula restul CRC (remainder).

### Cum functioneaza:
- `remainder` primeste primele caractere din mesaj, de lungime egala cu `generator`.
- `steps` stocheaza rezultatele intermediare ale operatiei de XOR pentru a le afisa mai tarziu.
- Parcurge mesajul printr-un `while` loop:
  - Daca primul bit al `remainder` este `1`, se efectueaza operatia de XOR cu `generator` si se adauga urmatorul bit din mesaj, daca exista.
  - Daca primul bit este `0`, bitul din stanga este eliminat si se adauga urmatorul bit din mesaj, daca exista.
  - Stocheaza rezultatul intermediar in `steps` si elimina primul caracter din `message`.
- Returneaza `remainder` si lista de pasi (`steps`).

---

## 3. Functia `crc_algorithm`
```python
    def crc_algorithm(message, generator):
        if not (all(bit in '01' for bit in message) and all(bit in '01' for bit in generator)):
            raise ValueError("Mesajul si polinomul trebuie sa fie siruri binare")

        if len(message) <= len(generator):
            raise ValueError("Mesajul trebuie sa fie mai lung decat polinomul generator")

        message_extended = message + '0' * (len(generator) - 1)

        remainder, steps = divide_message(message_extended, generator)

        return message_extended, remainder, steps
```
### Ce face:
Aceasta functie implementeaza logica principala a algoritmului CRC, incluzand validarea datelor introduse de utilizator.

### Cum functioneaza:
- Verifica daca mesajul si generatorul sunt binare.
- Verifica daca mesajul este mai lung decat generatorul.
- Adauga un numar de `0`-uri egal cu gradul generatorului la sfarsitul mesajului (`message_extended`).
- Apeleaza `divide_message()` pentru a obtine `remainder` si pasii de calcul (`steps`).

---

## 4. Functia `main`
```python
    def main():
        message = input("Introdu mesajul binar: ")
        generator = input("Introdu polinomul generator: ")

        try:
            message_extended, remainder, steps = crc_algorithm(message, generator)

            print(f"Mesaj extins: {message_extended}")
            print("Rezultatele intermediare XOR:")
            for step in steps:
                print(step)

            transmitted_message = message + remainder
            print(f"Mesajul transmis: {transmitted_message}")

        except ValueError as e:
            print(e)
```
### Ce face:
Aceasta functie este responsabila pentru interactiunea cu utilizatorul si afisarea rezultatelor.

### Cum functioneaza:
- Primeste mesajul si generatorul de la utilizator.
- Apeleaza `crc_algorithm()` si afiseaza pasii intermediari si mesajul transmis final.
- Gestioneaza erorile prin `try-except`.

---
