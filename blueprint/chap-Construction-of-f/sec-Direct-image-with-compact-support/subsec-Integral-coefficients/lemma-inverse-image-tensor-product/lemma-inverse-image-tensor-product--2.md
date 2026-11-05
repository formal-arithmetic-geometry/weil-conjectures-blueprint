+++
id = "lemma-inverse-image-tensor-product--2"
kind = "lemma"
title = "Tensor product"
order = 494004
aliases = ["bp-r149-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.isMonoidal_boundedConstructible"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
Let $\ell$ be prime, let $k$ be a field with
$\operatorname{char}(k)\ne\ell$, and let
$E\subset\overline{\mathbf Q}_\ell$ be finite over $\mathbf Q_\ell$.
For a scheme $X$ of finite type over $k$, $\Dbc(X,\mathcal O_E)$ contains
$\mathcal O_{E,X}$ in degree $0$ and is stable under the uncompleted derived
tensor product: if $K,L\in\Dbc(X,\mathcal O_E)$, then
$$
K\otimes^{\mathbf L}_{\mathcal O_{E,X}}L\in\Dbc(X,\mathcal O_E).
$$
Thus it is a monoidal subcategory of $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$.
