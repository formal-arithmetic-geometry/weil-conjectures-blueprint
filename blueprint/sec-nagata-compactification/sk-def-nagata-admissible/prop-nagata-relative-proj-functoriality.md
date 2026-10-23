+++
id = "prop-nagata-relative-proj-functoriality"
kind = "theorem"
title = "Restriction, base change, and functoriality of Proj"
lean = ["AlgebraicGeometry.Scheme.GradedAlgebraData.pullbackDataOfIsAffine", "AlgebraicGeometry.Scheme.GradedAlgebraData.isPullback_pullbackOfIsAffine", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjMap", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjIsoOfIso", "AlgebraicGeometry.Scheme.GradedAlgebraData.isClosedImmersion_relProjMap", "AlgebraicGeometry.Scheme.GradedAlgebraData.isPullback_relProjFunctor_map", "GradedRingHom.IsGradedBaseChange.isPushout_away", "AlgebraicGeometry.Proj.isPullback_map_of_isGradedBaseChange", "AlgebraicGeometry.Proj.isPullback_map_of_isGradedBaseChangeAlong"]
order = 186
tags = ["latex:proposition"]
uses = ["def-nagata-relative-proj", "lemma-nagata-proj-chart-ring-cocycle", "lemma-nagata-relative-proj-exists"]
+++
Relative Proj has the following properties.

1. Its restriction to an affine open $V$ is canonically
$\operatorname{Proj}(\Gamma(V,\mathcal A))$, compatibly on iterated
restrictions.
1. A degree-preserving equivalence of graded algebras inducing the
chosen degree-zero base identification induces an isomorphism of Proj.
1. A surjective degree-preserving morphism of graded algebras induces
a closed immersion in the opposite direction on Proj.
1. If $X$ is affine and $g\colon X'\to X$ is any morphism, the
coefficientwise pullback $g^*\mathcal A$, with
$(g^*\mathcal A)(V')=\Gamma(V',\mathcal O_{X'})\otimes_{\Gamma(X,\mathcal O_X)}\mathcal A(X)$
on affine opens $V'\subseteq X'$, is a quasi-coherent graded
$\mathcal O_{X'}$-algebra, and there is a canonical base-change isomorphism
$$
\operatorname{Proj}_{X'}(g^*\mathcal A)
\cong X'\times_X\operatorname{Proj}_X(\mathcal A).
$$
Chart by chart, for a ring homomorphism $R\to S$, an $\mathbb N$-graded
$R$-algebra $C$ and $f\in C$ homogeneous, this is the isomorphism
$S\otimes_RC_{(f),0}\cong(S\otimes_RC)_{(1\otimes f),0}$.
