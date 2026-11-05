+++
kind = "proof"
of = "lemma-finite-morphisms-cohomology--1"
order = 1594004
uses = ["lemma-finite-morphisms"]
+++
By the stalk formula of [lemma-finite-morphisms], the stalk of $h_*G$
at a geometric point with algebraically closed residue field is a
finite product of stalks of $G$. For an epimorphism $G\to G'$, the
induced maps on these factors are epimorphisms, and their finite
product is an epimorphism. These geometric stalks jointly detect
epimorphisms, so $h_*$ preserves epimorphisms. This is
`AlgebraicGeometry.Etale.preservesEpimorphisms_lowerStar_of_isFinite`.

The functor $h_*$ preserves finite limits. It therefore preserves
kernels as well as epimorphisms, hence homology and finite colimits.
This gives the asserted exactness. The same argument works in the
coefficient category $\mathcal A$ under the stated hypotheses.
