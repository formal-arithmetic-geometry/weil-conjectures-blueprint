+++
id = "cor-sf-direct-image-ctf-etale-origin"
kind = "theorem"
title = "The pro-étale direct image for objects of étale origin"
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_and_torAmplitudeIn_rightDerivedLowerStar_mapDerivedCategory"]
order = 2382
tags = ["latex:corollary"]
uses = ["cor-sf-direct-image-ctf-nonproper", "def-weil-finite-tor-amplitude", "def-weil-pbc-proetale-modules", "def-weil-pbc-site-comparison-morphism", "lem-cbc-proetale-stalk-conservative", "lem-exc-comparison-tor-interval", "lem-weil-pbc-pullback-preserves-bounded-constructible", "prop-weil-pbc-comparison-direct-image"]
+++
In the setting of [cor-sf-direct-image-ctf-nonproper], let
$K\in D(X_{\mathrm{proet}},A)$ be of étale origin: $K\cong\nu_X^*K'$
for the comparison morphism
of sites and a bounded constructible complex $K'$ of $A$-modules on
$X_{\Et}$ of finite Tor amplitude
in $[a,b]$. Then the pro-étale direct image $Rf_*K$ is bounded
constructible on $Y_{\mathrm{proet}}$ and has finite Tor amplitude in
$[a,b+2d]$; that is, clause (iii) of the finite-Tor preservation summary holds at
the finite coefficient ring $A$ for such $K$.
