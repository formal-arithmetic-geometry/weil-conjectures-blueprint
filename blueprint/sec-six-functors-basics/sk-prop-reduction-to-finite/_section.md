+++
id = "sk-prop-reduction-to-finite"
kind = "proposition"
title = "Isomorphisms reduce to finite coefficients"
order = 2861
uses = ["sk-def-sfb-constructible", "sk-prop-scalar-six"]
tags = ["sketch"]
+++
Many later theorems say that a canonical map is an isomorphism. They are proved with finite
coefficients and extended to all admissible rings by the same three steps: reduction modulo
$\pi_E$ and derived Nakayama for $\mathcal O_E$, inverting $\ell$ on integral models for $E$, and
descent to a finite extension for $\Qlb$. We state the argument once.

**Proposition.** For each admissible $\Lambda$ let
$F_\Lambda,G_\Lambda\colon\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$ ([sk-def-sfb-constructible]) be exact functors and
$\theta_\Lambda\colon F_\Lambda\to G_\Lambda$ a natural transformation of exact functors. Assume that
for each coefficient map $\Lambda\to\Lambda'$ of [sk-prop-scalar-six] there are isomorphisms
$F_\Lambda(K)\otimes\Lambda'\simeq F_{\Lambda'}(K\otimes\Lambda')$ and
$G_\Lambda(K)\otimes\Lambda'\simeq G_{\Lambda'}(K\otimes\Lambda')$ carrying
$\theta_\Lambda(K)\otimes\Lambda'$ to $\theta_{\Lambda'}(K\otimes\Lambda')$. This holds, by
[sk-prop-scalar-six], whenever $F$, $G$ and $\theta$ are built from the six operations, their
units and counits and base change maps, covariantly in $K$. If $\theta_A(K)$ is an isomorphism
for every finite ring $A$ and every $K\in\Dctf(X,A)$, then $\theta_\Lambda(K)$ is an isomorphism
for every admissible $\Lambda$ and every $K\in\Dctf(X,\Lambda)$.

The proposition applies also to some contravariant constructions after a rewriting: for
instance the double-dual map $K\to\mathbb D\mathbb DK$ is a natural transformation of covariant
exact functors. What does not reduce in this way is the construction of an adjoint or of a
map: the cycle class of the diagonal and the adjunction $Rf_!\dashv f^*(d)[2d]$ for smooth $f$
must be built as single morphisms with $\mathcal O_E$-coefficients (in the sections on the
exceptional inverse image and on smooth purity with $\ell$-adic coefficients), and a trace with
values in $\Lambda$ is not a map of complexes.
