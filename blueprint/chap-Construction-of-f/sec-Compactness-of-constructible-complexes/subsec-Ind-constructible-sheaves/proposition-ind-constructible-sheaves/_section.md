+++
id = "proposition-ind-constructible-sheaves"
kind = "proposition"
title = "Ind-constructible sheaves"
order = 453
lean = ["AlgebraicGeometry.ProEtale.indHeart_fullFaithfulness", "AlgebraicGeometry.ProEtale.IsIndConstructibleHeart", "AlgebraicGeometry.ProEtale.CondensedRing.isIndConstructibleHeart_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isIndConstructibleHeart_padicAlgClRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves"]
+++
1. The functor $\operatorname{Ind}(\Cons(X,\Lambda))\to\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$
   sending a formal filtered colimit to the actual colimit is fully
   faithful, with essential image $\IndCons(X,\Lambda)$.
2. $\IndCons(X,\Lambda)$ is closed in $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ under
   filtered colimits, direct sums, kernels, cokernels and extensions. In
   particular it is a Grothendieck abelian category and its inclusion is
   exact.
