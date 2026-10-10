+++
id = "prop-base-linear"
kind = "theorem"
title = "P7: the transform is linear over the base"
order = 2705
lean = ["AlgebraicGeometry.Etale.fourierTransformTensorIso"]
uses = ["def-fd-kernel", "def-fd-transform", "def-wf-tate-twist", "prop-functor-package"]
tags = ["latex:proposition"]
+++
Let $V_0\to S_0$ be the rank-$r$ vector bundle of [def-fd-kernel], let
$p:V\to S$ and $p':V^\vee\to S$ be the structure morphisms, and let
$\operatorname{FT}_\psi$ be the transform of [def-fd-transform]. For
$K\in D^b_c(V,E)$ and $N\in D^b_c(S,E)$ there is an isomorphism, natural
in $K$ and $N$,

$$
\operatorname{FT}_\psi\bigl(K\otimes^L_Ep^*N\bigr)\cong
\operatorname{FT}_\psi(K)\otimes^L_E{p'}^*N .
$$

In particular:

1. for $N$ from the base,
   $\operatorname{FT}_\psi(p^*N)\cong\operatorname{FT}_\psi(\underline{E})\otimes^L_E{p'}^*N$,
   so the transform of a base-changed sheaf is the base change of the
   transform of the unit;
2. (*Tate twists*) for every $m\in\mathbf Z$ and every $K$,
   $$
   \operatorname{FT}_\psi\bigl(K(m)\bigr)\cong\operatorname{FT}_\psi(K)(m),
   $$
   with the Tate twist of [def-wf-tate-twist]; if $K$ carries a Weil
   structure, this isomorphism is one of Weil complexes.
