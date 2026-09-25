+++
id = "def-trf-local-term"
kind = "definition"
title = "Local term of a correspondence"
order = 2435
uses = ["def-trf-coefficient-conventions", "def-trf-fixed-scheme", "def-trf-integration", "def-trf-trace-class", "def-weil-scheme-morphism-properties", "prop-functor-package", "thm-trf-dualizing-complex-composition"]
+++
Fix the coefficient
conventions and let $c$ be an admissible correspondence with
fixed scheme $F=\operatorname{Fix}(c)$
of [def-trf-fixed-scheme]. Assume that $F$ is
proper over $s$ and has
finitely many open-and-closed components $\beta\in\pi_0(F)$ in the
sense of [def-trf-fixed-scheme]. For $\beta\in\pi_0(F)$, write
$j_\beta:\beta\hookrightarrow F$ for the inclusion of the open-and-closed
subscheme $\beta$, and define the restriction of the
trace class to $\beta$ by

$$
\operatorname{Tr}_c(u)|_\beta:
A_\beta\xrightarrow{\ \sim\ }
Lj_\beta^*A_F
\xrightarrow{Lj_\beta^*\operatorname{Tr}_c(u)}
Lj_\beta^*\omega_{F,A}
\longrightarrow\omega_{\beta,A},
$$

the last arrow being the canonical identification
$Lj_\beta^*\omega_{F,A}\cong Rj_\beta^!\omega_{F,A}\cong\omega_{\beta,A}$
of [thm-trf-dualizing-complex-composition], combined with the
equality $Rj_\beta^!\cong Lj_\beta^*$ for the open immersion $j_\beta$
(the purity clause of the six-operations package
[prop-functor-package], item (6), in relative dimension $0$). The
*local term* of $u$ at $\beta$ is

$$
\operatorname{LT}_\beta(u):=
\int_\beta\bigl(\operatorname{Tr}_c(u)|_\beta\bigr)\in A,
$$

the integral of [def-trf-integration].
