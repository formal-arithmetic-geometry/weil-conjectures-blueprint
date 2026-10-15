+++
id = "sk-lem-bounded-continuity"
kind = "lemma"
title = "Continuity of cohomology"
order = 1559
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections"]
tags = ["sketch"]
+++
Here a filtered colimit of complexes means the termwise colimit of a filtered diagram of
complexes of sheaves.

Let $Y$ be a quasi-compact, quasi-separated scheme, let $A$ be a sheaf of rings on
$Y_{\mathrm{proét}}$, and let $(K_i^\bullet)$ be a filtered diagram of complexes of
$A$-modules that all vanish in degrees below a fixed integer $a$. Then for every $q$ the
natural map
$$
\varinjlim_iH^q(Y,K_i^\bullet)\longrightarrow H^q\bigl(Y,\varinjlim_iK_i^\bullet\bigr)
$$
is an isomorphism. If $g\colon Y\to Z$ is quasi-compact and quasi-separated, then likewise
$\varinjlim_iR^qg_*K_i^\bullet\to R^qg_*(\varinjlim_iK_i^\bullet)$ is an isomorphism of sheaves
on $Z_{\mathrm{proét}}$ for every $q$.
