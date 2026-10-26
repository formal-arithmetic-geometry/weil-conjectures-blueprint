+++
id = "cor-sf-direct-image-ctf-proetale"
kind = "theorem"
title = "The pro-étale direct image for all finite-Tor objects"
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_and_torAmplitudeIn_rightDerivedLowerStar"]
order = 2383
tags = ["latex:corollary"]
uses = ["cor-sf-direct-image-ctf-etale-origin", "cor-sf-direct-image-ctf-nonproper", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-exc-comparison-tor-interval", "lem-sf-etale-direct-image-vanishing", "lem-sf-proetale-constructible-origin", "prop-weil-pbc-comparison-direct-image", "thm-sf-direct-image-tor-amplitude"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$, $A=A_{E,n}$, and the algebraically closed field
$k=\overline{\mathbf F}_q$. Let $X,Y$ be finite-type $k$-schemes with
$\dim X\leq d$, let $f:X\to Y$ be a
separated finite-type
morphism, and let $K\in D^b_{ctf}(X_{\Proet},A)$ be a bounded
constructible complex of $A$-modules on the small pro-étale site with
finite Tor amplitude in $[a,b]$, both notions being the intrinsic ones of
[def-weil-finite-torsion-constructibility] and
[def-weil-finite-tor-amplitude]. Then $Rf_*K$ is bounded
constructible on $Y_{\Proet}$ and has finite Tor amplitude in
$[a,b+2d]$. That is, clause (iii) of the finite-Tor preservation summary holds at
the finite coefficient ring $A$ for *every* object of
$D^b_{ctf}(X_{\Proet},A)$, with no restriction to the objects of étale
origin.
