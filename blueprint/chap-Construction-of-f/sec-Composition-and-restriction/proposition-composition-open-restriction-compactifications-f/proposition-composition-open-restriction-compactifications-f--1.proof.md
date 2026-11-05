+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--1"
order = 530010
uses = ["proposition-composition-base-change-rf-shriek", "proposition-sp-unique-adjoint", "theorem-existence-exceptional-inverse-image"]
+++
For finite coefficients, choose an isomorphism
$R(gf)_!\simeq Rg_!Rf_!$ supplied by
[proposition-composition-base-change-rf-shriek]. Transport the adjunction
for $(gf)^!$ across this isomorphism and compare it with the composite
adjunction for $f^!g^!$. Uniqueness of right adjoints gives the required
isomorphism. This is exactly the use of `CategoryTheory.Adjunction.rightAdjointUniq`
in the étale proof.

For $\Qbarl$-coefficients, apply `CategoryTheory.conjugateIsoEquiv` to the
inverse of `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl`
under the same two adjunctions. This defines the specified comparison.
