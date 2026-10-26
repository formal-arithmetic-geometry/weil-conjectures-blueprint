+++
id = "lem-sc-c5"
kind = "lemma"
title = "C5: finiteness on proper curves"
lean = ["AlgebraicGeometry.IsCurve.finite_sheafH_constantModSheaf_of_isProper"]
order = 1461
uses = ["def-sc-curves", "def-weil-pbc-eight-curve-assertions", "lem-sc-artin-schreier-dimension", "lem-sc-as-sequence", "lem-sc-cohomological-dimension", "lem-sc-fixed-points-finite", "thm-sc-proper-cohomology"]
+++
Let $k$ be algebraically closed, let $C$ be a
smooth proper connected curve over $k$, let
$r$ be a prime (arbitrary, possibly
$r=\operatorname{char}k$), and let
$\mathbf F_r$ be the constant sheaf, viewed as constructible. Then
$\mathbf F_r$ satisfies $\mathcal C_5(C,\mathbf F_r)$ of
[def-weil-pbc-eight-curve-assertions]: $H^q(C_{\Et},\mathbf F_r)$
is finite for every $q\geq0$.
