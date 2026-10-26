+++
id = "det-pe-condensed-point-coefficients"
kind = "lemma"
title = "Coefficient sheaves of continuous functions"
lean = ["AlgebraicGeometry.ProEtale.continuousMapAddSheaf", "AlgebraicGeometry.ProEtale.constantSheafIsoContinuousMapAddSheaf", "AlgebraicGeometry.ProEtale.constantSheafCompComparisonUpperStarIso", "AlgebraicGeometry.ProEtale.comparisonUpperStarConstantSheafIsoContinuousMapRingSheaf"]
order = 1051
uses = ["def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism"]
+++
Let $X$ be a scheme and $M$ a topological abelian group. The presheaf
$\underline M_X\colon U\mapsto C(|U|,M)$ of continuous functions on the underlying
spaces is a sheaf on $X_{\Proet}$. If $M$ is discrete, the canonical map from the
constant sheaf with value $M$ to $\underline M_X$ is an isomorphism, and
$\underline M_X\cong\nu_X^*M_{X,\Et}$ is the pullback of the constant étale sheaf.
In particular, for a discrete ring $A$ the sheaf $U\mapsto C(|U|,A)=LC(|U|,A)$ is
the classical constant sheaf $\nu_X^*A_{X,\Et}$.
