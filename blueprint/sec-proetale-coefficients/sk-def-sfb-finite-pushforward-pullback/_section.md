+++
id = "sk-def-sfb-finite-pushforward-pullback"
kind = "proposition"
title = "The topos and its functoriality"
order = 909
uses = ["def-weil-pbc-proetale-site", "sk-def-pe-site", "sk-lem-pe-weakly-etale-stability"]
lean = ["AlgebraicGeometry.Scheme.ProEt.topology", "CategoryTheory.GrothendieckTopology.subcanonical_of_full_of_faithful", "AlgebraicGeometry.Scheme.ProEt.isContinuous_overPullback"]
tags = ["sketch"]
+++
The coverings of [sk-def-pe-site] define a subcanonical site. Its category of sheaves
$\Sh(X_{\mathrm{proét}})$ is a Grothendieck topos. Every scheme morphism
$f:X\to Y$ induces a geometric morphism

$$
 f_{\mathrm{proét}}:\Sh(X_{\mathrm{proét}})\longrightarrow\Sh(Y_{\mathrm{proét}}),
 \qquad f^{-1}\dashv f_*.
$$

Here $f^{-1}:\Sh(Y_{\mathrm{proét}})\to\Sh(X_{\mathrm{proét}})$ preserves finite
limits and all colimits, and is exact on
abelian sheaves. These morphisms are compatible with composition.
