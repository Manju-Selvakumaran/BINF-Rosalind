# DNA Reverse Complement Calculator

## Problem Statement

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The **reverse complement** of a DNA string s is the string s<sup>c</sup> formed by:
1. **Reversing** the symbols of s
2. **Taking the complement** of each symbol

**Example**: The reverse complement of "GTCA" is "TGAC"

**Given**: A DNA string s of length at most 1000 bp.

**Return**: The reverse complement s<sup>c</sup> of s.

---

## Background: DNA Structure

DNA (Deoxyribonucleic Acid) is a double helix structure where two complementary strands run in opposite directions:
```
5' - A T G C C G T A - 3'  (Original strand)
     | | | | | | | |
3' - T A C G G C A T - 5'  (Complementary strand)
```

### Base Pairing Rules
- **Adenine (A)** pairs with **Thymine (T)**
- **Guanine (G)** pairs with **Cytosine (C)**

The reverse complement represents the complementary strand read in the 5' to 3' direction, which is essential for DNA replication, PCR primer design, and sequencing analysis.

---

## Solution Approach

### Algorithm Steps

1. **Input**: Read DNA string from user
2. **Reverse**: Use Python string slicing `[::-1]` to reverse the string
3. **Complement**: Iterate through each nucleotide and apply base pairing rules:
   - A → T
   - T → A
   - G → C
   - C → G
4. **Output**: Print the reverse complement

### Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the DNA string
- **Space Complexity**: O(n) for storing the reversed and complemented strings

---

## Implementation
```python
Dna = input('Enter the strand of DNA: ')
revDna = Dna[::-1]
revComp = ''

for nt in revDna:
    if nt == 'A':
        revComp += 'T'
    elif nt == 'G':
        revComp += 'C'
    elif nt == 'C':
        revComp += 'G'
    elif nt == 'T':
        revComp += 'A'

print(revComp)
```

### Code Breakdown

**Step 1: Input**
```python
Dna = input('Enter the strand of DNA: ')
```
Reads the DNA string from user input.

**Step 2: Reverse the String**
```python
revDna = Dna[::-1]
```
Uses Python slicing notation `[::-1]` to reverse the DNA string.
- Example: "AAAACCCGGT" → "TGGCCCAAAA"

**Step 3: Build Complement**
```python
revComp = ''
for nt in revDna:
    if nt == 'A':
        revComp += 'T'
    elif nt == 'G':
        revComp += 'C'
    elif nt == 'C':
        revComp += 'G'
    elif nt == 'T':
        revComp += 'A'
```
Iterates through each nucleotide in the reversed string and applies Watson-Crick base pairing rules to build the complement.

**Step 4: Output**
```python
print(revComp)
```
Displays the final reverse complement.

---

## Example Walkthrough

### Sample Input
```
AAAACCCGGT
```

### Step-by-Step Process

**Step 1: Original DNA**
```
AAAACCCGGT
```

**Step 2: After Reversal**
```
AAAACCCGGT → TGGCCCAAAA
```

**Step 3: After Complementation**
```
T → A
G → C
G → C
C → G
C → G
C → G
A → T
A → T
A → T
A → T
```

**Result**: `ACCGGGTTTT`

### Sample Output
```
ACCGGGTTTT
```

---

## Usage

### Running the Program
```bash
python reverse_complement.py
```

### Example Session
```
Enter the strand of DNA: AAAACCCGGT
ACCGGGTTTT
```

### Additional Test Cases

| Input | Output | Explanation |
|-------|--------|-------------|
| `AAAACCCGGT` | `ACCGGGTTTT` | Sample from problem |
| `GTCA` | `TGAC` | Simple example |
| `ATCG` | `CGAT` | Four different nucleotides |
| `TTTT` | `AAAA` | All same nucleotide |

---

## Key Concepts

### String Slicing in Python
The `[::-1]` notation is a powerful Python feature for reversing sequences:
- `[start:stop:step]` is the general slicing syntax
- `[::-1]` means: start from the end, go to the beginning, step backwards by 1
- Creates a new string (doesn't modify original)

### Watson-Crick Base Pairing
- **Complementary base pairing**: A pairs with T, G pairs with C
- **Hydrogen bonds**: A=T has 2 hydrogen bonds, G≡C has 3 hydrogen bonds
- **Antiparallel strands**: DNA strands run in opposite directions (5' to 3' and 3' to 5')

### Biological Significance
- **DNA Replication**: Each strand serves as a template for its complement
- **PCR**: Primers must be reverse complements of target sequences
- **Gene Expression**: mRNA is transcribed from the complementary strand

---


