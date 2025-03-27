### Explicație cod - Biti de Paritate Bidimensională (Pas cu Pas)

Acest cod implementează o demonstrație grafică a algoritmului de paritate bidimensională, utilizând biblioteca `pygame` pentru afișarea matricei și interacțiunea cu utilizatorul. Vom parcurge codul linie cu linie pentru a explica fiecare parte a acestuia.

---

#### 1. Importarea modulelor necesare:
```python
import pygame
import random
import time
```
- `pygame`: Biblioteca folosită pentru a crea fereastra grafică și a desena matricea.
- `random`: Pentru a selecta la întâmplare un bit ce urmează să fie corupt.
- `time`: Pentru a implementa întârzieri vizuale în animații.

---

#### 2. Funcția `create_matrix()`:
```python
def create_matrix(binary_str):
    rows = len(binary_str) // 7
    matrix = [list(binary_str[i * 7:(i + 1) * 7]) for i in range(rows)]
    return matrix
```
- Primește un șir binar (`binary_str`) și îl împarte în linii de câte 7 biți.
- Returnează o matrice 2D reprezentată sub formă de listă de liste.

---

#### 3. Funcția `add_parity_bits()`:
```python
def add_parity_bits(matrix):
    rows = len(matrix)
    cols = 7

    for row in matrix:
        row.append(str(row.count('1') % 2))

    parity_col = []
    for col in range(cols + 1):
        ones_count = sum(1 for row in matrix if row[col] == '1')
        parity_col.append(str(ones_count % 2))

    matrix.append(parity_col)
```
- Calculează și adaugă un bit de paritate la fiecare rând, în funcție de numărul de biți `1` din acel rând (par sau impar).
- Calculează și adaugă un rând de paritate la final, care conține câte un bit de paritate pentru fiecare coloană din matrice.

---

#### 4. Funcția `corrupt_bit()`:
```python
def corrupt_bit(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    rand_row, rand_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    matrix[rand_row][rand_col] = '1' if matrix[rand_row][rand_col] == '0' else '0'
    return rand_row, rand_col
```
- Selectează aleatoriu un bit din matrice (fără rândul sau coloana de paritate) și îl inversează (`1` devine `0` și viceversa).
- Returnează coordonatele bitului corupt.

---

#### 5. Funcția `detect_error()`:
```python
def detect_error(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    error_row, error_col = -1, -1

    for i in range(rows):
        if sum(1 for c in matrix[i][:cols] if c == '1') % 2 != int(matrix[i][cols]):
            error_row = i
            break

    for j in range(cols):
        if sum(1 for i in range(rows) if matrix[i][j] == '1') % 2 != int(matrix[rows][j]):
            error_col = j
            break

    return error_row, error_col
```
- Parcurge fiecare rând și calculează paritatea acestuia. Dacă este diferită de bitul de paritate corespunzător, salvează acel rând ca fiind problematic (`error_row`).
- Apoi, parcurge fiecare coloană și calculează paritatea. Dacă diferă de bitul de paritate de pe ultima linie, salvează acea coloană ca fiind problematică (`error_col`).
- Returnează coordonatele erorii detectate (`error_row`, `error_col`).

---

#### 6. Funcția `draw_matrix()`:
```python
def draw_matrix(screen, font, matrix, highlight=None, step=0, delay=0, message=""):
```
- Această funcție se ocupă de afișarea matricei în fereastra grafică `pygame`.
- Parametrii săi sunt:
  - `screen`: Suprafața pe care se desenează matricea.
  - `font`: Fontul folosit pentru a desena textul din fiecare celulă.
  - `matrix`: Matricea curentă de afișat.
  - `highlight`: Celula care urmează să fie evidențiată (detectată ca eroare sau corectată).
  - `step`: Determină culoarea evidențierii (roșu pentru eroare, verde pentru corectare).
  - `delay`: Pauza dintre actualizările grafice pentru a permite utilizatorului să observe animația.
  - `message`: Mesajul explicativ afișat în partea de jos a ecranului.

- Desenează fiecare celulă ca un dreptunghi și afișează textul corespunzător (`0` sau `1`).
- Culoarea celulei se schimbă dacă aceasta este evidențiată ca eroare (`roșu`) sau corectată (`verde`).
- Mesajele explicative apar în partea de jos a ferestrei.

---

### 7. Funcția `main()` - Logica Principală
- Aici se combină toate funcțiile pentru a realiza demonstrația algoritmului.
- Se generează un șir binar și se creează matricea corespunzătoare.
- Se adaugă biți de paritate la rânduri și coloane.
- Se desenează matricea inițială în fereastră (`pygame`).
- Se corupe un bit aleatoriu și se evidențiază acest lucru.
- Se detectează eroarea folosind algoritmul de paritate bidimensională și se corectează dacă este cazul.
- Programul se încheie după detectarea și corectarea erorii.
