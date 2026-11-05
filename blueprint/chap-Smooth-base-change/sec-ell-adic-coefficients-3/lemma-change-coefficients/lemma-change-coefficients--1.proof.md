+++
kind = "proof"
of = "lemma-change-coefficients--1"
order = 698002
uses = ["definition-change-of-coefficients-maps", "definition-pro-etale-base-change-map", "lemma-inverse-image-coefficient-sheaves"]
+++
Apply the composition compatibility to $g\circ f'$ and $f\circ g'$.
Together with the equality of these composites, it says that the cube of
pullback comparisons commutes. In Lean this is
`AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIso_cube`.

The pushforward comparison $\rho_h$ is the mate of $\alpha_h^{-1}$ under
the two pullback–pushforward adjunctions, by
`CategoryTheory.Adjunction.pushHomOfComapIso_eq_mateEquiv`. Taking mates
of the commutative cube therefore gives a commutative square between the
two base change arrows. Its left vertical map is the composite

$$
T_{Y'}g^*Rf_*K\xrightarrow{\alpha_g}g^*T_YRf_*K
\xrightarrow{g^*\rho_f}g^*Rf_*T_XK,
$$

and its right vertical map is

$$
T_{Y'}Rf'_*g'^*K\xrightarrow{\rho_{f'}}Rf'_*T_{X'}g'^*K
\xrightarrow{Rf'_*\alpha_{g'}}Rf'_*g'^*T_XK.
$$

Both are isomorphisms by the assumptions. This gives the required
isomorphism of arrows, as in
`CategoryTheory.Adjunction.nonempty_arrowIso_map_exchangeRight_app`.

For the bounded constructible version, pullback preserves the indicated
subcategories, and preservation by pushforward and extension of scalars
is assumed. The inclusions into the ambient derived categories are fully
faithful. Under these inclusions, the restricted pullback comparisons
agree with the ambient comparisons: expand them into composition
isomorphisms and the equality $g\circ f'=f\circ g'$. The restricted
adjunctions then give the same exchange morphisms. Transporting the cube
argument along the inclusions proves the assertion, by
`CategoryTheory.Adjunction.nonempty_arrowIso_lift_map_app_of_eq_exchangeRight_restrictFullyFaithful`.
