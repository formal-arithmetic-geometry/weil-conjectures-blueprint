+++
id = "lem-sf-comparison-tor-amplitude"
kind = "lemma"
title = "Finite Tor amplitude under the site comparison"
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_mapDerivedCategory", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_mapDerivedCategory", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_of_mapDerivedCategory"]
order = 2411
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-complexes", "def-weil-pbc-site-comparison-morphism", "lem-exc-constant-inverse-image-flat", "lem-sf-flat-model", "lem-sf-proetale-constructible-origin", "lem-sf-pullback-tor-amplitude", "prop-weil-pbc-proetale-constant-ring-map", "thm-weil-pbc-site-comparison"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$ and $A=A_{E,n}$, and let $T$ be a scheme on which $\ell$ is
invertible. Write $\nu_T:T_{\Proet}\to T_{\Et}$ for the comparison
morphism of sites.

1. **(i)** If $K'\in D^b_c(T_{\Et},A)$ has finite Tor amplitude in
$[a,b]$ on the étale site, in the sense of the étale clause of
[lem-sf-flat-model], then $\nu_T^*K'$ is bounded constructible on
$T_{\Proet}$ and has finite Tor amplitude in $[a,b]$ in the sense of
[def-weil-finite-tor-amplitude].
1. **(ii)** Conversely, if $K\in D^b_c(T_{\Proet},A)$ has finite Tor
amplitude in $[a,b]$ and $K\cong\nu_T^*K'$ for a bounded-below complex
$K'$ of $A$-module sheaves on $T_{\Et}$, then $K'$ has finite Tor
amplitude in $[a,b]$ on the étale site.
