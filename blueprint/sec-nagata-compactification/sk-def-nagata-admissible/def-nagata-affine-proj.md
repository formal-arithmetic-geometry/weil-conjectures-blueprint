+++
id = "def-nagata-affine-proj"
kind = "definition"
title = "Affine Proj"
order = 153
lean = ["AlgebraicGeometry.Proj", "AlgebraicGeometry.Proj.toSpecZero"]
uses = ["def-nagata-homogeneous-localization-degree-zero"]
+++
For an $\mathbb N$-graded commutative ring $R$, let $\operatorname{Proj}(R)$
be the scheme whose points are the homogeneous prime ideals of $R$ not
containing the irrelevant ideal $R_+$, with the Zariski topology and the
structure sheaf whose stalks are the degree-zero homogeneous localizations,
together with its structural morphism to $\operatorname{Spec}(R_0)$.
