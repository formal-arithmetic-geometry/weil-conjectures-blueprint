+++
kind = "proof"
of = "lemma-double-dual-geometric-generic-fibre--1"
order = 841002
uses = ["proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-f-shriek-finite-coefficients", "lemma-verdier-duality-preserves-constructibility", "lemma-restriction-geometric-generic-fibre"]
+++
Put $\omega_{X/B}=f^!A_B$ and $\omega_p=p^!A_B$. Composition of exceptional
inverse images ([proposition-composition-open-restriction-compactifications-f])
and the fact that an invertible tensor factor passes through $f^!$ give

$$
\omega_X\simeq\omega_{X/B}\otimes_A^{\mathbf L}f^*\omega_B,
\qquad
\omega_{X/B}\simeq i^!\omega_p.
$$

This is `AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_comp_of_isInvertible`.
The complex $\omega_p$ is bounded constructible by the smooth case of
[theorem-f-shriek-finite-coefficients]. Apply the closed-support comparison
of [lemma-restriction-geometric-generic-fibre] to $i^!\omega_p$, then the
smooth base change of [proposition-exceptional-inverse-image-smooth-morphism]
to $\omega_p$. Composition on $X'$ gives

$$
g^*\omega_{X/B}
\simeq g^*i^!\omega_p
\simeq i'^!g_P^*\omega_p
\simeq i'^!\omega_{p'}
\simeq\omega_{X'/T}.
$$

Since pullback preserves tensor products and invertible objects, we may
take $L=g^*f^*\omega_B$.

For the second assertion, $\omega_X$ is bounded constructible by the
bounded-constructibility part of [theorem-f-shriek-finite-coefficients].
For the preservation in [lemma-verdier-duality-preserves-constructibility]
over the perfect field $k$, Lean uses
`AlgebraicGeometry.Etale.constructibleFiniteTor_and_torAmplitudeIn_verdierDual_of_perfectField`
to show that $\mathbb D_XK$ has finite Tor amplitude before using biduality.
Thus the internal-Hom comparison of [lemma-restriction-geometric-generic-fibre]
is an isomorphism both at $(K,\omega_X)$ and at
$(\mathbb D_XK,\omega_X)$; bounded constructibility of $\omega_X$ is supplied by
`AlgebraicGeometry.Etale.boundedConstructible_rightDerivedUpperShriek`.

The two comparisons, together with the symmetry compatibility of $g^*$,
compare the double-dual maps defined by evaluation. Changing the dualizing
object by the displayed isomorphism reduces the assertion to removing the
invertible tensor factor $L$. Tensoring by $L$ is an equivalence; the
isomorphisms
$\cHom(N,\omega_{X'/T})\otimes_A^{\mathbf L}L
\simeq\cHom(N,\omega_{X'/T}\otimes_A^{\mathbf L}L)$
identify the corresponding duality adjunctions up to this equivalence.
Their units are isomorphisms at the same objects. The cancellation of $L$ is
the formal lemma
`CategoryTheory.MonoidalClosed.isIso_toIhomIhom_tensor_right_iff`. This proves
the desired equivalence, as formalized by
`AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff`.
