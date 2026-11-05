+++
id = "theorem-smooth-purity-all-admissible-coefficients--9"
kind = "theorem"
title = "Base change"
order = 730018
aliases = ["bp-r220-9"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange"]
uses = ["definition-tate-twists", "theorem-existence-exceptional-inverse-image", "definition-exceptional-base-change-map"]
+++
In the shared context, consider a cartesian square with maps $g':X'\to X$, $f':X'\to Y'$, and $g:Y'\to Y$, where $X'$ and $Y'$ are also separated and of finite type over $k$, and $f'$ is smooth of pure relative dimension $d$. Put $T_X=\overline{\mathbf Q}_{\ell,X}(d)[2d]$ and similarly for $X'$. There exists an isomorphism

$$
\tau:g'^*T_X\xrightarrow{\sim}T_{X'}
$$

such that

$$
f'^!(\eta_g)\circ\beta\circ g'^*\gamma_f
 =\gamma_{f'}\circ\tau,
$$

where $\beta$ is the exceptional base change map at $\overline{\mathbf Q}_{\ell,Y}$ and $\eta_g:g^*\overline{\mathbf Q}_{\ell,Y}\simeq\overline{\mathbf Q}_{\ell,Y'}$ is the unit comparison. The isomorphism $\tau$ is not prescribed to be the canonical pullback comparison for Tate twists.
