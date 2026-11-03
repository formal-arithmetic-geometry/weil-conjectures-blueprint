+++
id = "def-nagata-affine-fp-descent"
kind = "definition"
title = "Finite-stage model of a finitely presented affine algebra"
order = 358
lean = ["CommRingCat.fpDescentStage", "CommRingCat.fpDescentRelations", "CommRingCat.FPDescent", "CommRingCat.fpDescentEquiv"]
uses = ["def-nagata-directed-finite-upper-bound", "lemma-nagata-filtered-colimit-finite-data"]
+++
Let $A=\varinjlim_\lambda A_\lambda$ be a filtered colimit of commutative
rings (for instance the rings of affine opens of the stages of an inverse
system with affine transitions, $S_\lambda=\operatorname{Spec}(A_\lambda)$,
$S=\operatorname{Spec}(A)$), and fix a finite presentation

$$
B=A[x_1,\ldots,x_n]/(r_1,\ldots,r_m).
$$

The finitely many coefficients of the $r_j$ lift to a common stage. Let
$\lambda_B$ be a selected such stage, let $r_{j,\lambda_B}$ be the selected
lifted polynomials, and define

$$
B_{\lambda_B}
=A_{\lambda_B}[x_1,\ldots,x_n]/
(r_{1,\lambda_B},\ldots,r_{m,\lambda_B}).
$$

Define $\beta_B$ to be the comparison
$A\otimes_{A_{\lambda_B}}B_{\lambda_B}\to B$ induced by the presentation.
