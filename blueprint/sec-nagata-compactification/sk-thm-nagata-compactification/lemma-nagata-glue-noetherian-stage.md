+++
id = "lemma-nagata-glue-noetherian-stage"
kind = "lemma"
title = "Properties of the finite-type stages"
order = 351
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.stage_finiteType_isAffineHom", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.isLimitStageCone", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.noetherianApproximation"]
uses = ["def-nagata-glued-limit-comparison", "def-nagata-noetherian-inverse-system", "lemma-nagata-affine-gluing-identities-eventually", "lemma-nagata-valid-refinements-directed"]
+++
Every $S_\lambda$ is of finite type over $\mathbf Z$, and every transition
morphism $t_{\mu\lambda}$ is affine. Moreover, the comparison cone
$\kappa_S$ of [def-nagata-glued-limit-comparison] is a limit cone, so the
glued stages $S_\lambda$, indexed by the valid stages, form a Noetherian
approximation of $S$.
