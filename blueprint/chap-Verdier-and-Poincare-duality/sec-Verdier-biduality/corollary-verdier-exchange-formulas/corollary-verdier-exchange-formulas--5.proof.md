+++
kind = "proof"
of = "corollary-verdier-exchange-formulas--5"
order = 847010
uses = ["lemma-internal-adjunction-two-exchange-formulas", "proposition-composition-base-change-rf-shriek", "proposition-construction-independence-rf-shriek"]
+++
Use the natural tensor–Hom isomorphism in
[lemma-internal-adjunction-two-exchange-formulas], evaluated at
$\omega_X$. The composition law in
[proposition-composition-base-change-rf-shriek], followed by uniqueness
of right adjoints, supplies $j^!\omega_X\simeq\omega_U$.

The compactification $U\xrightarrow{j}X\xrightarrow{\mathrm{id}}X$
and independence of compactification in
[proposition-construction-independence-rf-shriek] identify $Rj_!$ with
extension by zero. In Lean this identification is
`AlgebraicGeometry.Etale.rightDerivedLowerShriekIsoOfIsOpenImmersion`.
Substitute these two identifications in the tensor–Hom isomorphism.
Its naturality in the first argument gives the naturality of the
resulting exchange. This is precisely the specialization of
`AlgebraicGeometry.Etale.verdierDualLowerShriekIso` used in the proof
that the double-dual morphism commutes with open restriction.
