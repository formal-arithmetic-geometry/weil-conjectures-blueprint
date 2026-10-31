+++
id = "sk-def-sfb-finite-pushforward-pullback"
kind = "proposition"
title = "The topos and its functoriality"
order = 35
lean = ["AlgebraicGeometry.Scheme.ProEt.topology", "CategoryTheory.GrothendieckTopology.subcanonical_of_full_of_faithful", "AlgebraicGeometry.Scheme.ProEt.isContinuous_overPullback"]
uses = ["def-weil-pbc-proetale-site", "sk-def-pe-site", "sk-lem-pe-weakly-etale-stability"]
tags = ["sketch"]
+++
The above coverings define a subcanonical site. Its category of sheaves
$\Sh(X_{\mathrm{pro}\acute{e}t})$ is a Grothendieck topos. Every scheme morphism
$f:X\to Y$ induces a geometric morphism

$$
f_{\mathrm{pro}\acute{e}t}:\Sh(X_{\mathrm{pro}\acute{e}t})\longrightarrow\Sh(Y_{\mathrm{pro}\acute{e}t}),
\qquad f^{-1}\dashv f_*.
$$

Here $f^{-1}:\Sh(Y_{\mathrm{pro}\acute{e}t})\to\Sh(X_{\mathrm{pro}\acute{e}t})$ preserves finite
limits and all colimits, and is exact on
abelian sheaves. These morphisms are compatible with composition.
