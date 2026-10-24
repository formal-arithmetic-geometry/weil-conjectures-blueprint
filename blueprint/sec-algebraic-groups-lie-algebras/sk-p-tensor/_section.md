+++
id = "sk-p-tensor"
kind = "proposition"
title = "Tensor determinant weights"
lean = ["Representation.exists_detWeight_eq_add_of_subquotient_tprod"]
order = 3774
uses = ["sk-d-weights", "sk-p-central", "sk-p-readout", "sk-r-linear-library"]
tags = ["sketch"]
+++
Let $V,V'$ be nonzero Weil representations with composition factors
$A_1,\ldots,A_t$ and $B_1,\ldots,B_u$. Assume that these factors, and every
simple factor of $V\otimes V'$, have finite geometric determinant. Then
every simple factor $Q$ of $V\otimes V'$ satisfies

$$
\dw_\iota(Q)=\dw_\iota(A_a)+\dw_\iota(B_b)
$$

for some $(a,b)$, and every such sum occurs.

*Complement.* The first assertion holds for every real weight character
$\lambda$ in place of $\lambda_\iota$, over any algebraically closed field
of characteristic zero, and for an arbitrary group $W$ with a homomorphism
$\deg\colon W\to\mathbf Z$ (not necessarily surjective) and an arbitrary
element $\gamma\in W$, determinant weights being taken at $\gamma$ and
finite geometric determinant referring to $\ker(\deg)$: every simple
subquotient $Q$ of $V\otimes V'$ with finite geometric determinant has
$\dw_\lambda(Q)=\dw_\lambda(A_a)+\dw_\lambda(B_b)$ for some $(a,b)$.
