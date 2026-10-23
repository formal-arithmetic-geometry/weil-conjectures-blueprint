+++
id = "lem-sf-pullback-tor-amplitude"
kind = "lemma"
title = "Pullback preserves finite Tor amplitude"
order = 1057
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_and_torAmplitudeIn_leftDerivedFunctor_upperStar_obj", "AlgebraicGeometry.ProEtale.constructibleFiniteTor_leftDerivedFunctor_upperStar_obj", "AlgebraicGeometry.ProEtale.torAmplitudeIn_leftDerivedUpperStar", "AlgebraicGeometry.ProEtale.upperStarPreservesFlat_moduleCat"]
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "lem-exc-constant-inverse-image-flat", "lem-sf-flat-model", "lem-weil-pbc-pullback-preserves-bounded-constructible"]
+++
Let $A$ be a finite commutative ring, let $f:X\to Y$ be a morphism of
schemes, and let $K\in D^b_c(Y,A)$ be a bounded constructible complex on
$Y_{\mathrm{proet}}$ of finite Tor amplitude in $[a,b]$. Then
$Lf^*K\in D^b_c(X,A)$ is bounded constructible and has finite Tor amplitude in
$[a,b]$. Consequently $Lf^*$ carries $D^b_{ctf}(Y,A)$ into $D^b_{ctf}(X,A)$.
