+++
id = "lem-sc-arbitrary-curve-cd"
kind = "lemma"
title = "The torsion bound on an arbitrary algebraic curve"
lean = ["AlgebraicGeometry.IsCurve.hasTorsionCohomologicalDimensionLE", "AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_three_le", "AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_two_le_of_isAffine"]
order = 2246
uses = ["def-sc-etale-torsion-cd", "def-weil-pbc-scheme-conventions", "lem-fin-normalization-extension-finite", "lem-sc-affine-cohomological-dimension", "lem-sc-cohomological-dimension", "lem-sc-normal-dim1-dvr", "lem-weil-pbc-zero-dimensional-cohomology", "lemma-weil-pbc-finite-direct-image-exact", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $X$ be a
separated finite-type
scheme of dimension at most one over an algebraically closed
field. Put $e=1$ if $X$ is affine, and $e=2$ otherwise.
Then $\operatorname{cd}_{\rm tor}(X)\leq e$, in the sense of
[def-sc-etale-torsion-cd]. That is, for every torsion abelian sheaf $F$ on
$X_{\Et}$, with no condition relating the torsion of $F$ to the
characteristic, $H^q(X_{\Et},F)=0$ for $q\geq3$, and for $q\geq2$ if $X$ is
affine.
