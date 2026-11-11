+++
id = "lemma-descent-finite-coefficient-field--1"
kind = "lemma"
title = "Descent to a finite coefficient field (1)"
name_showing = false
order = 285003
aliases = ["bp-r085-1"]
lean = ["AlgebraicGeometry.ProEtale.coefficient_finite_descent_hom", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj"]
+++
For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars
induces an isomorphism

$$
\varinjlim_{E'\supset E}
\Hom_{D(X_{\mathrm{pro}\acute{e}t},E')}(C_{E'},D_{E'}[r])
\;\xrightarrow{\ \sim\ }\;
\Hom_{D(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)}(C_{\overline{\mathbf Q}_\ell},D_{\overline{\mathbf Q}_\ell}[r]),
$$

the colimit running over finite extensions $E'$ of $E$ in $\overline{\mathbf Q}_\ell$.
