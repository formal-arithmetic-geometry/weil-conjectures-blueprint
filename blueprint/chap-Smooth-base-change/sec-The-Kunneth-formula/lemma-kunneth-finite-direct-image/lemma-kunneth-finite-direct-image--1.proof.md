+++
kind = "proof"
of = "lemma-kunneth-finite-direct-image--1"
order = 711002
uses = ["lemma-identity-pasting", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "lemma-base-change-along-product-projection"]
+++
Put $K=e^*F$. Pasting with the square whose horizontal maps are identities,
and using the first assumed base change isomorphism, reduces the first
assertion to the invertibility of

$$
R\pi'_*A_{X'_i}\otimes^{\mathbf L}Rh_*K
\longrightarrow Rh_*(h^*R\pi'_*A_{X'_i}\otimes^{\mathbf L}K).
$$

This is the Künneth map for $\operatorname{id}_{X'}$ and $h$, up to the
canonical identifications for the identity functor. These are the steps
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_iff_degenerate` and
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_degenerate_iff_kunnethMap`;
the first uses `AlgebraicGeometry.Etale.tensorBaseChangeMap_paste`, the
tensor version of [lemma-identity-pasting].

The morphism $\rho$ is finite because it is a base change of $\pi'$.
Proper base change identifies $h^*R\pi'_*A_{X'_i}$ with $R\rho_*A_{Y_i}$,
and the projection formula for $\rho$ identifies the target with
$R(h\rho)_*\rho^*K$. Compatibility of the Künneth map with this exchange
map is `AlgebraicGeometry.Etale.kunnethMap_derivedBaseChangeMap`. Thus it
suffices to consider the Künneth map for $\pi'$ and $h$ with coefficients
$A_{X'_i}$ and $K$.

By the projection formula for $\pi'$, this last map is $R\pi'_*$ of the
second assumed base change map, with the tensor unit identified with the
constant sheaf. It is therefore an isomorphism. Lean uses
`AlgebraicGeometry.Etale.isIso_kunnethMap_tensorUnit` and
`AlgebraicGeometry.Etale.isIso_kunnethMap_rightDerivedLowerStar_unit` for
these two steps. The projection formula used here is
`AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarProjectionMap_of_isProper`;
the finite coefficient ring is torsion, and both finite maps are proper.
The base change input is the unbounded étale version of
[theorem-proper-base-change-classical-pro].

For the geometric assertion, form $X'_i=X_i\times_X X'$ and then
$Y_i=X'_i\times_{X'}Y$. Exactness of finite direct image and proper base
change give

$$
p^*(\pi_*A_{X_i})\simeq R\pi'_*A_{X'_i}.
$$

This is `AlgebraicGeometry.Etale.leftDerivedUpperStarSingleFunctorLowerStarUnitIso`;
the exactness is [lemma-finite-morphisms]. The base change theorem towards
a field, whose product case is [lemma-base-change-along-product-projection],
gives the first required base change isomorphism for $\mathcal F$ in degree
$0$. Apply it also to $X_i$, which is of finite type over $k$. Compatibility
with pasting then gives the second required isomorphism. These inputs are
`AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_app_singleFunctor` and
`AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_app_upperStar_singleFunctor`.
Apply the first assertion and transport along the displayed isomorphism.
