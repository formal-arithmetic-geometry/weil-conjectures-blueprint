+++
kind = "proof"
of = "corollary-verdier-exchange-formulas--1"
order = 847009
uses = ["lemma-internal-adjunction-two-exchange-formulas", "proposition-composition-base-change-rf-shriek"]
+++
The finite-coefficient tensor–Hom exchange in
[lemma-internal-adjunction-two-exchange-formulas], evaluated at
$L=\omega_Y$, gives

$$
Rf_*\cHom_X(K,f^!\omega_Y)\simeq\cHom_Y(Rf_!K,\omega_Y).
$$

The composition law for compact direct image in
[proposition-composition-base-change-rf-shriek] identifies the left
adjoints of $f^!a_Y^!$ and $a_X^!$. Uniqueness of right adjoints,
evaluated at $\Lambda_S$, therefore gives
$f^!\omega_Y\simeq\omega_X$. This is
`AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex`.
Invert the tensor–Hom exchange and apply $Rf_*\cHom_X(K,-)$ to this
last isomorphism. The resulting composite is the claimed exchange.
