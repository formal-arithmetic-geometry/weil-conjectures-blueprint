+++
id = "dag-lem-pur-signed-line-sheaf-pullback-forget"
kind = "dag-lemma"
title = "Signed line sheaf pullback forget"
name_showing = false
order = 187538
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-sheaf-pullback-forget"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.SignedLinePullbackConstruction.sheafPullbackForgetIso", "CategoryTheory.SignedLinePullbackConstruction.sheafPullbackForgetIso_unit"]
+++
Let U:C→D be continuous and V:E→Set a forgetful functor. Suppose left Kan extensions along U^op exist, V preserves them, and target sheafification exists and is preserved by V. Then the constructed E-valued sheaf inverse image followed by V is naturally isomorphic to the set inverse image of the underlying sheaf. This comparison sends the underlying E-valued adjunction unit to the set-valued adjunction unit. The site object and morphism universes may differ; the set universe contains both.

(SHEAF DAG node `lem-pur-signed-line-sheaf-pullback-forget`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`.
