+++
id = "corollary-rank-one-weights--1"
kind = "corollary"
title = "Local weights of a rank-one character"
name_showing = false
order = 1107001
aliases = ["bp-r339-1"]
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_eq_of_continuous"]
uses = ["situation-weil", "definition-weights"]
+++
Let $U_0/\Fq$ be a smooth geometrically connected curve, put
$U=U_0\times_{\Fq}\Fbar$, and fix a prime $\ell\nmid q$ and an embedding
$\iota:\Qbarl\hookrightarrow\mathbf C$ as in [situation-weil]. Let $W$
be its Weil group, with chosen degree-one lift $s$. Assume that
$\ker(\deg)$ is identified with $\pi_1(U)$ compatibly with Frobenius.
Lean records this as `AlgebraicGeometry.WeilGroup.IsEtaleQuotient`,
supplied for the Weil group of the curve by
`AlgebraicGeometry.WeilGroup.isEtaleQuotient`.

Let $\chi:W\to\Qbarl^\times$ be a character whose restriction to
$\ker(\deg)$ is continuous, and put $c=\chi(s)$. For every closed point
$x$ of $U_0$, the local weight is
$$
\frac{2\log|\iota(\chi(\operatorname{Frob}_x))|}{\log q_x}
=\frac{2\log|\iota(c)|}{\log q}
=\lambda_\iota(c).
$$
