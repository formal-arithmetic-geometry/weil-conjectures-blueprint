+++
id = "sk-cor-ambient-ind-derived"
kind = "corollary"
title = "The ind-constructible derived category"
order = 1524
uses = ["sk-prop-ind-heart", "sk-def-localizing-closure"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. The full subcategory

$$
\Dic(X,\Lambda)=\{K\in\D(X_{\mathrm{proét}},\Lambda):H^n(K)\in\IndCons(X,\Lambda)\text{ for every }n\}
$$

of $\D(X_{\mathrm{proét}},\Lambda)$ is triangulated, closed under direct sums, and stable under the truncations
$\tau_{\leq n}$, $\tau_{\geq n}$. In particular $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$
([sk-def-localizing-closure]).

Objects of $\Loc(\Dbc(X,\Lambda))$ need not be bounded, and their truncations need not lie in
$\Loc(\Dbc(X,\Lambda))$; truncation arguments therefore take place in $\Dic(X,\Lambda)$.
