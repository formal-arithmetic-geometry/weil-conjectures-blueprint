+++
id = "thm-pqf-immersion-descent"
kind = "theorem"
title = "Descent of the immersion to a finite stage"
lean = ["AlgebraicGeometry.Scheme.Hom.FiniteApproximation.exists_isOpenImmersion_isClosedImmersion", "AlgebraicGeometry.Scheme.exists_isClosedImmersion_of_isOpenImmersion_of_isLimit"]
order = 206
uses = ["def-weil-pbc-scheme-conventions", "pqf-def-locnoeth", "pqf-lem-finite-fp-locnoeth", "pqf-lem-limit-immersion-descends", "pqf-lem-limit-qc-open-descends", "pqf-lem-qs-intersection-qc"]
+++
Let $S$ be a quasi-compact and quasi-separated scheme and let
$\nu:N\to S$ be a morphism presented as a filtered limit
$N=\varprojlim_\lambda T_\lambda$ of finite $S$-schemes: each
$T_\lambda\to S$ is finite, the transition morphisms are $S$-morphisms, and
the projections $N\to T_\lambda$ are $S$-morphisms exhibiting $N$ as the
limit. Let $\iota:X\to N$ be a quasi-compact open immersion such that
$\nu\circ\iota:X\to S$ is locally of finite type. Then there are an index
$\lambda_0$ and a factorization

$$
X\xrightarrow{\ j\ }T\xrightarrow{\ i\ }T_{\lambda_0}
$$

of the composite $X\xrightarrow{\iota}N\to T_{\lambda_0}$, with $j$ a
quasi-compact open immersion and $i$ a closed immersion. If moreover $S$ is
locally Noetherian, then $T_{\lambda_0}$ is finite and of finite
presentation over $S$.
