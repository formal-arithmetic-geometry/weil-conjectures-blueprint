+++
id = "dag-def-pur-signed-line-ordinary-constraint-data"
kind = "dag-definition"
title = "Signed line ordinary constraint data"
name_showing = false
order = 187510
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "def-pur-signed-line-ordinary-constraint-data"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.OrdinaryLineConstraints"]
uses = ["dag-def-pur-signed-line-scalar-normalization-data"]
+++
Let A be a commutative ring sheaf, P an A-module sheaf, and P^$[d]$ its signed powers [dag-def-pur-signed-line-pullback-normalization-data]. OrdinaryLineConstraints(A,P,u,p,e) means: u: (- tensor P^$[0]$) ≅ Id sends x tensor r to r x; p_n: ((- tensor P^[n+1]) tensor P) ≅ (- tensor P^[n+2]) sends (x tensor y) tensor q to x tensor (y tensor q); and e_n: ((- tensor Hom(P^[n+1],A)) tensor P^[n+1]) → Id sends (x tensor phi) tensor y to phi(y)x. These identities hold on sections over every site object, for every module sheaf and every n≥0.

(SHEAF DAG node `def-pur-signed-line-ordinary-constraint-data`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: definition. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-sf-ringed-kflat-tensor-representative-data`, `lem-pur-signed-line-scalar-tensor-tower`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
