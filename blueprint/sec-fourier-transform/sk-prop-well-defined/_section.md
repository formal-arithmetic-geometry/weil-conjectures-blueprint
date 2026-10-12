+++
id = "sk-prop-well-defined"
kind = "proposition"
title = "P2: the transform is an exact triangulated functor"
order = 3034
lean = ["AlgebraicGeometry.Etale.boundedConstructible_fourierTransform_obj_of_boundedConstructible", "AlgebraicGeometry.Etale.fourierTransformBoundedConstructible"]
uses = ["sk-def-ft", "sk-prop-kernel-lisse"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite commutative ring in which $p$ is invertible and
whose exponent is invertible on $S$, let $p_2$ be of finite type and
admit a compactification, and let $V'$ be locally of finite type over a
field. For every $K\in\Dbc(V,\Lambda)$ one has
$\FT_\psi(K)\in\Dbc(V',\Lambda)$, so $\FT_\psi$ restricts to a functor
$\Dbc(V,\Lambda)\to\Dbc(V',\Lambda)$.
