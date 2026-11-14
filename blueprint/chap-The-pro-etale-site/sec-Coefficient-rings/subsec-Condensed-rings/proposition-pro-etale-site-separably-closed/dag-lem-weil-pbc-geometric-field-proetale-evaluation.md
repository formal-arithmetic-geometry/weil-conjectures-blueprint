+++
id = "dag-lem-weil-pbc-geometric-field-proetale-evaluation"
kind = "dag-lemma"
title = "Pro-etale evaluation over an algebraically closed field"
name_showing = false
order = 173504
tags = ["sheaf-dag"]
split_from = "proposition-pro-etale-site-separably-closed--2"
dag_id = "lem-weil-pbc-geometric-field-proetale-evaluation"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.geometricFieldTest_isContinuous", "AlgebraicGeometry.ProEtale.geometricFieldRestriction", "AlgebraicGeometry.ProEtale.geometricFieldTestFinalMap", "AlgebraicGeometry.ProEtale.geometricFieldPointAdjunction", "AlgebraicGeometry.ProEtale.geometricFieldAbelianPointAdjunction", "AlgebraicGeometry.ProEtale.geometricFieldTestBaseChange", "AlgebraicGeometry.ProEtale.geometricFieldRestrictionComparison", "AlgebraicGeometry.ProEtale.geometricFieldEvaluationComparison", "AlgebraicGeometry.ProEtale.geometricFieldInverseImageComp", "AlgebraicGeometry.ProEtale.geometricFieldInverseImageIdentity", "AlgebraicGeometry.ProEtale.geometricFieldModuleRestriction", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation_exact", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation_extension", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation_coherence", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation_identity", "AlgebraicGeometry.ProEtale.geometric_field_proetale_evaluation_operations"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Use `def-weil-size-convention`. Let $K$ be an algebraically closed field `def-weil-algebraic-closure`, and let $Z=\operatorname{Spec}K$ `def-pc-scheme`. The functor $S\mapsto Z[S]$ of `lem-weil-pbc-profinite-test-object-functor` identifies sheaves on $Z_{\mathrm{proet}}$ [dag-def-weil-pbc-proetale-site] with sheaves on profinite sets with finite jointly surjective coverings. Under this identification, the inverse image $p_Z^*$ of `lem-weil-pbc-profinite-point-pullback` is the identity on sheaves on profinite sets, and evaluation at $Z$ is evaluation at the one-point profinite set. Every pro-etale covering of $Z$ admits a section through one member. Evaluation at $Z$ is exact on abelian sheaves, and on sheaves of modules `def-weil-sheaf-of-modules-category` over any ring sheaf $R$ it preserves finite free modules and cokernels, with values in modules over $R(Z)$. For every extension $K\subseteq K'$ of algebraically closed fields, scheme inverse image `def-weil-proetale-inverse-image` corresponds to the identity under these profinite-site identifications, and therefore canonically preserves evaluation at the final object. These identifications are compatible with composition and with ring and module structures.

(SHEAF DAG node `lem-weil-pbc-geometric-field-proetale-evaluation`; machine-alignment layer.) Split from [proposition-pro-etale-site-separably-closed--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-sfb-profinite-test-objects`, `def-sfb-upper-star-from-point`, `def-weil-algebraic-closure`, `def-weil-proetale-inverse-image`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `lem-weil-pbc-profinite-point-pullback`.
