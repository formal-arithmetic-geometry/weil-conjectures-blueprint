+++
id = "sk-def-roots"
kind = "section"
title = "Reciprocal roots, weights and integrality"
order = 2858
lean = ["Polynomial.IsPureOfWeight", "Polynomial.IsUniversallyPureOfWeight", "Polynomial.alternatingNatDegreeSum", "shiftSpan"]
+++
*Definition (sketch).*

With $P_i\in\Z[T]$ the integral factor that [sk-thm-intfactors] produces
later put $b_i=\deg P_i$ and $P_i^{\#}(U)=U^{b_i}P_i(U^{-1})$. (Nothing here
depends on that theorem: wherever these notions are used before it, they are
applied to the $\ell$-adic factors $P_{i,\ell}$, whose roots in $\Qlb$ are
viewed in $\C$ through a fixed embedding $\iota:\Qlb\hookrightarrow\C$.) A
*reciprocal root* is a root $\alpha\in\overline{\Q}$ of $P_i^{\#}$, and
$\beta=\alpha^{-1}$ is the corresponding *ordinary root*. A reciprocal root
$\alpha$ is a *$q$-Weil number of weight $i$* if $|\tau(\alpha)|=q^{i/2}$ for every embedding
$\tau:\Q(\alpha)\hookrightarrow\C$.

For integers $q,w\ge0$, a polynomial $P\in\C[T]$ is *pure of weight $w$*
(for $q$) if $P(0)=1$ and every complex root $z$ of $P$ satisfies
$|z|=q^{-w/2}$, i.e. every reciprocal root has absolute value $q^{w/2}$. A
complex number $z$ is *universally pure of weight $w$* if it is algebraic
over $\Q$ and every complex root of its minimal polynomial over $\Q$ has
absolute value $q^{-w/2}$; a polynomial $P\in\C[T]$ is *universally pure of
weight $w$* if $P(0)=1$ and every complex root of $P$ is universally pure of
weight $w$.

The *Betti numbers* are $b_i=\deg P_i$, the *determinant constants* are
$D_i=(-1)^{b_i}[T^{b_i}]P_i(T)$, and the *Euler characteristic* of a family
$P_0,\dots,P_{n}$ of polynomials is the alternating degree sum
$\chi=\sum_{i=0}^{n}(-1)^{i}\deg P_i$.
For $C(T)=\sum_{n\ge0}c_nT^{n}\in K[[T]]$ the *Hankel matrix* is
$\mathcal H(C)=(c_{r+s})_{r,s\ge0}$ and its *Hankel rank* is the rank of
this (possibly infinite) matrix. The *shift span* of a sequence
$c=(c_n)_{n\ge0}$ in a ring $R$ is the $R$-submodule of $R^{\Z_{\ge0}}$
spanned by all its shifts $(c_{n+m})_{n\ge0}$, $m\ge0$ (the rows of
$\mathcal H(C)$). A *normalized integral presentation* is a
pair $A,B\in\Z[T]$ with $Z=A/B$, $A(0)=B(0)=1$ and $\gcd(A,B)=1$ in $\Q[T]$.
