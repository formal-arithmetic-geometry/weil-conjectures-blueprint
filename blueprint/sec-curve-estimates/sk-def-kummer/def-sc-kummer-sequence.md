+++
id = "def-sc-kummer-sequence"
kind = "definition"
title = "The Kummer sequence"
order = 874
uses = ["def-sc-curves"]
lean = ["AlgebraicGeometry.Scheme.kummerSequence"]
+++
Let $X$ be a scheme (for instance a curve $C$ over $k$ as in
[def-sc-curves]) and let $n$ be a natural number. The
*Kummer sequence* is the sequence of etale sheaves on
$X_{\Et}$

$$
1\longrightarrow\mu_n\longrightarrow\mathbf G_m
\xrightarrow{\ t\mapsto t^n\ }\mathbf G_m\longrightarrow1,
$$

where $\mathbf G_m$ is the sheaf of units of the structure sheaf and
$\mu_n$ is the kernel of $t\mapsto t^n$.
