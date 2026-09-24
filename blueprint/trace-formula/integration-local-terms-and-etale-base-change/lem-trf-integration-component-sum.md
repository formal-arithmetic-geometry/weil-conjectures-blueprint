+++
id = "lem-trf-integration-component-sum"
kind = "lemma"
title = "Integration splits over the open–closed components"
order = 3897
uses = ["def-trf-coefficient-conventions", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-integration", "def-trf-local-term", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-functor-package", "thm-trf-dualizing-complex-composition"]
+++
Fix the coefficient
conventions, $A=A_{E,n}$, and let $c$ be an admissible
correspondence whose fixed scheme
$F=\operatorname{Fix}(c)$ of [def-trf-fixed-scheme] is
proper over $s$ and has
finitely many open-and-closed components $\beta\in\pi_0(F)$. For every
$\tau:A_F\to\omega_{F,A}$,

$$
\int_F\tau=\sum_{\beta\in\pi_0(F)}\int_\beta(\tau|_\beta),
$$

where $\int_F,\int_\beta$ are the integrations of
[def-trf-integration], $\omega_{F,A}$ is the
dualizing complex of
[def-trf-dualizing-complex], and the restrictions $\tau|_\beta$
are defined as in [def-trf-local-term].

## Proof

The pro-etale site of a disjoint union of schemes is the disjoint union of
the sites ([def-weil-pbc-proetale-site]), so
$D(F,A)\cong\prod_{\beta}D(\beta,A)$ and the six operations decompose
accordingly: in particular
$R\Gamma(F,-)\cong\prod_\beta R\Gamma(\beta,-)$ (the product is a direct
sum over the finitely many components of [def-trf-fixed-scheme]),
the unit $A\to R\Gamma(F,A_F)$ of [def-trf-integration] is the
tuple of the units of the components, and the counit
$\varepsilon_{a_F}$ is the tuple of the counits
$\varepsilon_{a_\beta}$ (the adjunctions of [def-trf-integration]
decompose with the products, by the compatibility of the six-functor
formalism with disjoint unions). The restriction $\tau|_\beta$ of
[def-trf-local-term] is $Lj_\beta^*\tau$ followed by the
identification $Lj_\beta^*\omega_{F,A}\cong\omega_{\beta,A}$ of
[thm-trf-dualizing-complex-composition] combined with the equality
$Rj_\beta^!\cong Lj_\beta^*$ of [prop-functor-package] (item (6),
relative dimension $0$). Hence the composite displayed in
[def-trf-integration] for $\int_F\tau$ is the tuple of the
composites defining the $\int_\beta(\tau|_\beta)$, which is the
displayed identity; the terms are indexed by the finite set
$\pi_0(F)$ of [def-trf-fixed-scheme], and the identification of
$\omega_{F,A}$ with the tuple of the $\omega_{\beta,A}$ of
[def-trf-dualizing-complex] is the one used above.
