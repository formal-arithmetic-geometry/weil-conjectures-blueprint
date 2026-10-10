+++
id = "prop-nagata-relative-proj-functoriality"
kind = "theorem"
title = "Restriction, base change, and functoriality of Proj"
order = 44
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
1. If $g\colon X'\to X$ is flat, then coefficientwise pullback gives a
canonical base-change isomorphism
$$
\operatorname{Proj}_{X'}(g^*\mathcal A)
\cong X'\times_X\operatorname{Proj}_X(\mathcal A).
$$
