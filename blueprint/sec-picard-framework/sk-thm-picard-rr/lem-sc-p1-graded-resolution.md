+++
id = "lem-sc-p1-graded-resolution"
kind = "lemma"
title = "Resolutions by twists on $\\mathbf P^1_k$"
lean = ["AlgebraicGeometry.ProjectiveLine.exists_shortExact_sigma_twist", "AlgebraicGeometry.ProjectiveLine.exists_exact_sigma_twist"]
order = 697
uses = ["def-sc-p1-standard", "lem-sc-p1-twist-exists"]
+++
Let $k$ be a field and $\mathcal G$ a coherent
$\mathcal O_{\mathbf P^1_k}$-module. Then there is an exact
sequence of $\mathcal O_{\mathbf P^1_k}$-modules

$$
0\longrightarrow\mathcal E_2\longrightarrow\mathcal E_1
\longrightarrow\mathcal E_0\longrightarrow\mathcal G\longrightarrow0
$$

in which each $\mathcal E_i$ is a finite direct sum of modules
$\mathcal O(d)$, $d\in\mathbf Z$, with the convention of
[def-sc-p1-standard].
