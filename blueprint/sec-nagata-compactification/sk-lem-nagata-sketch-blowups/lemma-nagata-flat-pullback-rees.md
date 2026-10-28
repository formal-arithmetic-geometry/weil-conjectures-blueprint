+++
id = "lemma-nagata-flat-pullback-rees"
kind = "lemma"
title = "Flat pullback of the Rees algebra"
order = 143
lean = ["AlgebraicGeometry.reesGrading.isGradedBaseChangeAlong_hom"]
uses = ["def-nagata-flat-pullback-rees-map", "lemma-nagata-flat-pullback-ideal-pow"]
+++
The map $\beta_g$ is a graded algebra equivalence. Affine-locally: for a
flat ring map $\varphi\colon A\to B$ and an ideal $I\subseteq A$ with
$J=IB$, the induced map of Rees algebras
$\bigoplus_nI^n\to\bigoplus_nJ^n$ is a coefficientwise base change, i.e.
$B\otimes_AI^n\to J^n$ is an isomorphism in every degree $n$.
