+++
id = "det-pe-wcb-clopen-partition"
kind = "lemma"
title = "Coverings of a w-contractible affine are refined by clopen partitions"
lean = ["AlgebraicGeometry.exists_comp_eq_id_of_isWContractibleRing", "AlgebraicGeometry.Scheme.ProEt.exists_disjoint_cover_of_comp_sigmaDesc_eq_id"]
order = 962
uses = ["det-pe-wcb-split-cover", "def-weil-pbc-proetale-covering", "lem-trf-weakly-etale-between-objects", "det-pe-morphisms-etale-comparison"]
+++
Let $U=\operatorname{Spec}D$ with $D$ w-contractible be an object of $X_{\mathrm{proét}}$,
and let $\{U_i\to U\}_{i\in I}$ be a covering in $X_{\mathrm{proét}}$. There are a finite
partition $U=U'_1\sqcup\dots\sqcup U'_m$ into clopen subschemes, indices $i_1,\dots,i_m$,
and $U$-morphisms $g_k\colon U'_k\to U_{i_k}$.
