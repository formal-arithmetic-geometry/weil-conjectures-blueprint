+++
id = "prop-zla-normalized-gcd-reduction"
kind = "theorem"
title = "Normalized gcd reduction over the integers"
order = 1013
tags = ["latex:proposition"]
uses = ["lem-zla-normalized-gauss"]
+++
Let $A_0,B_0\in\mathbf Z[T]$ satisfy $A_0(0)=B_0(0)=1$, and let
$G\in\mathbf Q[T]$ be the unique generator of the ideal
$(A_0,B_0)\subseteq\mathbf Q[T]$ with $G(0)=1$. Define
$A,B\in\mathbf Q[T]$ by $A_0=GA$ and $B_0=GB$. Then

$$
G,A,B\in\mathbf Z[T],
\qquad
G(0)=A(0)=B(0)=1,
$$

the pair $(A,B)$ is coprime in $\mathbf Q[T]$, that is, every common divisor
of $A$ and $B$ is a unit, and

$$
\frac{A_0}{B_0}=\frac{A}{B}
\qquad\text{in }\mathbf Q(T).
$$

## Proof

The ring $\mathbf Q[T]$ is a principal ideal domain, so the ideal
$(A_0,B_0)$ has a generator, unique up to a scalar; since $A_0(0)=1$ the
generator does not vanish at $0$ and may be normalized by $G(0)=1$. Then
$A(0)=B(0)=1$ follows from $A_0(0)=B_0(0)=1$, and
[lem-zla-normalized-gauss] applied to $A_0=GA$ and to $B_0=GB$ gives
$G,A,B\in\mathbf Z[T]$. A common divisor of $A$ and $B$ would multiply $G$ to
a larger common divisor of $A_0$ and $B_0$, contradicting that $G$ generates
their ideal. The fraction is unchanged because $G\neq0$.
