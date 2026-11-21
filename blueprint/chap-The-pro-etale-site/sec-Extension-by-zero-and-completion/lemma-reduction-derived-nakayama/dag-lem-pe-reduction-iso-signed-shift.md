+++
id = "dag-lem-pe-reduction-iso-signed-shift"
kind = "dag-lemma"
title = "Signed shift equation for the canonical principal-resolution tensor comparison"
name_showing = false
order = 210513
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "lem-pe-reduction-iso-signed-shift"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["DerivedCategory.reductionIso_inv_signed_shift"]
+++
Let A be a Grothendieck abelian category `def-sp-grothendieck-abelian` with a closed braided monoidal structure and additive tensor `def-sfb-monoidal-category`, functorial flat resolutions, and the resulting derived tensor and canonical lax monoidal localization Q `lem-sfb-derived-monoidal`. Let B be a commutative ring acting linearly and monoidally on A, meaning scalar multiplication commutes with tensoring on either side. Fix b in B, an object N of A, and p:1→N such that 0→1 --b--> 1 --p--> N→0 is short exact (the first arrow is b times the identity). Write e_M:QM⊗Q(N$[0]$)≅Q Cone(b:M→M) for the canonical reductionIso: inverse tensor of Q applied to the two-term resolution augmentation, followed by the canonical scalar-cone tensor comparison `lem-pe-scalar-cone-tensor-model`. Use the cochain localization and cone of `def-weil-abstract-derived-category` and standard derived tensor shifts of `def-weil-triangulated-category`. For every unbounded cochain complex M and every integer t, the inverse e_M satisfies Q(mappingCone.shiftIso(b·id_M,t).inv) ≫ Q.shift_t(Cone(b_M)) ≫ (e_M.inv)$[t]$ = e_{M$[t]$}.inv ≫ tensorRight(Q(N$[0]$)).map(Q.shift_t(M)) ≫ tensorRight(Q(N$[0]$)).shift_t(QM). This asserts only compatibility of the already constructed comparison with one input shift; it asserts no family of coefficient quotients or natural isomorphisms.

(SHEAF DAG node `lem-pe-reduction-iso-signed-shift`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: statement. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-pc-kflat-complex`, `def-pc-module-kflat-complex`, `def-sfb-monoidal-category`, `def-sp-grothendieck-abelian`, `def-weil-abstract-derived-category`, `def-weil-triangulated-category`, `lem-kun-derived-tensor-well-defined`, `lem-pc-tensor-mapping-cone-iso`, `lem-sc-derived-tensor-shift-independent-universe`, `lem-sf-total-bifunctor-homotopy-exact`, `lem-sfb-derived-monoidal`, `lem-sfb-sequential-kflat-derivability`, `lem-sfb-total-tensor-homotopy`, `lem-sfb-unary-left-derived-calculus`, `sk-def-sfb-derived-tensor-hom`.
