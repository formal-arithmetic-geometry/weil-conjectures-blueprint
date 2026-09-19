+++
id = "prop-zla-weight-stratum-rational"
kind = "theorem"
title = "Rationality of a weight stratum"
order = 1022
tags = ["latex:proposition"]
uses = ["def-zla-reversal", "def-zla-universal-purity", "def-zla-weight-stratum", "lem-zla-reversal-roots"]
+++
Let $R\in\mathbf Q[T]$ satisfy $R(0)=1$ and let $w$ be a real number. Then
$R_w\in\mathbf Q[T]$ divides $R$, both $R_w$ and the complementary factor
$R/R_w\in\mathbf Q[T]$ have constant coefficient $1$, and for every field $K$
of characteristic zero the reciprocal roots of $R_w$ in $K$, counted with
multiplicity, are exactly the reciprocal roots of $R$ in $K$ that are
universally pure of weight $w$. In particular, for $K=\mathbf C$, the
complex roots of $R_w$ are exactly the complex roots of $R$ whose inverses are
universally pure of weight $w$.

## Proof

Rationality is by construction: $R_w$ is a subproduct of the normalized
irreducible factorization of $R$ over $\mathbf Q$, so it lies in
$\mathbf Q[T]$, divides $R$, and its complementary factor is the product of
the remaining $F_j^{m_j}$, hence also lies in $\mathbf Q[T]$; both constant
coefficients are $1$ because every $F_j$ has constant coefficient $1$.

For the description of the roots it suffices to see that the purity condition
is constant on each irreducible factor. Let $F$ be one of the $F_j$ and let
$\alpha\in K^\times$ be a reciprocal root of $F$, that is $F(\alpha^{-1})=0$.
By [lem-zla-reversal-roots] this says $F^{\mathrm{rev}}(\alpha)=0$, and
$F^{\mathrm{rev}}$ is monic; it is irreducible in $\mathbf Q[U]$ because $F$
is irreducible with $F(0)\neq0$. So $\alpha$ is algebraic over $\mathbf Q$
with minimal polynomial $F^{\mathrm{rev}}$, whose complex roots are exactly
the inverses of the complex roots of $F$. Hence $\alpha$ is universally pure
of weight $w$ if and only if $|z|=q^{-w/2}$ for every complex root $z$ of $F$,
a condition on $F$ alone. So the reciprocal roots of $R$ in $K$ that are
universally pure of weight $w$ are exactly those contributed by the factors
$F_j$ with $j\in J_w$, with the multiplicities $m_j$ they have in $R$, and
these are the reciprocal roots of $R_w$.
