+++
id = "cor-sc-hilbert-90-field"
kind = "theorem"
title = "Hilbert 90 for a field"
order = 1352
uses = ["def-sc-gm-torsor", "lem-sc-torsor-h1"]
lean = ["AlgebraicGeometry.Scheme.subsingleton_cohomologicalPicardGroup_of_field", "AlgebraicGeometry.Scheme.surjective_app_of_shortExact_gmSheaf"]
+++
Let $K$ be a field. Then $H^1(\operatorname{Spec}K_{\Et},\mathbf G_m)=0$.
Equivalently, every $\mathbf G_m$-torsor ([def-sc-gm-torsor]) on
$\operatorname{Spec}K_{\Et}$ is trivial: for every short exact sequence
$0\to\mathbf G_m\to E\to Q\to0$ of abelian sheaves on
$\operatorname{Spec}K_{\Et}$, the map $\Gamma(E)\to\Gamma(Q)$ is surjective.
