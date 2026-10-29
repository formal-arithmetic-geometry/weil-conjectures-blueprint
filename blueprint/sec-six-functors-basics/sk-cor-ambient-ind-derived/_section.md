+++
id = "sk-cor-ambient-ind-derived"
kind = "corollary"
title = "The ind-constructible derived category"
order = 2433
uses = ["sk-prop-ind-heart", "sk-def-localizing-closure"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. The full subcategory

$$
\Dic(X,\Lambda)=\{K\in\D(X_{\mathrm{proét}},\Lambda):H^n(K)\in\IndCons(X,\Lambda)\text{ for every }n\}
$$

of $\D(X_{\mathrm{proét}},\Lambda)$, with $\IndCons(X,\Lambda)$ as in [sk-prop-ind-heart], is triangulated,
closed under direct sums, and stable under the truncations $\tau_{\leq n}$, $\tau_{\geq n}$. In particular
$\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$ ([sk-def-localizing-closure]).
