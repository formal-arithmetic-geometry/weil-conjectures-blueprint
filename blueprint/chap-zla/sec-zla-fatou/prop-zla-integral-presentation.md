+++
id = "prop-zla-integral-presentation"
kind = "theorem"
title = "Integral rational presentation"
order = 1011
tags = ["latex:proposition"]
uses = ["def-zla-rational-germ", "lem-zla-integral-cayley-hamilton", "thm-zla-hankel-descent"]
+++
Let $f(T)=\sum_{n\geq0}a_nT^n\in\mathbf Z[[T]]$ be the Taylor series of a
normalized rational germ over $\mathbf Q$. Then there exist
$A_0,B_0\in\mathbf Z[T]$ with $B_0(0)=1$ and $A_0(0)=a_0$ such that

$$
B_0(T)f(T)=A_0(T)
\qquad\text{in }\mathbf Z[[T]].
$$

One may take $B_0(T)=1+c_{r-1}T+\cdots+c_0T^r$ built from the characteristic
polynomial of the shift on the integral shift lattice.

## Proof

Rationality over $\mathbf Q$ makes $\operatorname{Sh}_{\mathbf Q}(a)$
finite-dimensional, so the integral shift lattice is defined and
[lem-zla-integral-cayley-hamilton] applies. Multiplying $f$ by the
integral polynomial $B_0$ built from the recurrence kills every coefficient in
degree at least $r$, so the product is a polynomial with integer coefficients;
its constant coefficient is $a_0$ because $B_0(0)=1$.
