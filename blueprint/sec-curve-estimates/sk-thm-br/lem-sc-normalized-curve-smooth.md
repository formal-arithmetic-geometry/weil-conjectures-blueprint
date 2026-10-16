+++
id = "lem-sc-normalized-curve-smooth"
kind = "lemma"
title = "The normalized curve over a perfect field is smooth"
lean = ["AlgebraicGeometry.smooth_of_isRegular", "AlgebraicGeometry.Scheme.smooth_fromNormalization_comp"]
order = 924
uses = ["def-sc-normalization", "lem-sc-normal-dim1-dvr", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular"]
+++
Let $X$ be an integral scheme of finite type over a perfect field
$k$ with $\dim X=1$, and
$\nu:X^{\nu}\to X$ its normalization
([def-sc-normalization]). Then $X^{\nu}$ is smooth over
$k$.
