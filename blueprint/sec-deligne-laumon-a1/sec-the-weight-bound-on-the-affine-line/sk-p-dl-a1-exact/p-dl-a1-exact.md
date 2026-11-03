+++
id = "p-dl-a1-exact"
kind = "theorem"
title = "Exactness at a fixed pure weight"
order = 4243
uses = ["d-real-setup", "def-weil-derived-direct-image", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-a1-local-boundary-duality", "lem-a1-spectrum-exact-sequence", "lem-fix-weil-operations", "lem-tw-dual-negation", "lem-wf-boundary-semicontinuity", "lem-wf-tate-twist-frobenius", "p-linear-spectra", "prop-weil-open-closed-recollement-adjunctions", "rem-dl-a1-conventions"]
tags = ["latex:proposition"]
lean = ["AlgebraicGeometry.shortExact_map_directImage"]
+++
In the conventions of [rem-dl-a1-conventions], let
$j:U_0\hookrightarrow C_0$ be a dense quasi-compact open immersion
into a smooth curve $C_0$ over $k_0$, that is, a $k_0$-scheme smooth of
relative dimension one (for instance $C_0=A_0$), with
closed complement $i:Z_0\hookrightarrow C_0$. Let
$0\to F_1\to F\to F_2\to0$ be a short exact sequence of lisse
$\Qlb$-Weil sheaves on $U_0$, with $F_1$ and $F_2$ punctually
$\iota$-pure of the same weight $w$ ([def-weil-punctual-weights]). Then the ordinary
middle extension of [def-wf-middle-extension] is exact on it: the
sequence of Weil sheaves on $C_0$

$$
0\longrightarrow j_*F_1\longrightarrow j_*F
\longrightarrow j_*F_2\longrightarrow0
$$

is exact.
