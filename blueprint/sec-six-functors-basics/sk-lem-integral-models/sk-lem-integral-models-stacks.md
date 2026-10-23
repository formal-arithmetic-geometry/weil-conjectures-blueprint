+++
id = "det-lem-integral-models-stacks"
kind = "lemma"
title = "Comparison with the Stacks Project adic constructible category"
order = 2192
uses = ["det-prop-integral-criterion-constant-coefficients", "sk-prop-integral-criterion"]
+++
Let $X$ be a Noetherian scheme, $E/\mathbf Q_\ell$ finite, and let
$\operatorname{Res}\colon D(X_{\mathrm{proét}},\cO_{E,X})\to D(X_{\mathrm{proét}},(\cO_E)_X)$ be restriction
of scalars along the map from the constant sheaf. Let $\Dc(X,\cO_E)$ be the full subcategory of
$D(X_{\mathrm{proét}},(\cO_E)_X)$ of \stacks{09C1}: derived $\pi_E$-complete complexes $L$ such that
$L\otimes^{\mathbf L}_{\cO_E}\cO_E/\pi_E$ has finite Tor dimension and constructible cohomology
sheaves (pulled back from $X_{\mathrm{ét}}$). Then for $K\in D(X_{\mathrm{proét}},\cO_{E,X})$:
$$
K\in\Dbc(X,\cO_E)\iff\operatorname{Res}K\in\Dc(X,\cO_E),
$$
and $\operatorname{Res}$ restricts to an equivalence $\Dbc(X,\cO_E)\simeq\Dc(X,\cO_E)$.
