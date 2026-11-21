+++
id = "dag-lem-pe-profinite-sections-finite-quotient"
kind = "dag-lemma"
title = "Continuous sections of a topological module sequence with finite discrete quotient"
name_showing = false
order = 210504
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--1"
dag_id = "lem-pe-profinite-sections-finite-quotient"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-det-def-sfb-condensed-ring", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $A,T_0,T_1,T_2$ be commutative topological rings, with continuous unital homomorphisms $A\to T_i$ giving their $A$-module structures. Let $f:T_0\to T_1$ and $g:T_1\to T_2$ be continuous $A$-linear maps. Suppose $f$ is injective, $g$ is surjective, $\operatorname{im}f=\ker g$, $T_2$ is finite and discrete, and the induced bijection $T_0\to\ker g$ is a homeomorphism for the subspace topology on $\ker g$. For every profinite set $S$, the sequence of pointwise $C(S,A)$-modules
$$0\to C(S,T_0)\xrightarrow{f\circ-}C(S,T_1)\xrightarrow{g\circ-}C(S,T_2)\to0$$
is short exact. The postcomposition maps consequently give a short exact sequence of condensed $\underline A$-module objects $0\to\underline{T_0}\to\underline{T_1}\to\underline{T_2}\to0$, using the continuous-function sheaves of `sk-def-sfb-condensed-ring` and module objects of `sk-def-sfb-module-objects`.

(SHEAF DAG node `lem-pe-profinite-sections-finite-quotient`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--1]. DAG kind: statement. Placed through `det-pe-derived-nakayama-resolution` (ancestor-1). DAG status: split. Lean names not on master: `Profinite.continuousSectionsModule`, `Profinite.continuousSections_finiteDiscrete_shortExact`. Statement dependencies not drawn: `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-weil-pbc-sheaf-tensor-closed`, `sk-def-sfb-module-objects`, `sk-def-sfb-ring-object`.
