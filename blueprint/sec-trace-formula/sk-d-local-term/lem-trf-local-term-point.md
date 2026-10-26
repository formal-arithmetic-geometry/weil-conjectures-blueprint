+++
id = "lem-trf-local-term-point"
kind = "lemma"
title = "The local term at a point component"
order = 3636
uses = ["def-trf-admissibility", "def-trf-coefficient-conventions", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-integration", "def-trf-local-term", "def-trf-trace-class", "def-weil-scheme-morphism-properties", "lem-trf-integration-linear", "prop-functor-package", "prop-trf-trace-class-unconditional"]
+++
Fix the coefficient
conventions, let $c$ be an
admissible correspondence with
fixed scheme $F$ over $s=\Spec k$ (not necessarily proper), and let
$\beta\subseteq F$ be an open-and-closed subscheme with
$\beta\simeq\Spec k$, finite etale over $s$ in relative dimension
$0$ (for instance a component $\beta\in\pi_0(F)$ of this form when
$F$ is proper with finitely many open-and-closed components, or the
reduced point component $B_{\bar x}$ of a point $\bar x$ of $F$). Then
the local term
$\operatorname{LT}_\beta(u)=\int_\beta(\operatorname{Tr}_c(u)|_\beta)$
of [def-trf-local-term], where
$\operatorname{Tr}_c(u)|_\beta=j_\beta^*\operatorname{Tr}_c(u)$, is
the element of $A$ corresponding to
the trace class
$\operatorname{Tr}_c(u)|_\beta$ under the canonical identification

$$
\operatorname{Hom}_{D(\beta,A)}\bigl(A_\beta,\omega_{\beta,A}\bigr)
\cong\operatorname{End}_{D(A)}(A)\cong A
$$

of the point case $\beta\simeq\Spec k$. In particular this computes
$\operatorname{LT}_{\bar x}(u)=\operatorname{LT}_{B_{\bar x}}(u)$ at
every point $\bar x$ with reduced open-and-closed point component
$B_{\bar x}$.
