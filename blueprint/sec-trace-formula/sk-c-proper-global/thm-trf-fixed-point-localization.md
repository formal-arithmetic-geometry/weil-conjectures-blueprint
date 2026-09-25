+++
id = "thm-trf-fixed-point-localization"
kind = "theorem"
title = "Fixed-point localization"
order = 2513
uses = ["def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-correspondence", "def-trf-fixed-scheme", "def-trf-global-operator", "def-trf-integration", "def-trf-trace-class", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "lem-trf-contracting-trace-stalk", "lem-trf-localization-contracting", "lem-trf-localization-diagonal", "lem-trf-localization-normal-cone"]
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

## Proof

The identity is proved in three steps. First, the diagonal case is
[lem-trf-localization-diagonal]. Second, the normal-cone
reduction [lem-trf-localization-normal-cone] replaces the diagonal
by the graph of $c$ and deforms the graph section to the normal cone
of the diagonal without changing either side of the identity; this
reduction is the imported input SGA 5, Exposé III, 4.3–4.4 (see also
[Varshavsky, loc. cit.](https://arxiv.org/pdf/math/0505564),
2.1.1, and the deformation-to-the-normal-cone invariance
`thm:pur-dnc-invariance` of the smooth-purity chapter of this
manuscript). Third, after the reduction the correspondence is
contracting at the fixed points and the identity holds by
[lem-trf-localization-contracting]. The two imported inputs are
therefore exactly the normal-cone reduction and the normal-cone
computation of the trace map
([lem-trf-contracting-trace-stalk], Varshavsky, loc. cit.,
Theorem 2.1.2); everything else in the proof is proved in this chapter.
