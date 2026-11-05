+++
kind = "proof"
of = "theorem-smooth-base-change-classical-torsion--1"
order = 662002
uses = ["lemma-identity-pasting", "lemma-degree-zero-calculation", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed"]
+++
For $q<0$, both sides vanish. Suppose $q\geq0$. The stalkwise torsion
condition writes $F$ as a filtered colimit of sheaves killed by positive
integers $n$ invertible on $Y$. Inverse image commutes with this colimit,
and so do the higher direct images along the qcqs morphisms $f$ and $f'$.
It therefore suffices to treat a sheaf killed by one such $n$.
This is `AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_forall_nsmul_eq_zero`.

A sheaf killed by $n$ is a sheaf of $\Lambda/n\Lambda$-modules.
Restriction of scalars identifies its base change map with the one over
$\Lambda$, by
`AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_nsmul_eq_zero`.
Thus it suffices to prove smooth base change for every sheaf of
$A$-modules when $n=0$ in the commutative ring $A$ and $n$ is invertible
on the base.

Fix such $A$ and $n$. The property that base change in degree $q$ holds
for all qcqs direct images and all $A$-module sheaves is étale local on
the source and target of $g$ and is stable under composition, using
Lemma [lemma-identity-pasting]. Étale coordinates factor a smooth
morphism locally through an affine space. Induction on its dimension,
factoring the projection into relative lines, reduces to an affine
smooth morphism of relative dimension one with affine source. The case
of relative dimension zero is étale localization.

For these curves we prove the property after every base change, by
induction on $q$ with the hypothesis in all smaller degrees. Negative
degrees vanish, and degree zero follows from
Lemma [lemma-degree-zero-calculation]. If the universal property first
failed in degree $q\geq1$, the module form of
Lemma [lemma-reduction-curve-over-normal-base], namely
`AlgebraicGeometry.Etale.exists_isPullback_not_isZero_higherDirectImage`,
would give a smooth affine curve $C$ over a normal affine integral
scheme $S$ with algebraically closed function field $L$, an algebraically
closed extension $\Omega/L$, and $d\mid n$, such that, for
$h:C_\Omega\to C$,

$$
R^qh_*\underline{A/dA}\ne0.
$$

The integer $d$ is invertible on $S$ because it divides $n$. The module
form of Proposition [proposition-base-change-larger-algebraically-closed],
`AlgebraicGeometry.Etale.CurveTestDatum.isZero_higherDirectImage_constantSheaf`,
makes this higher direct image zero, a contradiction. This proves the
universal property for curves. Specializing to the identity base change
and reversing the reductions proves the assertion.
