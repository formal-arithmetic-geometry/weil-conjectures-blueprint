+++
kind = "proof"
of = "lemma-largest-punctual-subsheaf--3"
uses = ["proposition-topos-functoriality", "definition-punctual-sheaf"]
+++
The counit $j^*j_*\to\id$ is an isomorphism for an open immersion, so the
restriction of the unit $F\to j_*j^*F$ is an isomorphism
(`AlgebraicGeometry.WeilSheaf.isIso_upperStar_map_unit_app`). Since $j^*$
preserves kernels, $j^*F_{\rm p}=0$. A sheaf on the affine line vanishing
on a nonempty open has finite support
(`AlgebraicGeometry.WeilSheaf.support_finite_of_isZero_upperStar`): its
support lies in the finite complement of that open. Thus $F_{\rm p}$ is
punctual. If $F$ has no nonzero punctual subsheaf, its kernel inclusion
$F_{\rm p}\hookrightarrow F$ forces $F_{\rm p}=0$, and the unit is a
monomorphism.
