+++
id = "thm-fd-fourier-perverse"
kind = "theorem"
title = "Perverse amplitude of the Fourier transform"
lean = ["AlgebraicGeometry.Etale.isPerverseLE_fourierTransform", "AlgebraicGeometry.Etale.isPerverseGE_fourierTransform"]
order = 3089
uses = ["def-fd-kernel", "def-fd-transform", "def-per-perverse-subcategories", "def-weil-pbc-scheme-conventions", "lem-fd-as-lisse", "lem-per-artin-gabber-affine-curve", "lem-per-lisse-tensor-permanence", "lem-per-smooth-pullback-t-exact", "prop-kernel-lisse"]
+++
Let $k_0=\mathbf F_q$, let $V=V^\vee=\mathbf A^1_{k_0}$, let
$p_1,p_2:V\times_{k_0}V^\vee\to V,V^\vee$ be the projections of the
Fourier square, and let $\mathcal K_\psi$ be the
Fourier kernel of [def-fd-kernel]. The
Fourier–Deligne transform

$$
\operatorname{FT}_\psi=p_{2,!}\bigl(p_1^*(-)\otimes^L\mathcal K_\psi\bigr)[1]
$$

of [def-fd-transform] has perverse amplitude at most one on both
sides with respect to the perverse candidate subcategories of
[def-per-perverse-subcategories]:

$$
\operatorname{FT}_\psi\bigl({}^pD^{\le0}(V)\bigr)\subset
{}^pD^{\le1}(V^\vee),\qquad
\operatorname{FT}_\psi\bigl({}^pD^{\ge0}(V)\bigr)\subset
{}^pD^{\ge-1}(V^\vee),
$$

hence maps the perverse heart candidate of [def-per-perverse-subcategories]
into the strip ${}^pD^{\le1}(V^\vee)\cap{}^pD^{\ge-1}(V^\vee)$.
