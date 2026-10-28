+++
id = "lem-fd-inversion"
kind = "theorem"
title = "Fourier inversion"
order = 4174
uses = ["def-fd-transform", "def-wf-tate-twist", "lem-fd-convolution-kernel", "lem-fd-kernel-composition", "prop-functor-package"]
+++
Let $S$ be a separated finite-type $k_0$-scheme, $V\to S$ a vector bundle
of rank $r$, identified with $V^{\vee\vee}$, let $\iota'=[-1]_V:V\to V$ be
the inverse of the addition, and let $\Lambda=E$ or $\overline{\mathbf Q}_\ell$.
For every $K\in\Dbc(V,\Lambda)$ there are isomorphisms, natural in $K$,

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)\cong K(-r),
$$

and, with the same character,

$$
\operatorname{FT}_\psi\operatorname{FT}_\psi(K)\cong{\iota'}^*K(-r),
$$

where $(-r)$ is the $r$-fold Tate twist of [def-wf-tate-twist]. Both maps
are defined by the localization and trace isomorphism of
[lem-fd-convolution-kernel]; in particular (the case $S=\Spec k$,
$V=\mathbf A^r_k$) they apply to every constructible Weil complex on
$\mathbf A^r$.
