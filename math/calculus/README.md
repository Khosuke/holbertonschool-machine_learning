# Project : Calculus


## Task 0. Sigma is for Sum

What is the result of:

$\sum_{i=2}^5 i$

1. $3 + 4 + 5$
2. $3 + 4$
3. $2 + 3 + 4 + 5$
4. $2 + 3 + 4$

- File: [0-sigma_is_for_sum](0-sigma_is_for_sum)

## Task 1. The Greeks pronounce it sEEgma

What is the result of:

$\sum_{k=1}^4 9i-2k$

1. $90 - 20$
2. $36i - 20$
3. $90 - 8k$
4. $36i - 8k$

- File: [1-seegma](1-seegma)

## Task 2. Pi is for Product

What is the result of:

$\prod_{i=1}^m i$

1. $(m - 1)!$
2. $0$
3. $(m + 1)!$
4. $m!$

- File: [2-pi_is_for_product](2-pi_is_for_product)

## Task 3. The Greeks pronounce it pEE

What is the result of:

$\prod_{i=0}^10 i$

1. $10!$
2. $9!$
3. $100$
4. $0$

- File: [3-pee](3-pee)

## Task 4. Hello, derivatives!

What is the derivative of 

$\frac{dy}{dx}$ where $y = x^4 + 3x^3 - 5x + 1$

1. $3x^3 + 6x^2 - 4$
2. $4x^3 + 6x^2 - 5$
3. $4x^3 + 9x^2 - 5$
4. $4x^3 + 9x^2 - 4$

- File: [4-hello_derivatives](4-hello_derivatives)

## Task 5. A log on the fire

What is the derivative of 

$\frac{d(xln(x))}{dx}$

1. $ln(x)$
2. $\frac{1}{x}$ + 1
3. $ln(x) + 1$
4. $\frac{1}{x}$

- File: [5-log_on_fire](5-log_on_fire)

## Task 6. It is difficult to free fools from the chains they revere

What is the derivative of 

$\frac{d(ln(x^2))}{dx}$

1. $\frac{2}{x}$
2. $\frac{1}{x^2}$
3. $\frac{2}{x^2}$
4. $\frac{1}{x}$

- File: [6-voltaire](6-voltaire)

## Task 7. Partial truths are often more insidious than total falsehoods

$\frac{\partial_ \ }{\partial_ y}f(x, y)$ where $f(x, y) = e^{xy}$ and $\frac{\partial_  x}{\partial_ y}$ = $\frac{\partial_  y}{\partial_ x}$ = 0

1. $e^{xy}$
2. $ye^{xy}$
3. $xe^{xy}$
4. $e^x$

- File: [7-partial_truths](7-partial_truths)

## Task 8. Put it all together and what do you get?

$\frac{\partial_ \ ^2}{\partial_ y\partial_ x}(e^{x^2y})$ where $\frac{\partial_  x}{\partial_ y}$ = $\frac{\partial_  y}{\partial_ x}$ = 0

1. $2x(1 + y)e^{x^2y}$
2. $xe^{xy}$
3. $2x(1+x^2y)e^{x^2y}$
4. $e^{2x}$

- File: [8-all-together](8-all-together)

## Task 9. Our life is the sum total of all the decisions we make every day, and those decisions are determined by our priorities

Write a function `def summation_i_squared(n):` that calculates

$\sum_{i=1}^{n}i^2$

- `n` is the stopping condition
- Return the integer value of the sum
- If `n` is not a valid number, return `None`
- You are not allowed to use any loops

- File: [9-sum_total.py](9-sum_total.py)

## Task 10. Derive happiness in oneself from a good day's work

Write a function def poly_derivative(poly): that calculates the derivative of a polynomial:

- poly is a list of coefficients representing a polynomial
    - the index of the list represents the power of x that the coefficient belongs to
    - Example: if \
    $f(x) = x^3 + 3x +5$ \
    poly is equal to [5, 3, 0, 1]
- If poly is not valid, return None
- If the derivative is 0, return [0]
- Return a new list of coefficients representing the derivative of the polynomial 


- File: [10-matisse.py](10-matisse.py)

## Task 11. Good grooming is integral and impeccable style is a must

$\int_ \ x^3dx$

1. $3x^2+C$
2. $\frac {x^4}{4}+C$
3. $x^4+C$
4. $\frac {x^4}{3}+C$

- File: [11-integral](11-integral)

## Task 12. We are all an integral part of the web of life

$\int_ \ e^{2y}dy$

1. $e^{2y}+C$
2. $e^y+C$
3. $\frac {e^{2y}}{2}+C$
4. $\frac {e^y}{2}+C$

- File: [12-integral](12-integral)

## Task 13. Create a definite plan for carrying out your desire and begin at once

$\int_ 0^3 u^2du $

1. $3$
2. $6$
3. $9$
4. $27$

- File: [13-definite](13-definite)

## Task 14. My talents fall within definite limitations

$\int_ {-1}^0 \frac {1}{v}dv$

1. $-1$
2. $0$
3. $1$
4. $undefined$

- File: [14-definite](14-definite)

## Task 15. Winners are people with definite purpose in life

$\int_ 0^5xdy$

1. $5$
2. $5x$
3. $25$
4. $25x$

- File: [15-definite](15-definite)

## Task 16. Double whammy


$\int_ 1^2 \int_ 0^3x^2y^{-1}dxdy$

1. $9ln(2)$
2. $9$
3. $27ln(2)$
4. $27$


- File: [16-double](16-double)

## Task 17. Integrate

Write a function def poly_integral(poly, C=0): that calculates the integral of a polynomial:

- poly is a list of coefficients representing a polynomial
    - the index of the list represents the power of x that the coefficient belongs to
    - Example: if \
    $f(x) = x^3 + 3x +5$ \
    poly is equal to [5, 3, 0, 1]
- C is an integer representing the integration constant
- If a coefficient is a whole number, it should be represented as an integer
- If poly or C are not valid, return None
- Return a new list of coefficients representing the integral of the polynomial
- The returned list should be as small as possible


- File: [17-integrate.py](17-integrate.py)
