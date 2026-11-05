+++
kind = "proof"
of = "lemma-finite-quasi-finite-direct-images--3"
order = 1321006
uses = ["lemma-finite-morphisms", "proposition-composition-base-change-rf-shriek", "theorem-grothendieck-lefschetz-trace-formula"]
+++
Lean first proves preservation of punctual purity for $R^0h_!$ along
any separated quasi-finite morphism $h$. Zariski's main theorem,
exact extension by zero and exact finite direct image
([lemma-finite-morphisms]) show that $Rh_!F$ is concentrated in
degree zero. This vanishing is proved without weights in
`AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite`.

For a scheme quasi-finite over $k_0$, the trace formula
[theorem-grothendieck-lefschetz-trace-formula] now computes the traces
of every positive power of Frobenius on $H_c^0$. These traces determine
its local polynomial as a product of the local polynomials of the
stalks, with the variable replaced by the appropriate power.
Apply this computation to the fibre over a closed point $y$ and to
$\operatorname{Spec}\kappa(y)$. Compact-support base change and
composition ([proposition-composition-base-change-rf-shriek]) identify
the two $H_c^0$ groups. Cancelling the substitution
$T\mapsto T^{[\kappa(y):k_0]}$ gives

$$
\det(1-T\Frob_y\mid(R^0h_!F)_{\bar y})
=\prod_{z\mapsto y}\det(1-T^{e_z}\Frob_z\mid F_{\bar z}),
\qquad e_z=[\kappa(z):\kappa(y)].
$$

This is
`AlgebraicGeometry.WeilSheaf.exists_charpolyRev_stalk_higherLowerShriek_zero`.
Every eigenvalue $\beta$ on the left has $\beta^{e_z}=\alpha$ for
an eigenvalue $\alpha$ at some $z$ above $y$. Since $e_z>0$ and
$q_z=q_y^{e_z}$, purity gives

$$
|\iota(\beta)|^{e_z}=|\iota(\alpha)|
=q_z^{w/2}=q_y^{e_zw/2},
$$

so $|\iota(\beta)|=q_y^{w/2}$. This proves
`AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.higherLowerShriek_zero_of_quasiFinite`.
Finally, a finite morphism $g$ is proper, so $g_*F\simeq R^0g_!F$
by `AlgebraicGeometry.WeilSheaf.lowerStarIsoHigherLowerShriekZero`.
Transporting purity through this isomorphism proves the assertion.
