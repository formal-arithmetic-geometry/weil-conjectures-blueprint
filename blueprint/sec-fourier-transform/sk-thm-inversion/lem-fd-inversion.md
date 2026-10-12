+++
id = "lem-fd-inversion"
kind = "theorem"
title = "Fourier inversion"
order = 3054
lean = ["AlgebraicGeometry.Etale.fourierTransformInversionIso", "AlgebraicGeometry.Etale.fourierTransformSquareIso"]
uses = ["def-fd-transform", "def-wf-tate-twist", "lem-fd-convolution-kernel", "lem-fd-kernel-composition", "prop-functor-package"]
+++
Let $S=\Spec k$ (with $V\cong\mathbf A^r_k$ of rank $r$, and let
$\iota':V\to V$ be the inverse of the addition). For every
constructible Weil complex $K$ on $V$ there are functorial
isomorphisms

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)\cong K(-r),
$$

and, with the same character,

$$
\operatorname{FT}_\psi\operatorname{FT}_\psi(K)\cong{\iota'}^*K(-r),
$$

where $(-r)$ is the $r$-fold Tate twist of [def-wf-tate-twist].
