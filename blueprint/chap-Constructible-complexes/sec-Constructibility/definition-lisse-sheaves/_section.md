+++
id = "definition-lisse-sheaves"
kind = "definition"
title = "Lisse sheaves"
order = 221
lean = ["AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented", "AlgebraicGeometry.ProEtale.IsLisseCoefficientModule"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-constructible-sheaves"]
+++
Let $\Lambda$ be a commutative condensed ring. A $\Lambda_X$-module $M$ is
*lisse* if it satisfies the condition of
Definition [definition-constructible-sheaves](1) on $X$ itself, without
a stratification. A complex $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is *lisse*
if its cohomology sheaves are lisse.
