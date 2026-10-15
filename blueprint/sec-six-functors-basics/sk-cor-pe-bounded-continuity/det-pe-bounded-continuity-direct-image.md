+++
id = "det-pe-bounded-continuity-direct-image"
kind = "lemma"
title = "Higher direct images commute with bounded-below filtered colimits"
uses = ["det-pe-bounded-continuity-sections", "det-pe-topos-functoriality-inverse-image", "det-pe-wcb-cover"]
+++
Let $f\colon X\to Y$ be quasi-compact and quasi-separated, and let $(K_i^\bullet)$ be a
filtered diagram of complexes of $\mathcal R$-modules on $X_{\mathrm{proét}}$ vanishing
below a fixed degree $a$. Then for every $q$ the canonical map
$\varinjlim_iR^qf_*K_i^\bullet\to R^qf_*(\varinjlim_iK_i^\bullet)$ is an isomorphism of
sheaves on $Y_{\mathrm{proét}}$.
