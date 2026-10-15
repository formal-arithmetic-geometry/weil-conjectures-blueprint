+++
kind = "proof"
of = "sk-thm-sfb-qlbar-two-colimit"
+++
The statement about objects is part (3) of [sk-lem-coefficient-finite-descent]. Its proof descends the lisse
sheaves on the strata, together with their transition matrices, and then the connecting morphisms of a
finite Postnikov tower, so it descends the complexes themselves ([lem-sfb-constructible-cocone-obj]). The
bijection on morphisms is part (2) of [sk-lem-coefficient-finite-descent] with $r=0$, since $\Dctf$ is a full
subcategory; it rests on the continuity of Ext out of a constructible complex
([sk-lem-constructible-ext-continuity]). Surjectivity says that every morphism descends to a finite stage, and
injectivity that two morphisms with the same image agree at a later finite stage
([lem-sfb-constructible-cocone-hom-surj], [lem-sfb-constructible-cocone-hom-inj]). Together with descent of
objects, these say exactly that the functor from the category with objects the pairs $(E,K)$,
$K\in\Dctf(X,E)$, and Hom sets these colimits, to $\Dctf(X,\Qlb)$ is fully faithful and essentially surjective
([thm-sfb-constructible-cocone-two-colimit]).

The cocone itself: the derived extensions of scalars are [def-sfb-derived-extend-subfield] and
[def-sfb-derived-extend-to-qlbar], with transitivity [def-sfb-derived-extend-comp-iso]; they preserve bounded
constructibility ([lem-sfb-extend-subfield-constructible], [lem-sfb-extend-to-qlbar-constructible]) and restrict
to the categories [def-sfb-dcons-subfield] and [def-sfb-dcons-qlbar] ([def-sfb-constructible-extend-subfield],
[def-sfb-constructible-extend-to-qlbar], [def-sfb-constructible-extend-comp-iso]), forming the cocone
[def-sfb-constructible-cocone].

The proof uses only [sk-lem-coefficient-finite-descent] and [sk-lem-constructible-ext-continuity], which
precede the uniform Ext bound and Brown representability, so the proposition is available before them. None
of the properties is a formal consequence of $\overline{\mathbf Q}_{\ell,X}=\colim_EE_X$
([sk-prop-sfb-qlbar-colimit-x]); both fail on the unbounded derived categories.
