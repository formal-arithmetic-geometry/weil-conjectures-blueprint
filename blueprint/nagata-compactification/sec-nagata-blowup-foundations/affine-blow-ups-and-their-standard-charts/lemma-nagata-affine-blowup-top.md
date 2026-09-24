+++
id = "lemma-nagata-affine-blowup-top"
kind = "lemma"
title = "Blow-up of the unit ideal"
order = 282
lean = ["AlgebraicGeometry.AffineBlowup.isIso_toSpec_of_eq_top"]
uses = ["def-nagata-affine-blowup", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "prop-nagata-affine-blowup-chart"]
+++
The blow-up of $\operatorname{Spec}(A)$ in the unit ideal is canonically
isomorphic to $\operatorname{Spec}(A)$ over $\operatorname{Spec}(A)$.

## Proof

The Rees algebra of the unit ideal is $A[t]$. The single standard open
$D_+(t)$ covers Proj, and its chart algebra $A[A/1]$ is $A$.
