+++
id = "lem-trf-integration-component-sum"
kind = "lemma"
title = "Integration splits over the open–closed components"
order = 2686
uses = ["def-trf-coefficient-conventions", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-integration", "def-trf-local-term", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-functor-package", "thm-trf-dualizing-complex-composition"]
+++
Fix the coefficient
conventions, $A=A_{E,n}$, $s=\Spec k$, and let $T$ be a
separated finite-type scheme over $s$ which is a finite disjoint union

$$
T=\coprod_{\beta\in B}\beta
$$

of open-and-closed subschemes $j_\beta:\beta\hookrightarrow T$, each
proper over $s$. Then $T$ is proper over $s$. For
$\tau:A_T\to\omega_{T,A}$ and $\beta\in B$ define the *restriction*

$$
\tau|_\beta:
A_\beta\xrightarrow{\ \sim\ }Lj_\beta^*A_T
\xrightarrow{Lj_\beta^*\tau}Lj_\beta^*\omega_{T,A}
\cong Rj_\beta^!\omega_{T,A}\cong\omega_{\beta,A},
$$

using the equality $Rj_\beta^!\cong Lj_\beta^*$ for the open immersion
$j_\beta$ ([prop-functor-package], item (6), relative dimension $0$)
and the identification of [thm-trf-dualizing-complex-composition]
(this restriction makes sense without any properness). Then

$$
\int_T\tau=\sum_{\beta\in B}\int_\beta(\tau|_\beta),
$$

where $\int_T,\int_\beta$ are the integrations of
[def-trf-integration] and $\omega_{T,A}$ is the
dualizing complex of
[def-trf-dualizing-complex]; for $B=\emptyset$ both sides are $0$.
In particular, if $c$ is an admissible correspondence whose fixed
scheme $F=\operatorname{Fix}(c)$ of [def-trf-fixed-scheme] has
finitely many open-and-closed components $\beta\in\pi_0(F)$, each
proper over $s$, then $F$ is proper and
$\int_F\tau=\sum_{\beta\in\pi_0(F)}\int_\beta(\tau|_\beta)$, the
restrictions being those of [def-trf-local-term].
