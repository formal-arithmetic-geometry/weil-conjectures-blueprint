+++
id = "det-pe-products-derived"
kind = "lemma"
title = "Products in the derived category are termwise"
lean = ["DerivedCategory.isLimitFanQ", "HomologicalComplex.quasiIso_limMap"]
order = 989
uses = ["det-pe-products-exact"]
+++
Let $\mathcal C$ be an abelian category with K-injective resolutions, and let $I$ be a set
such that $I$-indexed products exist in $\mathcal C$ and are exact. By [det-pe-products-exact]
this holds for $\mathcal C$ the abelian sheaves on $X_{\mathrm{proét}}$ and any set $I$, and for
$\mathcal C$ the sheaves of $\Lambda$-modules ($\Lambda$ a ring) and $I$ countable. Let
$(K_i)_{i\in I}$ be a family of complexes in $\mathcal C$.

1. If $K_i\to K'_i$ are quasi-isomorphisms, so is $\prod_iK_i\to\prod_iK'_i$, and
   $H^p(\prod_iK_i)\cong\prod_iH^p(K_i)$ for every $p$.
2. The termwise product complex $\prod_iK_i$, with the projections induced by the termwise
   projections, is a product of the $K_i$ in $D(\mathcal C)$.
