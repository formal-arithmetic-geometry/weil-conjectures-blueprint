+++
id = "thm-zla-integral-fatou"
kind = "theorem"
title = "Integral Fatou theorem"
order = 1015
uses = ["def-zla-rational-germ", "lem-zla-normalized-fraction-unique", "prop-zla-integral-presentation", "prop-zla-normalized-gcd-reduction"]
+++
Let $f(T)\in1+T\mathbf Z[[T]]$ be the Taylor series of a normalized rational
germ over $\mathbf Q$. There is a unique pair of polynomials
$A,B\in\mathbf Z[T]$, coprime in $\mathbf Q[T]$, satisfying

$$
A(0)=B(0)=1,
\qquad
f(T)=\frac{A(T)}{B(T)}.
$$

This is the *normalized reduced integral presentation* of $f$.

## Proof

[prop-zla-integral-presentation] produces $A_0,B_0\in\mathbf Z[T]$ with
$B_0f=A_0$; here $A_0(0)=f(0)=1=B_0(0)$. Reducing this fraction by
[prop-zla-normalized-gcd-reduction] gives coprime integral $A,B$ with
constant coefficient $1$ and $A/B=A_0/B_0=f$. If $(A',B')$ is a second pair
with the same properties, then $A'/B'=f=A/B$ and both denominators are nonzero,
so cross multiplication gives $A'B=B'A$; both pairs are coprime and all four
polynomials have constant coefficient $1$, so
[lem-zla-normalized-fraction-unique] over $\mathbf Q$ yields $A'=A$ and
$B'=B$.
