+++
kind = "proof"
of = "proposition-comparison-etale-derived-category--3"
order = 474008
uses = ["proposition-comparison-morphism-inverse-image"]
+++
The inverse image $\nu_X^*$ on sheaves is exact and preserves direct sums,
since it is left adjoint to $\nu_{X,*}$
([proposition-comparison-morphism-inverse-image]). Represent the summands by
complexes. Their termwise direct sum represents the direct sum in the derived
category, and applying $\nu_X^*$ termwise commutes with this construction.
This is the specialization of
`CategoryTheory.Functor.preservesColimitsOfShape_mapDerivedCategory` to $\nu_X^*$;
the generic result uses K-injective resolutions to compute coproducts after
localization.
