+++
kind  = "proof"
of    = "def-sfb-derived-extend-comp-iso"
uses = ["det-def-sfb-derived-categories", "det-def-sfb-change-of-scalars", "lem-sfb-subfield-flat", "lem-sfb-qlbar-flat", "lem-sfb-subfield-coefficient-map-comp", "def-sfb-extend-scalars-iso-of-eq"]
+++
The extensions of scalars along $E_X\to F_X$ and $F_X\to\overline{\mathbf Q}_{\ell,X}$ are exact
([lem-sfb-subfield-flat], [lem-sfb-qlbar-flat]), and so is the one along their composite, which
equals $E_X\to\overline{\mathbf Q}_{\ell,X}$ ([lem-sfb-subfield-coefficient-map-comp]), via the isomorphism of
[def-sfb-extend-scalars-iso-of-eq]. For exact functors the left derived functor of a composite
is the composite of the left derived functors ([det-def-sfb-derived-categories]), so
$T_{F,\Qlb}\circ T_{E,F}\cong L(\operatorname{Ext}_{F_X\to\overline{\mathbf Q}_{\ell,X}}\circ
\operatorname{Ext}_{E_X\to F_X})$. Extension of scalars is compatible with composition
([det-def-sfb-change-of-scalars]), and by
[lem-sfb-subfield-coefficient-map-comp] and [def-sfb-extend-scalars-iso-of-eq] the composite
is $\operatorname{Ext}_{E_X\to\overline{\mathbf Q}_{\ell,X}}$, whose left derived functor is $T_{E,\Qlb}$.
