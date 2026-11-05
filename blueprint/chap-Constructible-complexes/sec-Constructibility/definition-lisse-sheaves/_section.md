+++
id = "definition-lisse-sheaves"
kind = "definition"
title = "Lisse sheaves"
order = 221
lean = ["AlgebraicGeometry.ProEtale.HasFiniteConstantLocalModel"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "sec-Derived-functors", "definition-constructible-sheaves"]
+++
Let $\Lambda$ be a commutative condensed ring. A $\Lambda_X$-module $M$ is
*lisse* if it satisfies the condition of
Definition [definition-constructible-sheaves](1) on $X$ itself, without
a stratification. A complex $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is *lisse*
if its cohomology sheaves are lisse.
