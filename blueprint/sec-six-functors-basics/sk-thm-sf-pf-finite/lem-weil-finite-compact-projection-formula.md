+++
id = "lem-weil-finite-compact-projection-formula"
kind = "lemma"
title = "Finite-coefficient compact-support projection formula"
order = 2747
uses = ["def-cbc-exchange-map", "def-compact-support-direct-image-detailed", "def-exchange-projection", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-etale-sheaves", "def-weil-scheme-morphism-properties", "fix-lem-finite-tor-perfect", "lemma-weil-pbc-geometric-stalk-conservative", "thm-cbc-finite-level-proetale", "thm-cbc-finite-torsion", "thm-weil-pbc-site-comparison"]
+++
Fix the finite-field datum
and finite coefficient ring $A=A_{E,n}$.
Let $f:X\to Y$ be a
separated finite-type
morphism of finite-type $k$-schemes.
On the small etale sites, let
$K\in D^b_c(X_{\mathrm{et}},A)$ and
$L\in D^b_c(Y_{\mathrm{et}},A)$, in the
derived categories of
bounded complexes with constructible cohomology.
Assume $L$ has
finite Tor amplitude,
using the same tensor-vanishing definition on the etale site.
The projection transformation,
formed with the
derived tensor and pullback
and the compact-support
direct image, is an isomorphism:

$$
Rf_!K\otimes_A^L L
\xrightarrow{\ \sim\ } Rf_!(K\otimes_A^L Lf^*L).
$$

It is natural in $K,L$.
The same assertion holds for their pro-etale realizations equipped
with etale-origin witnesses,
where the representatives satisfy the displayed hypotheses.
