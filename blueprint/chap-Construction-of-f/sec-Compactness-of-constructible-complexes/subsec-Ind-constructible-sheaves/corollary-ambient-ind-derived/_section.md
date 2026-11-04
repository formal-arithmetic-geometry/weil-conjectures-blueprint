+++
id = "corollary-ambient-ind-derived"
kind = "corollary"
title = "The derived category of ind-constructible sheaves"
name_showing = false
order = 454
lean = ["AlgebraicGeometry.ProEtale.localizingClosure_boundedConstructible_le"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-ind-constructible-sheaves", "proposition-ind-constructible-sheaves"]
+++
The full subcategory

$$
\Dic(X,\Lambda)
=\{K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda):H^n(K)\in\IndCons(X,\Lambda)\text{ for every }n\}
$$

of $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is triangulated, closed under direct sums, and
stable under the truncations $\tau_{\leq n}$, $\tau_{\geq n}$. In
particular $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$.
