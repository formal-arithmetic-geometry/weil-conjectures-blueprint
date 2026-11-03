+++
kind  = "proof"
of    = "thm-pur-smooth-base-change-coherence"
+++
Both composites are built from the purity construction of
[def-pur-smooth-purity-map] for $f$ and for $f'$. The dualizing-object
versions are compatible: the identification
$\omega_f\cong\Lambda_X(d)[2d]$ of [thm-pur-diagonal-dualizing-object]
is compatible with the base change $v$ because its constituents are:
the diagonal (the square of $f'$ is the base change of the square of
$f$ – the diagonal of the base change is the base change of the
diagonal of $f$, [lem-pur-diagonal-base-change] – and
[thm-pur-dnc-invariance] and
[cor-pur-vector-bundle-purity] are compatible with base change by
their statements, the tangent bundle of the base change being the base
change of the tangent bundle), the smooth base change
[lem-pur-smb-extraordinary] (the exchange is base-change
compatible by [def-exchange-projection]), and the co-projection
[lem-pur-coprojection]. The tensor formula
[thm-pur-cohomological-smoothness] is compatible
with base change together with the adjunction (the canonical map is the
mate of the projection formula, and base change of the adjunction is
the adjunction of the base change), and the twist isomorphisms
[def-coefficient-twists-detailed] are compatible with the pullback; the
square is the composite of these compatibilities. The transitivity
under successive base changes is the same statement for the transposed
compositions of the canonical base-change maps (the exchange of
[def-exchange-projection] composes, and the constructions are all
canonical).
