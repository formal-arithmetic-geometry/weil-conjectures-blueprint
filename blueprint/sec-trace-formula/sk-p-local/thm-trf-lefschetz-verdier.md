+++
id = "thm-trf-lefschetz-verdier"
kind = "theorem"
title = "Lefschetz–Verdier trace comparison"
order = 3647
uses = ["def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-correspondence", "def-trf-fixed-scheme", "def-trf-global-operator", "def-trf-local-term", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "lem-trf-global-operator-perfect", "lem-trf-integration-component-sum", "thm-trf-fixed-point-localization"]
+++
Fix the global finite-field datum
and the coefficient
conventions, $A=A_{E,n}$, $s=\Spec k$, and let $X$ be a
proper finite-type scheme.
Let $c=(c_1,c_2):C\to X\times_sX$ be an
admissible
cohomological correspondence with
$c_2$ proper and with
fixed scheme
$F=\operatorname{Fix}(c)$ proper over $s$ and with finitely many
open-and-closed components. Let $K\in D^b_{ctf}(X,A)$. Then

$$
\operatorname{tr}_A\bigl(T_c(u)\mid R\Gamma_c(X,K)\bigr)
=
\sum_{\beta\in\pi_0(F)}
\operatorname{LT}_\beta(u)
\quad\text{in }A,
$$

where $T_c(u)$ is the
global operator of
[def-trf-global-operator],
$\operatorname{tr}_A$ the
categorical trace, and the
$\operatorname{LT}_\beta(u)$ are the
local terms. Equivalently, the
categorical trace of the global operator equals the sum of the local
terms over the fixed points.
