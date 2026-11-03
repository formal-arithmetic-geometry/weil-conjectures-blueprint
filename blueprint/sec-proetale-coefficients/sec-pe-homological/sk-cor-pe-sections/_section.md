+++
id = "sk-cor-pe-sections"
kind = "corollary"
title = "Evaluation on weakly contractible objects"
order = 55
lean = ["CategoryTheory.GrothendieckTopology.exact_iff_of_forall_exists", "CategoryTheory.GrothendieckTopology.epi_iff_of_forall_exists", "AlgebraicGeometry.ProEtale.isZero_iff_forall_isWeaklyContractible", "AlgebraicGeometry.ProEtale.acyclic_iff_forall_isWeaklyContractible"]
uses = ["sk-thm-pe-weakly-contractible-basis", "sk-cor-pe-wc-sections", "sk-def-pe-weak-contractible"]
tags = ["sketch"]
+++
Let $W$ be a weakly contractible object of $X_{\mathrm{pro}\acute{e}t}$, for instance
$W=\operatorname{Spec}(D)$ with $D$ w-contractible.

1. The functor $F\mapsto F(W)$ from abelian sheaves on $X_{\mathrm{pro}\acute{e}t}$ to
   abelian groups is exact. Hence $H^q(W,F)=0$ for $q>0$, and
   $R\Gamma(W,K)\simeq K(W)$ for every complex $K$, with the right side
   computed term by term.
2. If $W$ is affine, evaluation at $W$ preserves all limits and all
   colimits of $\mathcal R$-modules.
3. Exactness of complexes and isomorphisms of $\mathcal R$-module
   sheaves can be tested by evaluation on all affine weakly contractible
   objects of $X_{\mathrm{pro}\acute{e}t}$.
