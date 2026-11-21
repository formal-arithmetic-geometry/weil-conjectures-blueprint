+++
id = "dag-lem-pur-transport-root-pull-step"
kind = "dag-lemma"
title = "Normalized finite root pullback commutes with consecutive power maps"
name_showing = false
order = 187540
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-transport-root-pull-step"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.PurityTransport.normalizedRootPull_step"]
uses = ["dag-def-pur-roots-of-unity-sheaf"]
+++
For every prime ell, morphism f:X -> Y and n >= 0, inverse image of the actual transition from ell^(n+1)-th roots to ell^n-th roots, followed by rootPull at level n, equals rootPull at level n+1 followed by the actual transition on X. The transition includes the equality transport ell^(n+1)=ell*ell^n. The root sheaves and their normalized inverse-image maps use [dag-def-pur-roots-of-unity-sheaf] and `def-pur-roots-of-unity-inverse-image`.

(SHEAF DAG node `lem-pur-transport-root-pull-step`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pur-roots-of-unity-inverse-image`.
