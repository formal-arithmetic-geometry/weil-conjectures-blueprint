+++
kind  = "proof"
of    = "cor-pur-affine-space-purity"
+++
By induction on $d$: the case $d=0$ is the identity, and for
$d\geq1$ the composition law [prop-pur-affine-space-composition-law]
expresses $\gamma_{p_d,K}$ as the composite of the isomorphism
$\gamma_{p_{d-1},Rp_1^!K}$ (the induction hypothesis applied to the
$(d-1)$-fold affine space over the base-changed line) with the affine-line
purity isomorphism $\gamma_{p_1,K}$ of [thm-pur-affine-line-purity],
both conjugated by invertible reassociation isomorphisms; hence
$\gamma_{p_d,K}$ is an isomorphism.
