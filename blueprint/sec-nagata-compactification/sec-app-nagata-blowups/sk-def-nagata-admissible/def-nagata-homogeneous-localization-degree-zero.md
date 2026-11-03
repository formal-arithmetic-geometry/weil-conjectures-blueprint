+++
id = "def-nagata-homogeneous-localization-degree-zero"
kind = "definition"
title = "Degree-zero homogeneous localization"
order = 54
lean = ["HomogeneousLocalization.Away"]
+++
Let $R=\bigoplus_{n\geq0}R_n$ be an $\mathbb N$-graded commutative ring and
let $f\in R$. Write $R_{(f),0}$ for the degree-zero part of the homogeneous
localization of $R$ away from $f$. Its elements are represented by

$$
\frac{x}{f^m},\qquad m\geq0,\quad x\in R_e,\quad f^m\in R_e
\text{ for some } e,
$$

modulo the ordinary localization relation. When $f\in R_d$ these are the
fractions $x/f^m$ with $x\in R_{md}$.
