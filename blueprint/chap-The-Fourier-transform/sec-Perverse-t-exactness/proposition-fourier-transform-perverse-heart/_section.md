+++
id = "proposition-fourier-transform-perverse-heart"
kind = "proposition"
title = "Fourier transform and the perverse heart"
order = 1260
lean = ["AlgebraicGeometry.isCurvePerverseLE_fourierTransform_obj", "AlgebraicGeometry.isCurvePerverseLE_fourierTransform_inv_obj", "AlgebraicGeometry.isCurvePerverse_fourierTransform_obj_iff"]
uses = ["lemma-artin-schreier-character-sheaf", "definition-tate-twists", "definition-weil-structure", "definition-perverse-sheaves-curve", "lemma-perverse-sheaves-curve"]
+++
On the geometric affine line, $\operatorname{FT}_\psi$ is a t-exact
equivalence of bounded constructible derived categories for the
perverse t-structure of Lemma [lemma-perverse-sheaves-curve], with inverse
$\operatorname{FT}_{\psi^{-1}}(-)(1)$. Hence it is an exact
equivalence of the perverse hearts, and its canonical Frobenius
compatibilities induce an exact equivalence of the categories of
perverse Weil sheaves.
