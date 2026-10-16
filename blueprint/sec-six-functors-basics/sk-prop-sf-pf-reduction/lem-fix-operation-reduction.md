+++
id = "lem-fix-operation-reduction"
kind = "lemma"
title = "Basic operations and coefficient reduction"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_rightDerivedLowerStar", "AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_derivedHom_of_isSitePerfect", "AlgebraicGeometry.Etale.leftDerivedUpperStarReductionModIdealIso", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarReductionModIdealMap_span_pow", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekReductionModIdealMap", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekReductionModIdealMap_span_pow"]
order = 2228
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-integral-rational-qbar-compact-support", "def-weil-rationalization-karoubi", "def-weil-site-perfect-complex", "lem-fix-compact-support-coefficient-change", "lem-weil-pbc-standard-quotients-perfect", "lem-weil-scalar-extension-exact-triangulated", "lemma-weil-pbc-perfect-projection-formula", "prop-weil-pbc-direct-image-limits"]
+++
For the derived-complete
coefficient categories, reduction $\mathcal O_E\to A_{E,n}$ commutes
with derived pullback, tensor, ordinary direct image and compact-support
direct image on their stated bounded domains. Finite reduction
$A_{E,n}\to A_{E,m}$ commutes with pullback, tensor and
compact-support direct image on the finite-Tor domains.
For $\mathcal O_E\to A_{E,n}$, internal Hom and evaluation commute
with reduction for arbitrary first variables on the stated integral
domains. Between finite quotient rings, the elementary comparison
proved here assumes that the first variable is
site-perfect; this includes
the coefficient dual of a perfect complex at a point.
For admissible
exceptional adjoints, use the coefficient comparisons required in
that admissibility hypothesis. The same operations and comparisons
commute with rationalization
and common-stage
scalar extension. All the displayed comparisons preserve the tensor
associativity maps, evaluations, units and counits used to construct
the projection and exchange transformations.
