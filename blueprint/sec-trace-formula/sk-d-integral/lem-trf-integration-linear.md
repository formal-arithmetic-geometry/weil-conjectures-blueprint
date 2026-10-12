+++
id = "lem-trf-integration-linear"
kind = "lemma"
title = "Linearity of the integration"
order = 2589
uses = ["def-compact-support-direct-image-detailed", "def-trf-admissibility", "def-trf-coefficient-conventions", "def-trf-dualizing-complex", "def-trf-integration", "def-weil-derived-direct-image", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties"]
+++
Fix the global finite-field datum
and the coefficient
conventions, $A=A_{E,n}$, $s=\Spec k$, and let $\beta$ be
separated finite type
and proper over $s$
with exceptionally admissible
structure morphism $a_\beta:\beta\to s$. Then the integration
$\int_\beta$ of [def-trf-integration] is $A$-linear: for
$\tau,\tau'\in\Hom_{D(\beta,A)}(A_\beta,\omega_{\beta,A})$ and
$a\in A$,

$$
\int_\beta(\tau+a\tau')=\int_\beta(\tau)+a\int_\beta(\tau').
$$
