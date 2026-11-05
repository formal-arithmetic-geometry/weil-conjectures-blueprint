+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--9"
order = 865019
uses = ["theorem-trace-isomorphism-top-degree--1", "corollary-degreewise-duality-over-fields", "theorem-poincare-duality-frobenius", "definition-tate-twists", "proposition-forgetting-supports-composition"]
+++
Apply the Frobenius-invariant perfect pairing
$$
H_c^{2d}(X,\QbarX)\times H^0(X,\QbarX(d))\longrightarrow\overline{\mathbf Q}_\ell
$$
provided by `AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_adicConstant`. By [theorem-trace-isomorphism-top-degree--1], the untwisted degree-zero group is a line with Frobenius the identity; the Tate twist multiplies this action by $q^{-d}$. Choose a vector $u$ corresponding to $1$ in the twisted line. Perfectness makes $z\mapsto\langle z,u\rangle$ an isomorphism, and Frobenius invariance gives
$$
\langle Fz,u\rangle=q^d\langle z,u\rangle.
$$
Twisting the compactly supported top group by $d$ cancels this multiplier and gives $t_d$. If $X_0$ is proper, transport the untwisted isomorphism through the Frobenius-equivariant comparison $H_c^{2d}\simeq H^{2d}$ of [proposition-forgetting-supports-composition]. Lean assembles these steps in `AlgebraicGeometry.WeilSheaf.poincareDuality_compactlySupportedCohomology_adicConstant`, then adds the degree-zero isomorphism.
