+++
id = "sk-cor-pe-bounded-continuity"
kind = "corollary"
title = "Continuity of cohomology"
order = 999
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections", "sk-cor-pe-wc-sections"]
tags = ["sketch"]
+++
Suppose $U$ is quasi-compact and quasi-separated and $(K_i^\bullet)$ is a filtered diagram
of complexes of $\mathcal R$-modules vanishing below one fixed degree $a$. Then for every
$q$,

$$
\varinjlim_iH^q(U,K_i^\bullet)\simeq H^q\bigl(U,\varinjlim_iK_i^\bullet\bigr).
$$

If $f\colon X\to Y$ is quasi-compact and quasi-separated, the analogous map
$\varinjlim_iR^qf_*K_i^\bullet\to R^qf_*(\varinjlim_iK_i^\bullet)$ is an isomorphism of
sheaves on $Y_{\mathrm{proét}}$.
