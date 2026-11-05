+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--4"
order = 530013
uses = ["proposition-construction-independence-rf-shriek", "proposition-extension-zero-restriction-closed-subscheme", "proposition-sp-unique-adjoint"]
+++
Use compactification independence to compute $Rj_!$ with the trivial
compactification $U\xrightarrow jX\xrightarrow{\mathrm{id}}X$.
The identity direct image gives $Rj_!\simeq j_!$. The exact extension by
zero is left adjoint to the exact restriction $j^*$, so uniqueness of
right adjoints identifies $j^!$ with $j^*$.

The étale construction uses
`AlgebraicGeometry.Etale.rightDerivedLowerShriekIsoOfIsOpenImmersion` and
`AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekUpperStarAdjunction`.
For $\mathcal O_E$ and $\Qbarl$, Lean instead expresses the same step as
`CategoryTheory.conjugateIsoEquiv` applied to the corresponding
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekIsoOpenImmersionLowerShriek_padicIntegers`
or
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekIsoOpenImmersionLowerShriek_padicAlgCl`
comparison.
