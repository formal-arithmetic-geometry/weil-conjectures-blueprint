+++
id = "det-pe-bounded-continuity-direct-image"
kind = "lemma"
title = "Higher direct images commute with filtered colimits and direct sums"
lean = ["AlgebraicGeometry.ProEtale.preservesColimitsOfShape_rightDerived_lowerStar", "AlgebraicGeometry.ProEtale.preservesColimitsOfShape_discrete_rightDerived_lowerStar"]
order = 954
uses = ["def-sfb-finite-lower-star", "det-pe-wcb-cover", "det-pe-wc-sections-exact"]
+++
Let $f\colon X\to Y$ be quasi-compact and quasi-separated, and let $q\geq0$.

1. For every small filtered category $I$ and every diagram $(M_i)_{i\in I}$ of abelian sheaves
   on $X_{\mathrm{proét}}$, the canonical map
   $\varinjlim_iR^qf_*M_i\to R^qf_*(\varinjlim_iM_i)$ is an isomorphism of abelian sheaves on
   $Y_{\mathrm{proét}}$.
2. For every family $(M_b)_{b\in B}$ of abelian sheaves on $X_{\mathrm{proét}}$, the canonical
   map $\bigoplus_bR^qf_*M_b\to R^qf_*(\bigoplus_bM_b)$ is an isomorphism.
