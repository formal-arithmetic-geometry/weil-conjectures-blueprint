+++
id = "proposition-fourier-transform-perverse-heart"
kind = "proposition"
title = "Fourier transform and the perverse heart"
order = 1263
lean = ["AlgebraicGeometry.isCurvePerverse_fourierTransform_obj_iff", "AlgebraicGeometry.isCurvePerverseLE_fourierTransform_obj", "AlgebraicGeometry.isCurvePerverseLE_fourierTransform_inv_obj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-artin-schreier-character-sheaf", "proposition-fourier-inversion", "definition-perverse-sheaves-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
On the geometric affine line, $\operatorname{FT}_\psi$ is a t-exact
equivalence of bounded constructible derived categories for the
perverse t-structure of Lemma [lemma-perverse-sheaves-curve], with inverse
$\operatorname{FT}_{\psi^{-1}}(-)(1)$. Hence it is an exact
equivalence of the perverse hearts, and its canonical Frobenius
compatibilities induce an exact equivalence of the categories of
perverse Weil sheaves.
