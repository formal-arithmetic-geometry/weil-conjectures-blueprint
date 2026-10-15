+++
id = "sk-def-kummer"
kind = "definition"
title = "The Kummer sequence"
order = 992
uses = ["sk-def-curve"]
lean = ["AlgebraicGeometry.Scheme.kummerSequence"]
tags = ["sketch"]
+++
For a scheme $X$ (for instance $C$ as in [sk-def-curve]) and a
natural number $n$, the *Kummer sequence* is the sequence of étale
sheaves on $X$

$$
0\longrightarrow\mu_n\longrightarrow\mathbb G_m
\xrightarrow{\ \omega\mapsto\omega^n\ }\mathbb G_m\longrightarrow0
$$

where $\mathbb G_m$ is the sheaf of units of the structure sheaf and
$\mu_n=\ker(\omega\mapsto\omega^n)$ is the sheaf of $n$-th roots of
unity.
