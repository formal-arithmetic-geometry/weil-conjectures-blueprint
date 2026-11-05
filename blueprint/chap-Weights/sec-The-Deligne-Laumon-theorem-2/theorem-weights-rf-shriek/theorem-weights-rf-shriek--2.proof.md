+++
kind = "proof"
of = "theorem-weights-rf-shriek--2"
order = 1084002
uses = ["theorem-weights-rf-shriek--1", "definition-weights", "definition-frobenius-operator"]
+++
The constant Weil sheaf $\Qbarl$ is punctually pure of weight zero.
Placed in degree zero, it therefore belongs to $D_{\leq0}(X_0)$;
its other cohomology sheaves vanish. Apply [theorem-weights-rf-shriek--1]
to the structure morphism $a:X_0\to\Spec k_0$. Its conclusion in
degree $n$ says that $\mathcal H^n(Ra_!\Qbarl)$ is mixed of weights
at most $n$.

By definition, $H_c^n(X,\Qbarl)$ is the space of geometric global
sections of this Weil sheaf on $\Spec k_0$, with its Frobenius operator.
Every eigenvalue on these global sections is an eigenvalue of local
Frobenius at the point. The mixed weight bound gives the required
inequality. Lean implements these two steps in
`AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_toComplex_adicConstant`
and
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.hasWeightsAtMostOver_globalSections`.
