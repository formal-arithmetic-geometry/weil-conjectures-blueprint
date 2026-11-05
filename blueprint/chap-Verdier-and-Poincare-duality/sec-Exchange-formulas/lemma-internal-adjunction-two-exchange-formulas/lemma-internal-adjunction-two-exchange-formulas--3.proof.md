+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--3"
order = 829007
uses = ["proposition-composition-open-restriction-compactifications-f", "lemma-internal-adjunction-two-exchange-formulas--2", "theorem-verdier-biduality"]
+++
For an open immersion, the internal-Hom comparison gives

$$
j^*\cHom_Y(L,\omega_Y)\simeq
\cHom_U(j^*L,j^*\omega_Y).
$$

The identification $j^!\simeq j^*$ and composition of exceptional
inverse images give $j^*\omega_Y\simeq\omega_U$, as in
[proposition-composition-open-restriction-compactifications-f].
Compose these two isomorphisms. In Lean they are the internal-Hom
comparison for open pullback and
`AlgebraicGeometry.ProEtale.CondensedRing.dualizingComplexUpperStarIso`.

For Weil complexes, use the natural form of the exchange in
[lemma-internal-adjunction-two-exchange-formulas--2] and biduality
[theorem-verdier-biduality]. Transport the adjunction
$f^*\dashv Rf_*$ through the dualities and compare its right adjoint
with $Rf_!\dashv f^!$. Uniqueness of right adjoints yields
$f^!M\simeq\mathbb D_Xf^*\mathbb D_YM$; this is
`AlgebraicGeometry.WeilComplex.nonempty_upperShriek_obj_iso`.
Apply it to $M=\mathbb D_YL$, then apply $\mathbb D_Xf^*$ to the
biduality isomorphism $L\simeq\mathbb D_Y\mathbb D_YL$.

The natural exchange used in this step is
`AlgebraicGeometry.WeilComplex.nonempty_verdierDual_derivedLowerShriek_natIso`;
its proof in the current Lean source is `sorry`.
