+++
id = "lemma-descent-finite-coefficient-field--1"
kind = "lemma"
title = "Descent to a finite coefficient field (1)"
name_showing = false
order = 285003
aliases = ["bp-r085-1"]
lean = ["AlgebraicGeometry.ProEtale.coefficient_finite_descent_hom", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "lemma-constructible-sheaves--8"]
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
