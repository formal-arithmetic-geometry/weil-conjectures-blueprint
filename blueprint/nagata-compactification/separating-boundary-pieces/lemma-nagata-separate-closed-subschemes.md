+++
id = "lemma-nagata-separate-closed-subschemes"
kind = "lemma"
title = "Properties of the closed-boundary separation blow-up, [stacks-project]"
order = 489
lean = ["AlgebraicGeometry.disjoint_range_strictTransformMap_sup"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-separate-closed-subschemes", "lemma-nagata-blowup-proper", "lemma-nagata-extended-ideal-affine-chart", "lemma-nagata-separate-closed-data-exists", "lemma-nagata-strict-transform-ambient-closed", "lemma-nagata-strict-transform-closure-characterization", "prop-nagata-global-blowup-cover-independent"]
+++
The morphism $\mathsf{SepBl}_U(Z_1,Z_2)\to X$ is $U$-admissible, and the
strict transforms of $Z_1$ and $Z_2$ in it are disjoint.

## Proof

The selected center is disjoint from $U_Z$, hence its image in $X$ is
disjoint from $U$. A composite of finite-presentation closed immersions is
finite presentation, so the ambient center is finite presentation and its
blow-up is $U$-admissible. By
[lemma-nagata-strict-transform-ambient-closed], the strict transforms
of $Z_1$ and $Z_2$ in this ambient blow-up agree with their strict
transforms in $\operatorname{Bl}_C(Z)$, which are disjoint by the selected
preparation witness.
