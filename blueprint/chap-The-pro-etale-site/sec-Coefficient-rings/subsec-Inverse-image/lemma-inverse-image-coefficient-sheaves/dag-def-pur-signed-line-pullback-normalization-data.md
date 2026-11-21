+++
id = "dag-def-pur-signed-line-pullback-normalization-data"
kind = "dag-definition"
title = "Normalized signed pullback families and scalar squares"
name_showing = false
order = 187511
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "def-pur-signed-line-pullback-normalization-data"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLinePullbackNormalized", "SheafOfModules.SignedLineScalarPullbackSquare"]
uses = ["dag-def-pur-signed-line-scalar-normalization-data", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
For sites, commutative ring sheaves and a ringed-site pullback $F$ `def-weil-pbc-ringed-topos-morphism` `def-weil-sheaf-of-modules-category`, use the signed powers and scalar normalizations of [dag-def-pur-signed-line-scalar-normalization-data]. Given $p:F(P)\cong P\prime$ and $T_d:F(P^{[d]})\cong(P\prime)^{[d]}$, SignedLinePullbackNormalized means that $T_0$ is the unit map, $T_1=p$, positive powers satisfy the canonical tensor recursion, and negative powers satisfy the evaluation equation on all pulled local functional/section pairs. Given compatible coefficient maps $\alpha:R\to S$, $\beta:R\prime\to S\prime$, structural maps, and degree-one scalar and pullback module isomorphisms, SignedLineScalarPullbackSquare is equality of the two composites under the canonical scalar/pullback reassociation. It is tested on every local scalar-extension generator inserted into the pullback by the actual adjunction unit. These are predicates only; no flatness, invertibility of coefficient maps or existence of normalized isomorphisms is asserted.

(SHEAF DAG node `def-pur-signed-line-pullback-normalization-data`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: definition. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `lem-pur-signed-line-scalar-tensor-tower`, `sk-def-pbc-conventions`.
