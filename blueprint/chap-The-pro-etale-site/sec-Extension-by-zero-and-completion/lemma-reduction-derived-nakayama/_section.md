+++
id = "lemma-reduction-derived-nakayama"
kind = "lemma"
title = "Reduction and derived Nakayama"
order = 210
lean = ["AlgebraicGeometry.ProEtale.derived_nakayama_first_reduction", "AlgebraicGeometry.ProEtale.isIso_of_derivedCompleteIntegers_of_isIso_derivedReduction_map", "AlgebraicGeometry.ProEtale.isZero_of_derivedCompleteIntegers_of_isZero_derivedReduction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-derived-adic-completeness"]
+++
Let $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$. Then $K_n$ is the cone of
$\pi_E^n:K\to K$. If $K$ is derived complete and $K_1=0$, then $K=0$.
Consequently a morphism between derived complete complexes is
an isomorphism whenever the induced map on $K_1$ is an isomorphism.
