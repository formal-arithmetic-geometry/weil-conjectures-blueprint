+++
id = "corollary-degreewise-duality-over-fields"
kind = "corollary"
title = "Degreewise duality over fields"
order = 853
lean = ["AlgebraicGeometry.Etale.TateOrientation.isPerfPair_degreewisePoincarePairing", "AlgebraicGeometry.Etale.TateOrientation.isPerfPair_degreewisePoincarePairing_of_isProper", "AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_dual", "AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.poincareDuality_compactlySupportedCohomology_adicConstant"]
+++
Let $X/k$ be smooth and separated of pure dimension $d$, with $k$
algebraically closed, let $\Lambda$ be a field (a finite coefficient
field, $\mathbf Q_\ell$, $E$ or $\overline{\mathbf Q}_\ell$), let $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, and put
$K^\vee=\cHom_X(K,\Lambda_X)$. For every $i$ the pairings induced by
$\beta_K$,

$$
H_c^i(X,K)\times H^{2d-i}(X,K^\vee(d))\longrightarrow\Lambda,
\qquad
H_c^i(X,K)\times H^{2d-i}(X,K^\vee)\longrightarrow\Lambda(-d),
$$

are perfect pairings of finite-dimensional vector spaces. If $X$ is
proper, the same holds with $H_c^i$ replaced by $H^i$.
