+++
id = "lem-wf-tensor-weil"
kind = "lemma"
title = "Tensor product of Weil complexes"
order = 3794
uses = ["def-wf-tensor-product", "def-weil-weil-sheaf-complex"]
+++
Let $\Lambda\in\{E,\Qlb\}$. The construction of [def-wf-tensor-product] defines a
bifunctor on Weil complexes with underlying complexes in $\Dbc(X,\Lambda)$,

$$
(K,\varphi_K)\otimes^{\mathbf L}(L,\varphi_L)=
\bigl(K\otimes^{\mathbf L}_{\Lambda_X}L,\ \varphi_K\otimes\varphi_L\bigr),
$$

lying over the exact bifunctor $-\otimes^{\mathbf L}_{\Lambda_X}-$ on $\Dbc(X,\Lambda)$.
