+++
id = "dag-lem-pur-signed-line-module-action-presentations"
kind = "dag-lemma"
title = "Signed line module action presentations"
name_showing = false
order = 187530
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-module-action-presentations"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLinePullbackConstruction.inverseImageAction_of_presentations"]
uses = ["dag-def-pur-signed-line-module-inverse-image-action", "dag-def-pur-signed-line-pullback-unit-presentation"]
+++
Let U:C→D be continuous and its set inverse image preserve finite limits. Given a unit presentation [dag-def-pur-signed-line-pullback-unit-presentation] of S by R whose unit is a:R→U_*S, and an isomorphism presenting the underlying set of the abelian inverse image compatibly with its unit, there is an InverseImageAction(a,M) [dag-def-pur-signed-line-module-inverse-image-action] on that abelian inverse image. The action is obtained by transporting scalar multiplication along inverse image and the given presentations; its module axioms and restriction semilinearity hold globally.

(SHEAF DAG node `lem-pur-signed-line-module-action-presentations`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
