+++
id = "det-ambient-ind-derived-sums"
kind = "lemma"
title = "Sums and truncations in $\\Dic(X,\\Lambda)$; the localizing closure"
lean = ["AlgebraicGeometry.ProEtale.indConstructibleDerived_sums_and_truncations"]
order = 2435
uses = ["det-ambient-ind-derived-triangulated", "sk-def-localizing-closure", "sk-prop-ind-heart"]
+++
Let $\Lambda=E$ or $\Qlb$.

1. For any family $(K_s)$ in $\D(X_{\mathrm{proét}},\Lambda)$ and every $n$,
   $H^n(\bigoplus_sK_s)=\bigoplus_sH^n(K_s)$; hence $\Dic(X,\Lambda)$ is closed under direct sums.
2. For $K\in\Dic(X,\Lambda)$, $\tau_{\leq n}K$ and $\tau_{\geq n}K$ lie in $\Dic(X,\Lambda)$.
3. $\Dbc(X,\Lambda)\subset\Dic(X,\Lambda)$, and $\Loc(\Dbc(X,\Lambda))\subset\Dic(X,\Lambda)$.
