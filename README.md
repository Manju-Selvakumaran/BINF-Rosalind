# Mendelian Inheritance Probability Calculator

## Problem Statement

Given a population with three genotype groups:
- **k** individuals: Homozygous dominant (AA)
- **m** individuals: Heterozygous (Aa)
- **n** individuals: Homozygous recessive (aa)

**Objective**: Calculate the probability that two randomly selected organisms will produce offspring with the **dominant phenotype** (at least one dominant allele).

---

## Solution Approach

### Strategy: Complement Probability

It's easier to calculate the probability of the **recessive phenotype** (aa) and subtract from 1:
```
P(dominant phenotype) = 1 - P(recessive phenotype)
```

An offspring displays the recessive phenotype **only** if it has genotype **aa**.

---

## Mathematical Derivation

### Step 1: Identify Crosses That Produce aa Offspring

Using Punnett squares, only these crosses can produce aa offspring:

| Parent Cross | P(aa offspring) |
|-------------|----------------|
| Aa × Aa | 1/4 |
| Aa × aa | 1/2 |
| aa × aa | 1 |

All other crosses (AA × AA, AA × Aa, AA × aa) **cannot** produce aa offspring.

---

### Step 2: Calculate Selection Probabilities

When selecting 2 organisms without replacement from a population of (k+m+n):
- **Total possible pairings**: (k+m+n)(k+m+n-1)

For each cross type, we count the number of ways to select that pairing:

#### Aa × Aa Cross
- Select first Aa: m choices
- Select second Aa: (m-1) choices
- **Ways to select**: m(m-1)
- **Contribution to P(aa)**: m(m-1) × (1/4)

#### Aa × aa Cross
- Can select Aa first, then aa: m × n ways
- Can select aa first, then Aa: n × m ways
- **Ways to select**: 2mn
- **Contribution to P(aa)**: 2mn × (1/2) = mn

#### aa × aa Cross
- Select first aa: n choices
- Select second aa: (n-1) choices
- **Ways to select**: n(n-1)
- **Contribution to P(aa)**: n(n-1) × 1

---

### Step 3: Compute P(aa offspring)

Combine all contributions:
```
P(aa) = [m(m-1) × (1/4) + 2mn × (1/2) + n(n-1) × 1] / [(k+m+n)(k+m+n-1)]
```

Simplifying:
```
P(aa) = [m(m-1)/4 + mn + n(n-1)] / [(k+m+n)(k+m+n-1)]
```

Multiply numerator and denominator by 4:
```
P(aa) = [m(m-1) + 4mn + 4n(n-1)] / [4(k+m+n)(k+m+n-1)]
```

---

### Step 4: Final Formula
```
P(dominant) = 1 - [m(m-1) + 4mn + 4n(n-1)] / [4(k+m+n)(k+m+n-1)]
```

---

## Implementation
```python
k = int(input('Enter population of k : '))
m = int(input('Enter population of m : '))
n = int(input('Enter population of n : '))

prob = 1 - (((m*(m-1)) + (4*m*n) + (4*n*(n-1)))/(4*(k+m+n)*(k+m+n-1)))

print(prob)
```

### Code Breakdown

- **Numerator**: `m*(m-1) + 4*m*n + 4*n*(n-1)`
  - `m*(m-1)`: Contribution from Aa × Aa crosses producing aa
  - `4*m*n`: Contribution from Aa × aa crosses producing aa (simplified from 2mn × 1/2 × 4)
  - `4*n*(n-1)`: Contribution from aa × aa crosses producing aa

- **Denominator**: `4*(k+m+n)*(k+m+n-1)`
  - Total possible pairings multiplied by 4 (from simplification)

- **Subtraction from 1**: Converts P(aa) to P(dominant phenotype)

---

## Example Calculation

**Input**: 
```
k = 2 (AA individuals)
m = 2 (Aa individuals)
n = 2 (aa individuals)
Total population = 6
```

**Step-by-step**:
```
Numerator = 2(1) + 4(2)(2) + 4(2)(1)
          = 2 + 16 + 8
          = 26

Denominator = 4(6)(5)
            = 120

P(aa) = 26/120 ≈ 0.2167

P(dominant) = 1 - 0.2167 = 0.7833
```

**Result**: Approximately **78.33%** chance of producing offspring with dominant phenotype.

---

## Usage

Run the script and provide input values:
```bash
$ python mendelian_inheritance.py
Enter population of k : 2
Enter population of m : 2
Enter population of n : 2
0.7833333333333333
```

---

## Key Insights

1. **Complement approach** simplifies calculation by focusing on the single recessive outcome
2. **Order matters** in selection: picking organism A then B is different from B then A
3. **Without replacement** affects probabilities: (m-1) and (n-1) terms account for this
4. The formula elegantly captures all Mendelian inheritance patterns in one expression

---

## References
- Mendelian genetics and Punnett square analysis
