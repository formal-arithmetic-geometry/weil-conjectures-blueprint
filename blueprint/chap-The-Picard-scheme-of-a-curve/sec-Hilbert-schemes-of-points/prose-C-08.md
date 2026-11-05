+++
id = "prose-C-08"
kind = "hidden"
title = "Hilbert schemes of points (1)"
order = 1533
+++
On a smooth curve a finite subscheme of length $d$ is the same as an
effective divisor of degree $d$. These divisors are parametrized by the
Hilbert scheme of points $\operatorname{Hilb}^{d}_{C/k}$, which is the
symmetric power $C^{(d)}$. Iterated addition of points gives a finite
surjection $C^d\to \operatorname{Hilb}^{d}_{C/k}$, from which
$\operatorname{Hilb}^{d}_{C/k}$ inherits properness, irreducibility and
dimension $d$ (Theorem [theorem-hilbert-schemes-points-smooth-curve]).
For example, for $C=\mathbf P^1$, an effective divisor of degree $d$ is the zero set of
a binary form of degree $d$ up to scalars, and
$\operatorname{Hilb}^{d}_{C/k}=\mathbf P^d$.

A divisor $D$ gives the invertible sheaf $\mathcal O(D)$ with its
canonical section. Conversely, an invertible sheaf with a section up to
scalars gives a divisor. When $h^0=1$ the section is unique up to
scalars, and then the divisor is determined by the sheaf. In this way the
open part of $\operatorname{Hilb}^{g}_{C/k}$ where $h^0(\mathcal O(D))=1$
and $h^1=0$ becomes an open subfunctor of the Picard functor
(Proposition [proposition-divisors-degree-g-open-chart]).

For $d\geq0$, let $\operatorname{Hilb}^d_{C/k}$ be the
functor on $k$-schemes sending $T$ to the set of closed subschemes
$D\subset C_T$ that are finite locally free of rank $d$ over $T$.
