+++
id = "thm-pur-cohomological-smoothness"
kind = "theorem"
title = "Cohomological smoothness of smooth morphisms"
order = 1996
uses = ["def-coefficient-twists-detailed", "def-pur-co-smoothness", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-co-smooth-composition", "lem-pur-co-smooth-etale-locality", "lem-pur-smb-extraordinary", "prop-asd-smooth-base-change", "sbc-thm-etale-local-normal-form", "thm-asd-smooth-tensor", "thm-sf-ambient-adjoint-class", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
for every smooth separated morphism $f:X\to Y$ of relative dimension
$d$ put

$$
\omega_f\;=\;Rf^!\Lambda_Y.
$$

Then:

1. *Tensor formula.* For every $K\in D^b_{ctf}(Y,\Lambda)$ the
canonical map
$$
Lf^*K\otimes^L_{\Lambda_X}\omega_f\xrightarrow{\ \sim\ }Rf^!K
$$
is an isomorphism.
1. *Invertibility.* $\omega_f$ is invertible.
1. *Base change.* The formation of $\omega_f$ and of the
canonical map is compatible with arbitrary base change: for a
Cartesian square with $f'$ the base change of $f$,
$$
Lu^*\omega_f\xrightarrow{\ \sim\ }\omega_{f'},
$$
and the two canonical maps correspond under $Lu^*$; this holds for
*arbitrary* $v$ by [lem-pur-smb-extraordinary].
1. *Composition.* The tensor formula is compatible with
composition of smooth morphisms, through the composition isomorphism
for $R^!$ of [def-weil-exceptional-inverse-image].

(*Orientation-free form*: none of the four statements identifies
$\omega_f$ with a twist and a shift; that identification,
$\omega_f\cong\Lambda(d)[2d]$, is the content of
[thm-pur-diagonal-dualizing-object] proved below from the diagonal
argument.)
