+++
id = "sk-cor-pe-wc-sections"
kind = "corollary"
title = "Exact sections on contractible affines"
order = 969
lean = ["AlgebraicGeometry.Scheme.ProEt.isWeaklyContractible_of_iso", "CategoryTheory.GrothendieckTopology.epi_iff_of_forall_exists", "AlgebraicGeometry.ProEtale.projective_freeSheaf"]
uses = ["sk-thm-pe-weakly-contractible-basis"]
tags = ["sketch"]
+++
For an affine $U$ as in [sk-thm-pe-weakly-contractible-basis], the functor
$F\mapsto F(U)$ on abelian sheaves is exact. In particular

$$
H^q(U,F)=0\quad(q>0),\qquad R\Gamma(U,K)\simeq K(U)
$$

for a complex $K$, with the last expression computed term by term.

The affine objects in [sk-thm-pe-weakly-contractible-basis] form a basis of
$X_{\mathrm{proét}}$, in the sense that every object is covered by them; a fibre product of
two such affines is in general not of this form, but it is again covered by such affines.
Hence sheaf-theoretic assertions can be checked on these affines, while global cohomology
still records how they are glued. The arguments with derived inverse limits below rely on
this local exactness.
