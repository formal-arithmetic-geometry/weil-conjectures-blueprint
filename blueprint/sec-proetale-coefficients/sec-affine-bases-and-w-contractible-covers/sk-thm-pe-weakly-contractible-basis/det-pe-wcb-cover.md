+++
id = "det-pe-wcb-cover"
kind = "lemma"
title = "Coverings by w-contractible affines"
lean = ["AlgebraicGeometry.Scheme.ProEt.exists_isWContractibleRing_cover", "exists_isWContractibleRing"]
order = 965
uses = ["det-pe-wc-cover-second-stage", "lem-weil-pbc-strict-w-cover", "def-weil-pbc-proetale-covering", "lem-weil-pbc-ind-etale-stability", "lem-trf-weakly-etale-between-objects"]
+++
Every object $U$ of $X_{\mathrm{proét}}$ has a covering $\{\operatorname{Spec}D_i\to U\}$ in
$X_{\mathrm{proét}}$ with every $D_i$ w-contractible. Each $\operatorname{Spec}D_i\to U$ can
be taken to factor as $\operatorname{Spec}D_i\to\operatorname{Spec}B_i\subset U$, with
$\operatorname{Spec}B_i$ an affine open of $U$ and $B_i\to D_i$ faithfully flat and
ind-étale.
