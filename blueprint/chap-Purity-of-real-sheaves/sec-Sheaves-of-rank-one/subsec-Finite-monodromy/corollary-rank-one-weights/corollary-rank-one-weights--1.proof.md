+++
kind = "proof"
of = "corollary-rank-one-weights--1"
order = 1107002
uses = ["theorem-rank-one-sheaves-have-finite", "definition-weil-representation"]
+++
The proof of [theorem-rank-one-sheaves-have-finite] gives an integer
$N>0$ such that $\chi(g)^N=1$ for every $g\in\ker(\deg)$
(`AlgebraicGeometry.WeilGroup.exists_pow_eq_one_of_continuous`). For a
closed point $x$, put $d=\deg(x)>0$. The degree identities show that
$g_x=\operatorname{Frob}_x s^{-d}$ belongs to $\ker(\deg)$, and hence
$$
\chi(\operatorname{Frob}_x)=\chi(g_x)c^d.
$$
Since $\chi(g_x)^N=1$, its image under $\iota$ has absolute value one.
It follows that
$|\iota(\chi(\operatorname{Frob}_x))|=|\iota(c)|^d$.
Now $q_x=q^d$, so taking logarithms and cancelling $d$ gives the
claimed equality of weights.

To pass to a rank-one lisse representation $\rho$, take
$\chi=\det\rho$. This character is continuous on the geometric part
because the determinant is a polynomial in the continuous matrix
coefficients (`AlgebraicGeometry.WeilGroup.IsLisse.continuous_detCharacter`).
On a one-dimensional space every endomorphism is its determinant times
the identity (`LinearMap.eq_det_smul_id_of_finrank_eq_one`). Thus every
local Frobenius eigenvalue is $\det\rho(\operatorname{Frob}_x)$, and the
calculation gives punctual purity of weight
$2\log_q|\iota(\det\rho(s))|$.
