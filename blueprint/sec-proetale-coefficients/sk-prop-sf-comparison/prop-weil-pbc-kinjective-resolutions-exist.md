+++
id = "prop-weil-pbc-kinjective-resolutions-exist"
kind = "theorem"
title = "Existence of K-injective resolutions"
order = 1025
lean = ["AlgebraicGeometry.Etale.kInjectiveResolutions_exist"]
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "def-sp-kinjective-bridge"]
tags = ["latex:proposition"]
+++
Let $\mathcal A$ be a Grothendieck abelian coefficient category, for instance the
$R$-modules of [def-weil-pbc-derived-categories]. Every complex of $\mathcal A$-valued sheaves
on $T_{\Et}$ admits a K-injective resolution $K\to I(K)$, functorial in $K$; two K-injective
resolutions of one complex are chain-homotopy equivalent, and a bounded-below complex of
injective objects is K-injective.
