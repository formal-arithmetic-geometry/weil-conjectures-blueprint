+++
id = "thm-trf-fixed-point-localization"
kind = "theorem"
title = "Fixed-point localization"
order = 3808
uses = ["def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-coefficient-pushforward", "def-trf-correspondence", "def-trf-fixed-scheme", "def-trf-global-operator", "def-trf-integration", "def-trf-trace-class", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "fix-prop-adjunctions", "lem-trf-integration-as-pushforward", "lem-trf-trace-class-diagonal-pairing", "prop-functor-package", "prop-trf-compact-support-perfectness", "prop-trf-pairing-point-normalization", "thm-sf-comp-composition", "thm-sf-preservation-class", "thm-trf-trace-proper-compatibility"]
+++
Fix the global finite-field datum
and the coefficient
conventions, $A=A_{E,n}$, put $s=\Spec k$, and let $X$ be a
proper finite-type scheme.
Let $c=(c_1,c_2):C\to X\times_sX$ be an
admissible
cohomological correspondence with
$c_2$ proper and with
fixed scheme
$F=\operatorname{Fix}(c)$ proper over $s$. For
$K\in D^b_{ctf}(X,A)$, the
categorical trace of the
global operator equals the integral of
the trace class:

$$
\operatorname{tr}_A\bigl(T_c(u)\mid R\Gamma_c(X,K)\bigr)
=\int_F\operatorname{Tr}_c(u)
\quad\text{in }A,
$$

where $T_c(u)$ is the global operator of
[def-trf-global-operator], $\operatorname{Tr}_c(u)$ the trace class
of [def-trf-trace-class], and $\int_F$ the integration of
[def-trf-integration].
