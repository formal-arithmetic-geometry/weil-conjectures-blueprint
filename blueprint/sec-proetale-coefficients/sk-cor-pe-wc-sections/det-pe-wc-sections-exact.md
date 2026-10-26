+++
id = "det-pe-wc-sections-exact"
kind = "lemma"
title = "Sections over a w-contractible affine are exact"
lean = ["AlgebraicGeometry.Scheme.ProEt.isWeaklyContractible_of_iso", "CategoryTheory.GrothendieckTopology.epi_iff_of_forall_exists", "AlgebraicGeometry.Scheme.ProEt.exists_isWeaklyContractible_cover"]
order = 931
uses = ["det-pe-wcb-projective"]
+++
Let $U=\operatorname{Spec}D$ with $D$ w-contractible be an object of $X_{\mathrm{proét}}$,
and let $\Lambda$ be a ring. The functor $\Gamma(U,-)\colon F\mapsto F(U)$ from sheaves of
$\Lambda$-modules on $X_{\mathrm{proét}}$ to $\Lambda$-modules is exact: it preserves kernels,
and an epimorphism $F\to G$ of sheaves of $\Lambda$-modules induces a surjection
$F(U)\to G(U)$. For $\Lambda=\mathbf Z$ this is the statement for abelian sheaves.
