+++
id = "def-pc-projective-space-twist"
kind = "definition"
title = "Twists on projective space over a ring"
lean = ["AlgebraicGeometry.ProjectiveSpace.twist", "AlgebraicGeometry.ProjectiveSpace.isFreeGenerator_twistGenerator", "AlgebraicGeometry.ProjectiveSpace.map_twistGenerator_eq_transitionUnit_smul", "AlgebraicGeometry.ProjectiveSpace.twistGenerator", "AlgebraicGeometry.ProjectiveSpace.transitionUnit", "AlgebraicGeometry.ProjectiveSpace.coordinateSection"]
order = 620
uses = ["def-pc-proj", "def-sc-invertible-module", "def-sc-p1-standard", "pqf-def-coherent"]
+++
For a commutative ring $A$ and $n\ge0$, put
$P=\operatorname{Proj}(A[x_0,\ldots,x_n])$, using the
projective spectrum construction. Write
$U_i=D_+(x_i)$ for its standard affine opens. For $d\in\mathbf Z$,
the invertible module
$\mathcal O_P(d)$ is obtained by gluing free rank-one modules on
the $U_i$ with bases $e_i^{(d)}$ and transition rule
$e_i^{(d)}=(x_i/x_j)^d e_j^{(d)}$.
