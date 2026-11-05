+++
id = "proposition-integral-constructibility-criterion--1"
kind = "proposition"
title = "The residue criterion and finite Tor amplitude"
name_showing = false
order = 246001
aliases = ["bp-r073-1"]
lean = ["AlgebraicGeometry.ProEtale.internal_integral_residue_criterion"]
uses = ["definition-small-pro-etale-site", "definition-derived-adic-completeness", "definition-constructible-sheaves"]
+++
Let $\ell$ be prime, let $E/\mathbf Q_\ell$ be finite, and let $X$ be
Noetherian. For every $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, put

$$
K_1=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathbf F_{E,X},
\qquad \mathbf F_E=\mathcal O_E/\pi_E.
$$

Then

$$
K\in\Dbc(X,\mathcal O_E)
\quad\Longleftrightarrow\quad
K\text{ is derived complete and }K_1\in\Dctf(X,\mathbf F_E).
$$

Here completeness is that of [definition-derived-adic-completeness],
and the residue condition includes both bounded constructible cohomology
and finite Tor amplitude, as in [definition-constructible-sheaves].
Moreover,

$$
\Dbc(X,\mathcal O_E)=\Dctf(X,\mathcal O_E).
$$
