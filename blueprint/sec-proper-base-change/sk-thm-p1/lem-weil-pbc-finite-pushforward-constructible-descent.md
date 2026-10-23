+++
id = "lem-weil-pbc-finite-pushforward-constructible-descent"
kind = "lemma"
title = "A sheaf whose finite direct image on a curve is constructible is constructible"
uses = ["def-weil-algebraic-closure", "def-weil-finite-integral-morphism", "def-weil-pbc-direct-image", "def-weil-pbc-curve-setting", "def-weil-pbc-constructible-torsion"]
lean = ["AlgebraicGeometry.CurveCoefficientPair.isConstructible_of_finite_pushforward"]
order = 1940
tags = ["stacks-095R"]
+++
Let $k$ be an algebraically closed field [def-weil-algebraic-closure], let $X$ and $Y$ be separated schemes of finite type over $k$ of dimension at most one, let $f:X\to Y$ be a finite morphism of $k$-schemes [def-weil-finite-integral-morphism], and let $F$ be a torsion abelian sheaf on $X_{\Et}$ whose direct image $f_*F$ [def-weil-pbc-direct-image] is torsion, so that $(X,F)$ and $(Y,f_*F)$ are curve coefficient pairs [def-weil-pbc-curve-setting]. If $f_*F$ is constructible [def-weil-pbc-constructible-torsion], then $F$ is constructible.
