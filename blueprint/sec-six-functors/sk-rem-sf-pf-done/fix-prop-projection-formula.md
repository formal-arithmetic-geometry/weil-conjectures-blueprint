+++
id = "fix-prop-projection-formula"
kind = "theorem"
title = "Compact-support projection formula for all admissible coefficient rings"
order = 2453
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-exchange-projection", "def-fix-six-functor-datum", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "def-wf-tensor-product", "def-weil-weil-sheaf-complex", "lem-fix-weil-operations", "lem-weil-finite-compact-projection-formula", "prop-sf-pf-coherence", "prop-sf-pf-reduction", "thm-sf-pf-adic", "thm-sf-pf-field", "thm-sf-pf-proetale", "thm-sf-comp-composition"]
+++
In the six-functor datum of
[def-fix-six-functor-datum], let $f:X\to Y$ be
separated of finite
type, let $K\in D^b_c(X,\Lambda)$ and
$L\in D^b_{ctf}(Y,\Lambda)$, using the
finite-Tor subcategory.
The
projection transformation, built from the
derived tensor and pullback
and the compact-support direct image of
[def-compact-support-direct-image-detailed],
is then an isomorphism for every admissible coefficient ring:

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L_{\Lambda}L
\xrightarrow{\ \sim\ }Rf_!\bigl(K\otimes^L_{\Lambda}Lf^*L\bigr),
$$

natural in $K$ and $L$, compatible with the composition law of
[thm-sf-comp-composition] (associativity pentagon), with the compactification comparisons, with
finite reduction on the stated finite-Tor domains and scalar extension,
and with the identification
$Rf_!\cong Rf_*$ for proper $f$; for $\Lambda=E,\Qlb$ it is compatible
with Weil structures: for Weil complexes in the sense of
[def-weil-weil-sheaf-complex], with the tensor Frobenius of
[def-wf-tensor-product], it is a morphism of Weil complexes
([lem-fix-weil-operations]). A projection formula for the
derived direct image is asserted
only in the proper case, where it is this same statement via
$Rf_!\cong Rf_*$.
