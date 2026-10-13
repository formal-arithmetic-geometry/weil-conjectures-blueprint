+++
id = "sk-i-global-additivity"
kind = "proposition"
title = "Compact trace additivity"
order = 2716
uses = ["sk-d-operator", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-p-trace", "sk-prop-sf-open-closed-triangle", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.trace_globalOperator_eq_trace_add_trace"]
tags = ["sketch"]
+++
For a closed immersion $i_0:Z_0\hookrightarrow X_0$ and its open
complement $j_0:U_0\hookrightarrow X_0$, the induced
Frobenius coefficient morphisms on the functorial
compact localization triangle satisfy

$$
\tr_A(F_{c,m},R\Gamma_c(X,K))=
\tr_A(F_{c,m},R\Gamma_c(U,j^*K))+
\tr_A(F_{c,m},R\Gamma_c(Z,i^*K)).
$$

These are traces of perfect complexes; invertibility
of the coefficient morphism is unnecessary.
