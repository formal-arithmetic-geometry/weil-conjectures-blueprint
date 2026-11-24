+++
id = "corollary-evaluation-weakly-contractible-objects"
kind = "corollary"
title = "Evaluation on weakly contractible objects"
order = 79
lean = ["AlgebraicGeometry.ProEtale.isZero_rightDerived_sectionsFunctor_of_isWeaklyContractible"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "definition-weak-contractibility"]
+++
Let $W$ be a [weakly contractible](@definition-weak-contractibility) object of [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site), for instance
$W=\operatorname{Spec}(D)$ with $D$ [w-contractible](@definition-w-local-w-strictly-local).

1. The functor $F\mapsto F(W)$ from abelian sheaves on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) to
   abelian groups is exact. Hence $H^q(W,F)=0$ for $q>0$, and
   $R\Gamma(W,K)\simeq K(W)$ for every complex $K$, with the right side
   computed term by term.
2. If $W$ is affine, evaluation at $W$ preserves all limits and all
   colimits of $\mathcal R$-modules.
3. Exactness of complexes and isomorphisms of $\mathcal R$-module
   sheaves can be tested by evaluation on all affine [weakly contractible](@definition-weak-contractibility)
   objects of [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site).
