+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--5"
order = 640011
uses = ["proposition-inverting-ell", "lemma-change-coefficients-compact-support", "theorem-exceptional-inverse-image"]
+++
The schemes $X$ and $Y$ are Noetherian. By [proposition-inverting-ell],
extension of scalars from $\mathcal O_E$ to $E$ on both schemes is
rationalization: it localizes at morphisms whose cones are killed by a
power of $\ell$.

The comparison for $Rf_!$ is an isomorphism by
[lemma-change-coefficients-compact-support]. Apply
`CategoryTheory.Rationalization.isIso_mateEquiv_of_isLocalization` to
this isomorphism and the adjunctions $Rf_!\dashv f^!$ over
$\mathcal O_E$ and $E$. Indeed, on Hom groups out of an object obtained
by extension of scalars, its mate is the localization of the adjunction
bijection. It is therefore bijective; essential surjectivity of
rationalization and Yoneda show that the mate is an isomorphism.
By the definition of $\beta$, this is the desired comparison.
