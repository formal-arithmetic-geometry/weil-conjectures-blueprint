+++
id = "det-pe-sections-conservative"
kind = "lemma"
title = "Evaluation on weakly contractible affines is conservative"
lean = ["CategoryTheory.GrothendieckTopology.exact_iff_of_forall_exists", "CategoryTheory.GrothendieckTopology.epi_iff_of_forall_exists", "AlgebraicGeometry.ProEtale.acyclic_iff_forall_isWeaklyContractible", "AlgebraicGeometry.Scheme.ProEt.exists_isWeaklyContractible_cover"]
order = 936
uses = ["det-pe-wcb-cover", "det-pe-weak-contractible-equivalences", "det-pe-wc-sections-exact"]
+++
Let $\Lambda$ be a ring and let $\mathcal W$ be the
class of affine weakly contractible objects of $X_{\mathrm{proét}}$.

1. A sequence $A\xrightarrow{f}B\xrightarrow{g}C$ of sheaves of $\Lambda$-modules with $g\circ f=0$
   is exact at $B$ if and only if $A(W)\to B(W)\to C(W)$ is exact for every
   $W\in\mathcal W$.
2. A complex of sheaves of $\Lambda$-modules is acyclic if and only if its evaluation at every
   $W\in\mathcal W$ is acyclic.
3. A morphism of sheaves of $\Lambda$-modules is an isomorphism if and only if its evaluation at
   every $W\in\mathcal W$ is bijective; a morphism of complexes is a quasi-isomorphism if and
   only if its evaluation at every $W\in\mathcal W$ is a quasi-isomorphism.
