+++
id = "det-cor-jacobian-torsion-kernel"
kind = "lemma"
title = "The $n$-torsion of an abelian variety over an algebraically closed field"
lean = ["AlgebraicGeometry.etale_torsionSubgroupScheme", "AlgebraicGeometry.finrankΓ_torsionSubgroupScheme", "AlgebraicGeometry.IsAbelianVariety.exists_overIso_sigma_torsionSubgroupScheme", "AlgebraicGeometry.torsionByEquiv", "AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.jacobian_compatibility"]
order = 876
uses = ["sk-thm-av-final", "sk-prop-av-isogeny", "sk-prop-av-prime-p-etale", "sk-prop-av-finite-etale-points", "sk-thm-picard-main"]
+++
Let $k$ be algebraically closed, let $A/k$ be an abelian variety of
dimension $g$, and let $n>0$ be invertible in $k$. Let
$A[n]=\ker([n]\colon A\to A)=A\times_{[n],A,e}\Spec k$.

1. $A[n]$ is a finite étale group scheme of rank $n^{2g}$ over $k$, and
   $A[n]\simeq\coprod_{r=1}^{n^{2g}}\Spec k$ as $k$-schemes.
2. $A[n](k)=A(k)[n]$, the kernel of multiplication by $n$ on the group
   $A(k)$, and this group has exactly $n^{2g}$ elements.
3. For every algebraically closed extension $K/k$ one has
   $A[n]\times_kK=A_K[n]$, and the natural map
   $$
   A[n](k)\longrightarrow A[n](K)=A_K[n](K),\qquad x\longmapsto x_K,
   $$
   is an isomorphism of groups.
4. Let $C/k$ be a smooth proper connected curve of genus $g$ and $A=J(C)$.
   Then the composite
   $$
   J(C)[n](k)\longrightarrow (J(C)\times_kK)[n](K)\xrightarrow{\ \sim\ }J(C_K)[n](K),
   $$
   whose second arrow is induced by the canonical identification
   $J(C)\times_kK=J(C_K)$ of [sk-thm-picard-main], is an isomorphism of
   groups. It is defined without any choice and is functorial in $K$.
