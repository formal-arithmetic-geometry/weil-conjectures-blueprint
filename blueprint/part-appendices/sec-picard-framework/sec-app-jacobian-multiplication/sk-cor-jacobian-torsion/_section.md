+++
id = "sk-cor-jacobian-torsion"
kind = "corollary"
title = "Torsion of the Jacobian and field extension"
order = 901
lean = ["AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion", "AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.jacobian_compatibility", "AlgebraicGeometry.Scheme.surjective_pow_picardZero", "AlgebraicGeometry.Scheme.ker_picDegreeMod"]
uses = ["sk-def-av", "sk-prop-av-isogeny", "sk-prop-av-tate-rank", "sk-thm-picard-main", "sk-cor-picard-degree", "sec-abelian-varieties"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed, let $C/k$ be a smooth proper
connected curve of genus $g$, and let $n>0$ be invertible in $k$.
Then there is a noncanonical isomorphism

$$
J(C)[n](k)\simeq(\mathbf Z/n\mathbf Z)^{2g}.
$$

For every algebraically closed
extension $k'/k$, the natural map

$$
J(C)[n](k)\longrightarrow J(C_{k'})[n](k')
$$

is an isomorphism. Multiplication by $n$ on $J(C)(k)$ is
surjective, and consequently

$$
\operatorname{Pic}(C)[n]=J(C)[n](k),
\qquad
\operatorname{Pic}(C)/n\operatorname{Pic}(C)
\xrightarrow[\deg]{\ \sim\ }\mathbf Z/n\mathbf Z.
$$
