+++
id = "theorem-rank-one-sheaves-have-finite--1"
kind = "theorem"
title = "A uniform exponent for the geometric character"
name_showing = false
order = 1104001
aliases = ["bp-r338-1"]
lean = ["AlgebraicGeometry.WeilGroup.exists_pow_eq_one_of_continuous"]
uses = ["situation-weil"]
+++
Let $U_0/k_0$ be a smooth geometrically connected curve over a finite
field, and let $\ell\ne\operatorname{char}(k_0)$ be prime. Let $W$ be a
Weil group for $U_0$, whose geometric subgroup $G=\ker(\deg)$ is
identified, compatibly with Frobenius, with $\pi_1(U)$ as in
[situation-weil]. This is the hypothesis
`AlgebraicGeometry.WeilGroup.IsEtaleQuotient` in Lean.
If $\chi:W\to\overline{\mathbf Q}_\ell^\times$ is a character whose
restriction to $G$ is continuous, then there is an integer $N>0$ such
that

$$
\chi(g)^N=1\qquad(g\in G).
$$
