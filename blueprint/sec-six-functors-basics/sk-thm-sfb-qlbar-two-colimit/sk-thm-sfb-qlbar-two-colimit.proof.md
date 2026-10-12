+++
kind  = "proof"
of    = "sk-thm-sfb-qlbar-two-colimit"
uses = []
+++
*The cocone.* The derived extensions of scalars are [def-sfb-derived-extend-subfield] and
[def-sfb-derived-extend-to-qlbar], with transitivity [def-sfb-derived-extend-comp-iso]. They
preserve bounded constructibility ([lem-sfb-extend-subfield-constructible],
[lem-sfb-extend-to-qlbar-constructible]) and so restrict to functors between the categories of
[def-sfb-dcons-subfield] and [def-sfb-dcons-qlbar]
([def-sfb-constructible-extend-subfield], [def-sfb-constructible-extend-to-qlbar]), again
compatible ([def-sfb-constructible-extend-comp-iso]); this is the cocone
[def-sfb-constructible-cocone].

*The 2-colimit.* For Noetherian $|X|$, (Hom-surj) and (Hom-inj) are
[lem-sfb-constructible-cocone-hom-surj] and [lem-sfb-constructible-cocone-hom-inj], and (Obj) is
[lem-sfb-constructible-cocone-obj]; together they give
[thm-sfb-constructible-cocone-two-colimit].

None of the three properties is a formal consequence of
$\overline{\mathbf Q}_{\ell,X}=\operatorname{colim}_EE_X$ ([sk-prop-sfb-qlbar-colimit-x]): (Obj) is a descent
statement for constructible objects ([sk-def-sfb-constructible]), and (Hom) is the continuity of
the derived hom out of a constructible complex. Both fail on the unbounded derived categories,
which is why the statement is restricted to bounded constructible complexes.
