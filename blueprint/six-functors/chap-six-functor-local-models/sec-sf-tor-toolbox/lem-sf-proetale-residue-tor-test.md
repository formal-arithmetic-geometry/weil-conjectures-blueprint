+++
id = "lem-sf-proetale-residue-tor-test"
kind = "lemma"
title = "The residue test on the pro-étale site"
order = 3432
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-complexes", "def-weil-pbc-site-comparison-morphism", "lem-exc-residue-tor-test", "lem-sf-comparison-tor-amplitude", "lem-sf-proetale-constructible-origin", "prop-weil-pbc-proetale-constant-ring-map", "thm-weil-pbc-site-comparison"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$ and $A=A_{E,n}$, put $\kappa=A/(\varpi_E)$, let $T$ be a
scheme on which $\ell$ is invertible, and let
$K\in D^b_c(T_{\Proet},A)$ be a bounded constructible complex of
$A$-modules on the small pro-étale site in the intrinsic sense of
[def-weil-finite-torsion-constructibility]. Then $K$ has finite
Tor amplitude in $[a,b]$ if and
only if the derived tensor product $K\otimes_A^L\kappa_T$ with the
constant sheaf $\kappa_T$ has cohomology only in $[a,b]$.

## Proof

One direction is the definition [def-weil-finite-tor-amplitude], the
constant sheaf $\kappa_T$ being a sheaf of $A$-modules placed in degree
zero. For the converse, apply
[lem-sf-proetale-constructible-origin]: there is a bounded complex
$K'$ with constructible cohomology on $T_{\Et}$ and an isomorphism
$K\cong\nu_T^*K'$. The comparison pullback of the constant coefficient
sheaf is the constant coefficient sheaf, by
[prop-weil-pbc-proetale-constant-ring-map], so

$$
\nu_T^*\bigl(K'\otimes_A^L\kappa_T\bigr)\cong K\otimes_A^L\kappa_T
$$

has cohomology only in $[a,b]$ by hypothesis; by
[thm-weil-pbc-site-comparison] the pullback reflects the vanishing of
cohomology, so $K'\otimes_A^L\kappa_T$ has cohomology only in $[a,b]$.
The étale residue test [lem-exc-residue-tor-test] applies to the
bounded complex $K'$ with constructible cohomology and to the residue
field $\kappa=A/(\varpi_E)$, and gives finite Tor amplitude of $K'$ in
$[a,b]$ on the étale site.
[lem-sf-comparison-tor-amplitude] then transfers that amplitude to
$K\cong\nu_T^*K'$.
