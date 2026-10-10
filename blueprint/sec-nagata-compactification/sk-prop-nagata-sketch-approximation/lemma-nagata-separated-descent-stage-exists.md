+++
id = "lemma-nagata-separated-descent-stage-exists"
kind = "lemma"
title = "Existence of a separated descent stage"
order = 367
lean = ["AlgebraicGeometry.Scheme.exists_isSeparated_pullback_snd"]
uses = ["def-nagata-finite-presentation-descent", "lemma-nagata-diagonal-finite-presentation", "lemma-nagata-finite-presentation-descends"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of schemes with affine
transition maps and limit $S$, and let $X\to S$ be separated. Let
$Y_\lambda\to S_\lambda$ be of finite presentation, with $S_\lambda$
quasi-compact and quasi-separated, such that
$X\cong Y_\lambda\times_{S_\lambda}S$ over $S$. Then the base change of
$Y_\lambda$ to some later stage is separated. In particular, if $X\to S$ is
also of finite presentation and
$X^{\mathrm{desc}}_{\lambda_{\mathrm{rel}}}\to S_{\lambda_{\mathrm{rel}}}$ is the finite-presentation descent model,
there is a later index $\lambda_{\mathrm{sep}}$ for which the descended
model is separated, remains of finite presentation, and has base change
canonically isomorphic to $X\to S$.
