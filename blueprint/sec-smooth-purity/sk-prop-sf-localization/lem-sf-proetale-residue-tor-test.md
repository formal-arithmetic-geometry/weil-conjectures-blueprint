+++
id = "lem-sf-proetale-residue-tor-test"
kind = "lemma"
title = "The residue test on the pro-étale site"
lean = ["DerivedCategory.torAmplitudeIn_iff_homologyConcentratedIn_tensor_singleFunctor", "AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_iff_homologyConcentratedIn_tensor"]
order = 3216
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$ and $A=A_{E,n}$, put $\kappa=A/(\pi_E)$, let $T$ be a
scheme on which $\ell$ is invertible, and let
$K\in D^b_c(T_{\Proet},A)$ be a bounded constructible complex of
$A$-modules on the small pro-étale site in the intrinsic sense of
[def-weil-finite-torsion-constructibility]. Then $K$ has finite
Tor amplitude in $[a,b]$ if and
only if the derived tensor product $K\otimes_A^L\kappa_T$ with the
constant sheaf $\kappa_T$ has cohomology only in $[a,b]$.
