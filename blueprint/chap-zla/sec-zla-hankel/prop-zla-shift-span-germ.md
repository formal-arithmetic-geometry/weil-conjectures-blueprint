+++
id = "prop-zla-shift-span-germ"
kind = "theorem"
title = "Finite shift span supplies a rational germ"
order = 1003
tags = ["latex:proposition"]
uses = ["def-zla-rational-germ", "def-zla-shift-span"]
+++
Assume $W=\operatorname{Sh}_K(a)$ is finite-dimensional of dimension $r$. The
shift restricts to an endomorphism $S_W:W\to W$. Write

$$
\det(U-S_W)=U^r+c_{r-1}U^{r-1}+\cdots+c_0
$$

and set $B_a(T)=1+c_{r-1}T+\cdots+c_0T^r$. If
$f_a(T)=\sum_{n\geq0}a_nT^n$, then $B_a(T)f_a(T)$ is a polynomial $A_a(T)$.
If $r=0$ then $a=0$ and $A_a=0$; if $r>0$ then $\deg A_a<r$. In both cases
$f_a(T)=\tau_K[A_a,B_a]$.

## Proof

Cayley–Hamilton applied to $S_W$ gives
$S^ra+c_{r-1}S^{r-1}a+\cdots+c_0a=0$ in $W$, that is
$a_{n+r}+c_{r-1}a_{n+r-1}+\cdots+c_0a_n=0$ for every $n\geq0$. This is
exactly the vanishing of the coefficient of $T^{n+r}$ in $B_a(T)f_a(T)$, so
that product is a polynomial of degree less than $r$. Since $B_a(0)=1$, the
pair $(A_a,B_a)$ is a normalized polynomial fraction with Taylor series
$f_a$.
