+++
id = "dag-def-weil-pbc-ind-etale-algebra"
kind = "dag-definition"
title = "Ind-etale and ind-Zariski algebras"
name_showing = false
order = 27501
tags = ["sheaf-dag"]
split_from = "definition-ind-etale-pro-etale-weakly--1"
dag_id = "def-weil-pbc-ind-etale-algebra"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["Algebra.IndEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.weaklyEtale_SpecMap_algebraMap_iff", "RingHom.IndEtaleAcrossUniverses"]
+++
Let $A$ be a commutative ring and let $B$ be an $A$-algebra. The
$A$-algebra $B$ is *ind-etale* if it is a filtered colimit of etale
$A$-algebras of finite presentation `def-weil-pbc-scheme-conventions`. It is
*ind-Zariski* if such a presentation can be chosen with terms finite products
of localizations $A_f$. The corresponding affine scheme $\operatorname{Spec}B$
is an inverse limit of affine etale schemes, with affine transition maps. The
ring map $A\to B$ is *weakly etale* when the induced map
$\operatorname{Spec}B\to\operatorname{Spec}A$ is weakly etale in
`def-weil-pbc-scheme-conventions`; equivalently, $B$ is flat as an $A$-module
and is flat as a module over $B\otimes_A B$ via the multiplication map
$B\otimes_A B\to B$.

(SHEAF DAG node `def-weil-pbc-ind-etale-algebra`; machine-alignment layer.) Split from [definition-ind-etale-pro-etale-weakly--1]. DAG kind: definition. DAG status: split. Lean names not on master: `Algebra.WeaklyEtale`. Statement dependencies not drawn: `def-weil-pbc-scheme-conventions`.
