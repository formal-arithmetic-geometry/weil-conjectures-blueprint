+++
id = "lem-exc-comparison-tor-interval"
kind = "lemma"
title = "Site comparison preserves and detects Tor intervals"
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_mapDerivedCategory_iff", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_mapDerivedCategory", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_of_mapDerivedCategory", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_mapDerivedCategory"]
order = 1058
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-site-comparison-morphism", "lem-exc-constant-inverse-image-flat", "prop-weil-pbc-site-comparison-finite-level", "thm-weil-pbc-site-comparison"]
+++
Let $A$ be a finite commutative ring, $T$ a scheme, and
$\nu_T:T_{\Proet}\to T_{\Et}$ the comparison morphism of sites. The derived
categories are the ordinary ones of [def-weil-pbc-derived-categories]. Let
$K\in D(T_{\Et},A)$ and let $a\leq b$ be integers.

1. If $K$ has Tor amplitude in $[a,b]$ on the étale site, then $\nu_T^*K$
has Tor amplitude in $[a,b]$ on the pro-étale site
([def-weil-finite-tor-amplitude]). If moreover $K$ is bounded constructible
[def-weil-pbc-constructible-complexes], then $\nu_T^*K$ is bounded
constructible on $T_{\Proet}$, so $\nu_T^*$ carries
$D^b_{\mathrm{ctf}}(T_{\Et},A)$ into $\Dctf(T,A)$.
2. Conversely, if $\nu_T^*K$ has Tor amplitude in $[a,b]$, then $K$ has Tor
amplitude in $[a,b]$ on the étale site.

In other words, $K$ has Tor amplitude in $[a,b]$ if and only if $\nu_T^*K$
has Tor amplitude in the same interval.
