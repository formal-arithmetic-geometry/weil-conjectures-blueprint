+++
id = "sk-def-pe-classical-definition"
kind = "definition"
title = "Classical pro-étale sheaves"
order = 989
uses = ["sk-def-pe-site", "sk-prop-pe-affine-basis"]
tags = ["sketch"]
+++
In this subsection $\Lambda$ denotes a discrete commutative ring and
$\Lambda_X$ its constant sheaf on $X_{\Proet}$.

A sheaf $F$ on $X_{\Proet}$ is *classical* if, for every pro-étale affine
presentation $U=\varprojlim_i U_i$ with $U_i$ affine and étale over $X$, its
restriction maps induce a bijection

$$
\varinjlim_i F(U_i)\xrightarrow{\ \sim\ }F(U).
$$

For sheaves of modules the map is required to be an isomorphism of modules. A
complex is classical if all its cohomology sheaves are classical.
