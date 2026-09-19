+++
id = "sec-nagata-gap-registry"
kind = "section"
title = "Formalization gap registry"
order = 554
+++
This registry no longer lists open obligations. The chapter is formalized
along a route that never passes through several of the blocks developed
above; those blocks are kept because they carry the mathematical narrative,
and each of them now displays a **Status** note naming the declaration
or the alternative argument that replaced it. The bypassed groups are the
following.

- **Relative Proj.** The relative Proj interface of
[def-nagata-relative-proj], [lemma-nagata-relative-proj-exists]
and [prop-nagata-relative-proj-functoriality], and its base-change
and tensor-power companions, are never formalized as primitives. The blow-up
is glued from the affine Proj charts with
`AlgebraicGeometry.Scheme.Cover.RelativeGluingData`, as
[lemma-nagata-relative-proj-current-api] explains.
- **Affine blow-up chart algebra.** The chart algebra of
[def-nagata-blowup-chart-ring] and the Rees-localization coherence
lemmas are replaced by `AlgebraicGeometry.AffineBlowup` together
with `AffineBlowup.chart` and
`AffineBlowup.isLocalization_away_map`.
- **Projectivity and flat base change of blow-ups.** The route needs only
properness of the global blow-up
(`AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap`),
so [thm-nagata-global-blowup-projective] is not used; and it never
base-changes a blow-up along a flat morphism, so
[thm-nagata-blowup-flat-base-change] is not used either.
- **Chart-cocycle strict transforms.** The strict-transform chart rings,
their comparison isomorphisms and their cocycle are replaced by the API
of `WeilConjectures/Compactification/StrictTransform.lean`, that
is, `AlgebraicGeometry.strictTransform` with its closed immersion
into the base change and the pullback square over the preserved open.
- **The Raynaud–Gruson flattening chain.** The module strict transform,
the flattening theorem, and the selected flattening ideal are not
formalized. Elimination of indeterminacy is obtained instead by the
route of the chapter *Elimination of indeterminacy after Deligne and
Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.
- **Boundary-separation preparation.** The preparation data of
[lemma-nagata-separate-closed-data-exists] is replaced by
`AlgebraicGeometry.separationBlowup` and
`AlgebraicGeometry.exists_admissibleBlowup_disjoint_closures`,
which are proved from Deligne's disjointness blow-up.
- **Noetherian approximation bookkeeping.** The stagewise descent carried
out in the section *Finite-presentation reduction and approximation*
— coefficient stages, valid stages, and eventual equalities — is
subsumed by
`AlgebraicGeometry.Scheme.exists_isPullback_of_finitePresentation_of_isSeparated`
and `AlgebraicGeometry.Scheme.nonempty_noetherianApproximation`,
as [lemma-nagata-noetherian-current-api] records.
- **The explicit final assembly.** The named intermediate objects of the
section *Explicit final assembly* are not built separately:
`AlgebraicGeometry.NagataCompactification` and
`AlgebraicGeometry.nagataCompactification_of_locallyOfFinitePresentation`
produce the factorization and its three properties directly.
- **Selected-witness and specification pairs.** Wherever the blueprint
chooses a witness and then records its fields in a companion lemma, the
Lean route uses the corresponding existence statement directly, so
neither member of the pair has a declaration of its own. This is the
case for the quasi-affine immersion into relative affine space, the
affine neighbourhood of finitely many generic points, and the
constructible separation data in a spectral space.
