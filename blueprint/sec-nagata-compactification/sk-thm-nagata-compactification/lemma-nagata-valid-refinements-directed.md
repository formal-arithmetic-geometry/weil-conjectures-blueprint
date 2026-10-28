+++
id = "lemma-nagata-valid-refinements-directed"
kind = "lemma"
title = "Valid finite coefficient refinements form a directed set"
order = 350
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.nonempty_and_isDirected_stage", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.Stage.transition", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.Stage.transition_refl", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.Stage.transition_trans"]
uses = ["def-nagata-noetherian-stage", "lemma-nagata-affine-gluing-identities-eventually", "lemma-nagata-directed-finite-upper-bound", "lemma-nagata-filtered-colimit-finite-data"]
+++
The valid stages occurring in [def-nagata-noetherian-stage] are nonempty
and directed under inclusion: the chartwise sum
$(A_{\lambda,a}+A_{\mu,a})_a$ of the subrings of two valid stages
(the subring they generate) is again a valid stage, above both. If
$\lambda\leq\mu$, the inclusions $A_{\lambda,a}\subseteq A_{\mu,a}$ induce
compatible chart maps
$\operatorname{Spec}(A_{\mu,a})\to\operatorname{Spec}(A_{\lambda,a})$,
which glue to a transition morphism $S_\mu\to S_\lambda$; these morphisms
satisfy the identity and composition laws.
