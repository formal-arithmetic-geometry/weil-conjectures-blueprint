+++
id = "lem-sc-c8"
kind = "lemma"
title = "C8: surjectivity of the restriction map in degree two"
lean = ["AlgebraicGeometry.IsCurve.surjective_cohomologyMap_constantModSheaf_two"]
order = 1572
uses = ["def-sc-curves", "def-weil-pbc-eight-curve-assertions", "def-weil-pbc-scheme-conventions", "lem-sc-affine-cohomological-dimension", "lem-sc-affine-open-proper", "lem-sc-compactification", "thm-sc-affine-cohomology"]
+++
Let $k$ be algebraically closed, let $C$ be a
smooth separated connected curve over $k$, let
$j:U\hookrightarrow C$ be an
open immersion, and let
$r$ be a prime. Then the constant sheaf $\mathbf F_r$ satisfies
$\mathcal C_8(C,\mathbf F_r)$ of
[def-weil-pbc-eight-curve-assertions]: the restriction map

$$
H^2(C_{\Et},\mathbf F_r)\longrightarrow
H^2(U_{\Et},\mathbf F_r)
$$

is surjective.
