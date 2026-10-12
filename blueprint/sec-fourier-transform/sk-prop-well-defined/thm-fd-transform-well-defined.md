+++
id = "thm-fd-transform-well-defined"
kind = "theorem"
title = "Well-definedness of the Fourier–Deligne transform"
order = 3035
lean = ["AlgebraicGeometry.Etale.boundedConstructible_fourierTransform_obj_of_boundedConstructible", "AlgebraicGeometry.Etale.fourierTransformBoundedConstructible"]
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "prop-functor-package", "prop-kernel-lisse"]
+++
Let $\Lambda$ be a finite commutative ring in which $p$ is invertible
and whose exponent is invertible on $S$, and let $\pi:V\to S$,
$\pi':V'\to S$, $b$, $\Psi$, $r\in\mathbf Z$ and the projections
$p_1,p_2$ be as in [def-fd-transform], with
$p_2:V\times_SV'\to V'$ of finite type and admitting a compactification.
Assume that $V'$ is locally of finite type over some field $k$. Let
$D^b_c(-,\Lambda)$ denote the full subcategory of the derived category of
étale sheaves of $\Lambda$-modules consisting of the bounded complexes
with constructible cohomology sheaves. Then for every
$K\in D^b_c(V,\Lambda)$,

$$
\operatorname{FT}_\psi(K)\in D^b_c(V',\Lambda),
$$

so that $\operatorname{FT}_\psi$ restricts to a functor

$$
\operatorname{FT}_\psi:
D^b_c(V,\Lambda)\longrightarrow D^b_c(V',\Lambda).
$$
