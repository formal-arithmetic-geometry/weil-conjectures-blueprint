+++
id = "theorem-smooth-purity-all-admissible-coefficients--4"
kind = "theorem"
title = "Purity isomorphism: algebraically closed coefficients"
order = 730008
aliases = ["bp-r220-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothOrientation", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekUnitTensorMap_of_smooth"]
uses = ["definition-tate-twists", "theorem-existence-exceptional-inverse-image", "definition-relative-dualizing-complex", "definition-constructible-sheaves"]
+++
In the shared context, the chosen orientation is an isomorphism

$$
\gamma_f:\overline{\mathbf Q}_{\ell,X}(d)[2d]\xrightarrow{\sim}
 f^!\overline{\mathbf Q}_{\ell,Y}.
$$

For every $K\in\Dbc(Y,\overline{\mathbf Q}_\ell)$, the tensor product map, defined as the exceptional adjoint of the projection formula followed by the counit, is an isomorphism

$$
\alpha_f(K):f^*K\otimes^{\mathrm L} f^!\overline{\mathbf Q}_{\ell,Y}
 \xrightarrow{\sim}f^!K.
$$

Consequently, tensoring with $\gamma_f$ and then applying $\alpha_f(K)$ gives $f^*K(d)[2d]\simeq f^!K$. The orientation uses a compatible integral lift when an invertible lift exists, and otherwise a chosen isomorphism; compatibility with all the normalizations of the human statement is not asserted.
