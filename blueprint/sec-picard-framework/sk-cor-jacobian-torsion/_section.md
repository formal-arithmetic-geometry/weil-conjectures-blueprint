+++
id = "sk-cor-jacobian-torsion"
kind = "corollary"
title = "Jacobian torsion and geometric extension"
order = 841
lean = ["AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion", "AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.jacobian_compatibility", "AlgebraicGeometry.Scheme.surjective_pow_picardZero", "AlgebraicGeometry.Scheme.ker_picDegreeMod"]
uses = ["sk-def-av", "sk-prop-av-isogeny", "sk-prop-av-tate-rank", "sk-thm-picard-main", "sk-cor-picard-degree", "sec-abelian-varieties"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed, let $C/k$ be a smooth proper connected
curve of genus $g$, and let $n>0$ be invertible in $k$. Then

$$
J(C)[n](k)\simeq(\Z/n\Z)^{2g}.
$$

This isomorphism is not canonical. For every algebraically closed
extension $K/k$, the natural map

$$
J(C)[n](k)\longrightarrow J(C_K)[n](K)
$$

is a canonical isomorphism. Multiplication by $n$ on $J(C)(k)$ is
surjective, and consequently

$$
\operatorname{Pic}(C)[n]=J(C)[n](k),
\qquad
\operatorname{Pic}(C)/n\operatorname{Pic}(C)\xrightarrow[\ \deg\ ]{\sim}\Z/n\Z.
$$
