+++
kind  = "proof"
of    = "lem-sfb-dc-tensor-preserves"
uses = ["sk-lem-integral-models", "sk-prop-integral-criterion", "sk-cor-coefficient-heart-ii", "sk-thm-sfb-qlbar-two-colimit"]
+++
Let first $\Lambda=\underline{\cO}_E$. This is part (3) of [sk-lem-integral-models]. In terms of
the integral criterion [sk-prop-integral-criterion]: on the strata of a stratification for $K$,
$K$ is pro-étale locally a bounded complex of finite free modules, so tensoring with it preserves
derived completeness, and the reduction is

$$
(K\otimes^{\mathrm L}L)/\pi_E\cong(K/\pi_E)\otimes^{\mathrm L}_{\cO_E/\pi_E}(L/\pi_E),
$$

a derived tensor product of bounded constructible étale complexes over the field
$\cO_E/\pi_E$, hence bounded with constructible cohomology; the projection formula for extension
by zero along the strata globalizes this.

For $\Lambda=\underline E$, the tensor product is exact in each variable and $\Dbc(X,E)$ is
triangulated ([sk-cor-coefficient-heart-ii]), so by part (4) of [sk-lem-integral-models] it
suffices to treat $K=K_0[1/\ell]$ and $L=L_0[1/\ell]$ with $K_0,L_0\in\Dbc(X,\cO_E)$. Since
inverting $\ell$ is extension of scalars along the flat map $\cO_{E,X}\to E_X$, which is
monoidal, $K\otimes^{\mathrm L}_{E_X}L\simeq(K_0\otimes^{\mathrm L}_{\cO_{E,X}}L_0)[1/\ell]$, and this
lies in $\Dbc(X,E)$ by the integral case. For $\Lambda=\underline{\Qlb}$, descend $K$ and $L$ to a
common finite $E$ ([sk-thm-sfb-qlbar-two-colimit]); extension of scalars to $\Qlb$ is monoidal and
preserves bounded constructible complexes, so the case $\underline E$ applies.
