+++
id = "lemma-change-coefficients-exceptional-inverse-image--5"
kind = "lemma"
title = "Exceptional inverse image: inverting the uniformizer"
order = 640010
aliases = ["bp-r195-5"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleUpperShriekExtendScalars"]
uses = ["theorem-exceptional-inverse-image", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-compact-support"]
+++
Let $E\subset\overline{\mathbf Q}_\ell$ be finite over $\mathbf Q_\ell$,
and take $\Lambda=\mathcal O_E$ and $\Lambda'=E$. For every
$K\in\Dbc(Y,\mathcal O_E)$ the comparison
$$
\beta_{f,K}:(f^!_{\mathcal O_E}K)_E\longrightarrow f^!_E(K_E)
$$
is an isomorphism in $\Dbc(X,E)$, natural in $K$. Here $\beta$ is the
adjoint transpose, under $Rf_!\dashv f^!$, of the inverse of the
compactly supported comparison in [lemma-change-coefficients-compact-support].
