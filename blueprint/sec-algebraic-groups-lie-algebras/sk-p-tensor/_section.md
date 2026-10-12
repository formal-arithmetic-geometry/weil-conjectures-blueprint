+++
id = "sk-p-tensor"
kind = "proposition"
title = "Tensor-product weights"
order = 2898
uses = ["sk-d-linear", "sk-d-weights", "sk-i-restriction", "sk-r-linear-library"]
lean = ["Representation.exists_detWeight_eq_add_of_subquotient_tprod"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed of characteristic zero. Fix a real
weight character $\lambda$, a group $W$ with a homomorphism
$\deg:W\to\mathbf Z$, and an element $\gamma\in W$; determinant weights
are taken at $\gamma$, and finite geometric determinant refers to
$\ker(\deg)$. Let $V,E$ be finite-dimensional representations of $W$,
and assume that all simple subquotients of $V$ and of $E$ have finite
geometric determinant. For every simple subquotient $Q$ of $V\otimes E$
with finite geometric determinant there are simple subquotients $V_i$ of
$V$ and $E_j$ of $E$ such that

$$
\dw_\lambda(Q)=\dw_\lambda(V_i)+\dw_\lambda(E_j).
$$
