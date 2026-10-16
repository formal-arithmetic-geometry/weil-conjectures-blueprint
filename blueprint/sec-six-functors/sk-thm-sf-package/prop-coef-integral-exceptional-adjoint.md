+++
id = "prop-coef-integral-exceptional-adjoint"
kind = "theorem"
title = "The integral exceptional adjoint on constructible complexes"
lean = ["AlgebraicGeometry.Etale.boundedConstructibleIntegral_rightDerivedUpperShriek", "AlgebraicGeometry.Etale.boundedConstructibleIntegral_exceptionalAdjoint"]
order = 2493
tags = ["latex:proposition"]
uses = ["lem-coef-finite-exceptional", "lem-coef-integral-compact-support", "lem-coef-normalized-dvr-effectivity", "lemma-weil-pbc-completed-pullback-reduction", "prop-coef-integral-dualizing", "thm-coef-integral-verdier"]
+++
For a separated finite-type $f:X\to Y$, define

$$
G_fL=R\varprojlim_n\operatorname{Res}_n Rf_n^!L_n.
$$

Then $G_f$ maps $D^b_c(Y,R)$ to $D^b_c(X,R)$, is right
adjoint to integral $Rf_!$ on these categories, and has canonical
identifications

$$
G_fL\cong D_{X,R}f^*_{\mathrm{comp}}D_{Y,R}L,
\qquad (G_fL)\otimes_R^L A_n\cong Rf_n^!L_n.
$$

Here $f^*_{\mathrm{comp}}$ is completed pullback. For input
reduction Tor interval $[a,b]$, one output interval is
$[a-2\dim X,b+2\dim Y]$. The comparison identifies the
canonical units and counits; in particular the dualizing object
of [prop-coef-integral-dualizing] is $G_aR$.
This is an adjunction on the stated constructible categories.
