+++
id = "det-pe-milnor-epimorphic"
kind = "lemma"
title = "Towers with epimorphic transitions have no derived limit terms"
lean = ["CategoryTheory.GrothendieckTopology.epi_one_sub_of_forall_exists", "DerivedCategory.isHomotopyLimit_mapCone_Q_of_epi_one_sub", "AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi"]
order = 992
uses = ["det-pe-milnor-sequence", "det-pe-sections-conservative", "det-pe-wc-sections-exact", "det-pe-products-exact"]
+++
Let $\Lambda$ be a commutative ring.

1. Let $(M_n,t_n)$ be a tower of sheaves of $\Lambda$-modules on $X_{\mathrm{proét}}$ whose
   transition maps $t_n\colon M_{n+1}\to M_n$ are epimorphisms. Then
   $1-T\colon\prod_nM_n\to\prod_nM_n$ is an epimorphism, i.e. $R^1\varprojlim_nM_n=0$.
2. Let $(K_n)$ be a tower of complexes of sheaves of $\Lambda$-modules on $X_{\mathrm{proét}}$
   whose transition maps are epimorphisms in every degree. Then the degreewise limit
   $\varprojlim_nK_n$, with its projections, is a homotopy limit of the tower in
   $D(X_{\mathrm{proét}},\Lambda)$: it sits in a distinguished triangle
   $\varprojlim_nK_n\to\prod_nK_n\xrightarrow{1-T}\prod_nK_n\to(\varprojlim_nK_n)[1]$. In
   particular, for a tower of sheaves as in 1, $\varprojlim_nM_n\to R\varprojlim_nM_n$ is an
   isomorphism in $D(X_{\mathrm{proét}},\Lambda)$.
