+++
id = "det-pe-left-complete-truncation-tower"
kind = "lemma"
title = "Cohomology of the truncation tower"
lean = ["DerivedCategory.isZero_of_isGE", "DerivedCategory.isIso_homologyFunctor_map_truncGEπ_app", "CategoryTheory.Limits.epi_one_sub_of_isZero_of_isIso", "CategoryTheory.Limits.isLimitOfIsZeroOfIsIso"]
order = 984
+++
Let $\mathcal C$ be an abelian category, $K$ an object of $D(\mathcal C)$, and
$\tau_{\geq-n}K$ ($n\geq0$) its truncations for the standard $t$-structure, with the
truncation maps $K\to\tau_{\geq-n}K$ and $\tau_{\geq-(n+1)}K\to\tau_{\geq-n}K$. Fix
$q\in\mathbf Z$ and put $N=\max(0,-q)$.

1. $H^q(\tau_{\geq-n}K)=0$ for $n<N$, and for $n\geq N$ the map
   $H^q(K)\to H^q(\tau_{\geq-n}K)$ is an isomorphism.
2. Let $T$ be the transition endomorphism of a product $\prod_nH^q(\tau_{\geq-n}K)$ (with
   components $\prod_mH^q(\tau_{\geq-m}K)\to H^q(\tau_{\geq-(n+1)}K)\to H^q(\tau_{\geq-n}K)$).
   Then $1-T$ is a split epimorphism, so its cokernel
   $R^1\varprojlim_nH^q(\tau_{\geq-n}K)$ vanishes, and the maps
   $H^q(K)\to H^q(\tau_{\geq-n}K)$ exhibit $H^q(K)$ as $\varprojlim_nH^q(\tau_{\geq-n}K)$.
