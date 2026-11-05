+++
id = "corollary-functional-equation--10"
kind = "corollary"
title = "Functional equation as a correspondence of roots"
order = 1044011
aliases = ["bp-r320-10"]
lean = ["TraceDatum.roots_map_charpolyRev_rev", "TraceDatum.weilFunctionalEquation_of_pairing"]
uses = []
+++
The sign form is bypassed by the Lean route; its functional equation is the
following correspondence of roots.

Let $K$ be a field of characteristic zero, let $q,d\in\mathbf N$ with $q>1$,
and fix an embedding $\iota:K\to\mathbf C$. Let $V_i,F_i,N_n$ be a trace datum
of length $2d$: the $V_i$, for $0\le i\le2d$, are finite-dimensional
$K$-vector spaces with endomorphisms $F_i$, and the integers $N_n$ satisfy

$$
N_n=\sum_{i=0}^{2d}(-1)^i\operatorname{Tr}(F_i^n)\qquad(n\ge1).
$$

Suppose that there are perfect pairings $p_i:V_i\times V_{2d-i}\to K$ with
$p_i(F_iv,F_{2d-i}w)=q^d p_i(v,w)$. Put $P_i(T)=\det(1-TF_i)$, and write
$\iota(P_i)$ for coefficientwise extension to $\mathbf C[T]$. Then

$$
\operatorname{roots}(\iota(P_{2d-i}))
=\left[\frac1{q^d z}:z\in\operatorname{roots}(\iota(P_i))\right],
$$

as multisets, so multiplicities are retained. If $Q_i\in\mathbf Z[T]$ is any
family whose images in $\mathbf C[T]$ are $\iota(P_i)$, then the same root
identity holds for the $Q_i$. This is the predicate
`AlgebraicGeometry.WeilFunctionalEquation`.
