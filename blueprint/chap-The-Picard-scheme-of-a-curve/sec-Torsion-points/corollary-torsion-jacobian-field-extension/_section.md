+++
id = "corollary-torsion-jacobian-field-extension"
kind = "corollary"
title = "Torsion of the Jacobian and field extension"
order = 1558
lean = ["AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion", "AlgebraicGeometry.jacobian_compatibility", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.Scheme.ker_picDegreeMod"]
uses = ["definition-abelian-variety", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
