+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--2"
order = 829006
uses = ["lemma-internal-adjunction-two-exchange-formulas--1", "theorem-exceptional-inverse-image", "proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients"]
+++
For finite coefficients, the composition isomorphism
$Ra_{X!}\simeq Ra_{Y!}Rf_!$ from
[proposition-composition-base-change-rf-shriek] identifies their right
adjoints. Evaluating at $\Lambda_S$ gives
$f^!\omega_Y\simeq\omega_X$. This is
`AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex`.
Apply [lemma-internal-adjunction-two-exchange-formulas--1] with
$L=\omega_Y$, invert its isomorphism, and apply $Rf_*\cHom_X(K,-)$ to
$f^!\omega_Y\simeq\omega_X$.

For Weil complexes, Lean uses the adjunctions for $a_X$ and $a_Y$
directly. The projection formula identifies
$Rf_!K\otimes^{\mathbf L}N$ with
$Rf_!(K\otimes^{\mathbf L}f^*N)$, and composition of compactly supported
direct images identifies
$\Hom_Y(Rf_!M,\omega_Y)$ with $\Hom_X(M,\omega_X)$.
The tensor–Hom adjunction and $f^*\dashv Rf_*$ then identify the two
represented Hom functors. Yoneda gives the required isomorphism in
`AlgebraicGeometry.WeilComplex.nonempty_iso_derivedLowerStar_of_adjunction`.
