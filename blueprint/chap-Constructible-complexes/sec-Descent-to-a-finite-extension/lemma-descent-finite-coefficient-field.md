+++
id = "lemma-descent-finite-coefficient-field"
kind = "lemma"
title = "Descent to a finite coefficient field"
order = 285
lean = ["AlgebraicGeometry.ProEtale.finiteCoefficientDescentTwoColimit", "AlgebraicGeometry.ProEtale.coefficient_finite_descent_hom", "AlgebraicGeometry.ProEtale.coefficient_finite_descent_objects"]
+++
1. For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars
   induces an isomorphism
   $$
   \varinjlim_{E'\supset E}
   \Hom_{D(X_{\mathrm{pro}\acute{e}t},E')}(C_{E'},D_{E'}[r])
   \;\xrightarrow{\ \sim\ }\;
   \Hom_{D(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)}(C_{\overline{\mathbf Q}_\ell},D_{\overline{\mathbf Q}_\ell}[r]),
   $$
   the colimit running over finite extensions $E'$ of $E$ in $\overline{\mathbf Q}_\ell$.
2. Every object of $\Dbc(X,\overline{\mathbf Q}_\ell)$ is isomorphic to $K_{\overline{\mathbf Q}_\ell}$ for
   some $K\in\Dbc(X,E)$ and some finite $E/\mathbf Q_\ell$.
