+++
id = "def-nagata-rees-algebra"
kind = "definition"
title = "Rees algebra"
order = 60
lean = ["reesAlgebra"]
+++
Let $A$ be a ring and $I\subseteq A$ an ideal. The Rees algebra is

$$
\mathcal R_A(I)=\bigoplus_{n\geq 0}I^nt^n\subseteq A[t].
$$

Its underlying ring is the subring of $A[t]$ consisting of polynomials whose
coefficient of $t^n$ belongs to $I^n$.
