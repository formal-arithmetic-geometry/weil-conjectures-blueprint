+++
id = "lem-pc-flf-properties"
kind = "lemma"
title = "The module $f_*\\mathcal{O}_X$ of a finite locally free morphism"
lean = ["AlgebraicGeometry.Scheme.Hom.isPushout_app_evaluation_fiber", "AlgebraicGeometry.Scheme.Hom.exists_ringEquiv_tensorProduct_fiber", "AlgebraicGeometry.Scheme.Hom.isLocalization_stalk_pushforward", "AlgebraicGeometry.Scheme.Hom.exists_ringEquiv_stalk_pushforward_tensorProduct_fiber", "AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOfRank_pushforward_unit"]
order = 763
uses = ["def-pc-base-change", "def-pc-finite-locally-free", "def-pc-morphism-conventions"]
+++
Let $f:X\to S$ be a morphism
finite locally free of degree
$d$. Then $f_*\mathcal{O}_X$ is a locally free $\mathcal{O}_S$-module of rank $d$,
and for every $s\in S$ the canonical map
$(f_*\mathcal{O}_X)_s\otimes_{\mathcal{O}_{S,s}}\kappa(s)\to \Gamma(X_s,\mathcal{O}_{X_s})$ is an isomorphism.
