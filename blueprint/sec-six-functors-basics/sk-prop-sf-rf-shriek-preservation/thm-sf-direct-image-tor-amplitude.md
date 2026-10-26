+++
id = "thm-sf-direct-image-tor-amplitude"
kind = "theorem"
title = "Direct image and finite Tor amplitude"
order = 2389
uses = ["def-sf-uniform-direct-image-vanishing", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-pbc-direct-image", "def-weil-pbc-etale-site", "lem-exc-residue-tor-test", "lem-sf-flat-model", "lem-sf-projection-finite-constant", "sbc-def-coefficient-conventions", "thm-dg-finite-type-constructibility", "thm-sp-truncation-e2"]
+++
Fix an algebraically closed field $k$, a prime
$\ell\ne\operatorname{char}k$, $n\geq1$,
$A=A_{E,n}$, finite-type
$k$-schemes $X,Y$ and a separated finite-type morphism $f:X\to Y$.
Assume $\operatorname{UDV}(f,A;N)$ for an integer $N\geq0$, in the sense
of [def-sf-uniform-direct-image-vanishing]. Let $K$ be a bounded
constructible complex of $A$-modules on the small étale site $X_{\Et}$
with finite Tor amplitude in
$[a,b]$, the finite-Tor condition being the one of the étale clause of
[lem-sf-flat-model]. Then $Rf_*K$ is bounded constructible on
$Y_{\Et}$ and has finite Tor amplitude in $[a,b+N]$.
