+++
id = "det-picard-main-geometry"
kind = "lemma"
title = "Smoothness, separatedness and properness of the degree components"
lean = ["AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor", "AlgebraicGeometry.GrpObj.isSeparated_hom", "AlgebraicGeometry.abelMapPresheaf", "AlgebraicGeometry.exists_surjective_of_representableBy_picardFunctorDegree_genus", "AlgebraicGeometry.theorem_of_the_base"]
order = 836
uses = ["thm-pc-picard-representable", "det-picard-main-degree", "det-picard-f-representable-chart", "thm-pc-hilb-curves", "lem-pc-twist", "lem-sc-riemann-roch"]
+++
Let $k$ be algebraically closed, $C/k$ a smooth proper connected curve of
genus $g$, $P\in C(k)$, and let $\underline{\operatorname{Pic}}_{C/k}=\coprod_d\underline{\operatorname{Pic}}^d_{C/k}$
be as in [det-picard-main-degree]. Then:

1. $\underline{\operatorname{Pic}}_{C/k}$ is locally of finite type,
smooth of pure dimension $g$ and separated over $k$;
1. the Abel map $\alpha:H_g\to\underline{\operatorname{Pic}}^g_{C/k}$,
$D\mapsto\cO_C(D)$ (normalized along $P$), is surjective;
1. every $\underline{\operatorname{Pic}}^d_{C/k}$ is a smooth proper
geometrically irreducible (in particular geometrically connected)
variety of dimension $g$.
