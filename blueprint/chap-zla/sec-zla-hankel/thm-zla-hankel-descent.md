+++
id = "thm-zla-hankel-descent"
kind = "theorem"
title = "Hankel rationality descent"
order = 1005
uses = ["def-zla-rational-germ", "def-zla-shift-span", "lem-zla-det-scalar-extension", "lem-zla-finite-coordinates", "lem-zla-germ-recurrence", "lem-zla-recurrence-shift-span", "prop-zla-shift-span-germ"]
+++
For every field extension $K\subseteq L$,

$$
K[[T]]\cap L(T)_0=K(T)_0
$$

inside $L[[T]]$. Explicitly, if $f\in K[[T]]$ becomes the Taylor series of a
normalized rational germ over $L$, then its coefficient sequence has finite
shift span over $K$, and the characteristic polynomial of the shift on that
span constructs a normalized rational germ over $K$ whose Taylor series is
$f$.

## Proof

Let $a$ be the coefficient sequence of $f$, which lies in $K^{\mathbf N}$. A
normalized rational germ over $L$ with Taylor series $f$ supplies an eventual
recurrence for $a$ over $L$ ([lem-zla-germ-recurrence]), hence a finite
bound on $\dim_L\operatorname{Sh}_L(a)$
([lem-zla-recurrence-shift-span]). Any $K$-independent family of shifts
of $a$ has a nonvanishing finite coordinate determinant
([lem-zla-finite-coordinates]) and therefore stays independent over $L$
([lem-zla-det-scalar-extension]); so $\dim_K\operatorname{Sh}_K(a)$ is
bounded by the same number. Now [prop-zla-shift-span-germ] over $K$
produces $A_a,B_a\in K[T]$ with $B_a(0)=1$ and
$f=\tau_K[A_a,B_a]$. The reverse inclusion is trivial.
