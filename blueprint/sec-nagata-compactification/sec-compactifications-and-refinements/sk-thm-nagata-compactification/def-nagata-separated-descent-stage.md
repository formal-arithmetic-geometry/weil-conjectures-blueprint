+++
id = "def-nagata-separated-descent-stage"
kind = "definition"
title = "Separated stage of a descended finite-presentation model"
order = 375
lean = ["AlgebraicGeometry.separatedDescentStage", "AlgebraicGeometry.separatedDescentModel"]
uses = ["def-nagata-finite-presentation-descent", "lemma-nagata-separated-descent-stage-exists"]
+++
Let $X\to S$ be separated, and let $Y_\lambda\to S_\lambda$ be of finite
presentation, with $S_\lambda$ quasi-compact and quasi-separated, such that
$X\cong Y_\lambda\times_{S_\lambda}S$ over $S$. Choose one witness from
[lemma-nagata-separated-descent-stage-exists] and define
$\lambda_{\mathrm{sep}}\geq\lambda$ to be its index and

$$
X^{\mathrm{sep}}_{\lambda_{\mathrm{sep}}}
=Y_\lambda\times_{S_\lambda}S_{\lambda_{\mathrm{sep}}}
\longrightarrow S_{\lambda_{\mathrm{sep}}}
$$

the corresponding separated model. When $X\to S$ is separated and of finite
presentation and $Y_\lambda$ is its finite-presentation descent model
$X^{\mathrm{desc}}_{\lambda_{\mathrm{rel}}}\to S_{\lambda_{\mathrm{rel}}}$,
we write $\lambda_{\mathrm{sep}}(X/S)$ and
$X^{\mathrm{sep}}_{\lambda_{\mathrm{sep}}(X/S)}$.
