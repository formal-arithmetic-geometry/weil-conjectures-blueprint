+++
id = "det-pe-products-exact"
kind = "lemma"
title = "Products of pro-étale module sheaves are exact"
lean = ["AlgebraicGeometry.Scheme.ProEt.epi_piMap", "AlgebraicGeometry.Scheme.ProEt.epi_pi_map", "AlgebraicGeometry.Scheme.ProEt.countableAB4Star", "AlgebraicGeometry.ProEtale.CondensedRing.countableAB4Star_mod"]
order = 979
uses = ["det-pe-sections-conservative", "det-pe-wc-sections-exact"]
+++
1. For every (small) set $I$ and every family of epimorphisms $\varphi_i\colon A_i\to B_i$
   of abelian sheaves on $X_{\mathrm{proét}}$, the product
   $\prod_i\varphi_i\colon\prod_iA_i\to\prod_iB_i$ is an epimorphism. Hence for every family
   of short exact sequences $0\to A_i\to B_i\to C_i\to0$ of abelian sheaves the sequence
   $0\to\prod_iA_i\to\prod_iB_i\to\prod_iC_i\to0$ is exact.
2. Let $\Lambda$ be a ring. Countable products of epimorphisms of sheaves of $\Lambda$-modules
   on $X_{\mathrm{proét}}$ are epimorphisms; equivalently, countable products are exact in the
   category of sheaves of $\Lambda$-modules on $X_{\mathrm{proét}}$. The same holds for
   modules over the pullback to $X_{\mathrm{proét}}$ of a commutative condensed ring.
