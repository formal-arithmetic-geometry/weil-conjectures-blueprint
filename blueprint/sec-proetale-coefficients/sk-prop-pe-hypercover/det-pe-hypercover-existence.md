+++
id = "det-pe-hypercover-existence"
kind = "lemma"
title = "Hypercovers by single w-contractible affines"
uses = ["det-pe-wcb-cover", "det-pe-wlocal-strict-contractible", "det-pe-weak-contractible-equivalences", "det-pe-topos-functoriality-site"]
+++
Let $U$ be a quasi-compact, quasi-separated object of $X_{\mathrm{proét}}$.

1. A finite product $D=D_1\times\dots\times D_k$ of w-contractible rings is w-contractible.
2. Every quasi-compact object $V$ of $X_{\mathrm{proét}}$ admits a single covering map
   $\operatorname{Spec}D\to V$ with $D$ w-contractible.
3. There is a hypercovering $W_\bullet\to U$ in $X_{\mathrm{proét}}$ (a simplicial object
   over $U$ such that $W_0\to U$ and every map $W_{r+1}\to(\operatorname{cosk}_r
   \operatorname{sk}_rW_\bullet)_{r+1}$ to the matching object is a covering) with every
   $W_r=\operatorname{Spec}D_r$, $D_r$ w-contractible; in particular every $W_r$ is
   affine and weakly contractible.
