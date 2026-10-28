+++
id = "det-pe-left-complete-iso"
kind = "lemma"
title = "Postnikov convergence in the pro-étale derived category"
lean = ["DerivedCategory.isHomotopyLimit_truncGECone"]
order = 996
uses = ["det-pe-left-complete-truncation-tower", "det-pe-milnor-sequence"]
+++
Let $\mathcal C$ be an abelian category with K-injective resolutions in which countable
products exist and are exact; for instance the sheaves of $\Lambda$-modules on
$X_{\mathrm{proét}}$ ($\Lambda$ a ring). For every object $K$ of $D(\mathcal C)$, the
truncation maps $K\to\tau_{\geq-n}K$ exhibit $K$ as a homotopy limit of the tower
$\cdots\to\tau_{\geq-1}K\to\tau_{\geq0}K$: with $T$ the transition endomorphism of
$\prod_n\tau_{\geq-n}K$, there is a distinguished triangle

$$
K\longrightarrow\prod_n\tau_{\geq-n}K\xrightarrow{\,1-T\,}\prod_n\tau_{\geq-n}K
\longrightarrow K[1]
$$

whose first map has the truncation maps as components. In other words,
$K\to R\varprojlim_n\tau_{\geq-n}K$ is an isomorphism.
