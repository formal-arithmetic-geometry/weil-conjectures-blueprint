+++
id = "sbc-def-specialization-map"
kind = "definition"
title = "Specialization map"
order = 1450
uses = ["def-weil-pbc-etale-cohomology", "sbc-def-milnor-tube", "sbc-def-strict-localization"]
+++
For $K\in D(X_{\Et})$ and the
Milnor tube $F_{\bar x,\bar t}$ of
[sbc-def-milnor-tube], the strictly henselian
$X_{(\bar x)}$ of [sbc-def-strict-localization] gives
$K_{\bar x}=R\Gamma(X_{(\bar x)},K)$; pulling back cohomology along
$F_{\bar x,\bar t}\to X_{(\bar x)}$ and using the etale cohomology
of [def-weil-pbc-etale-cohomology] gives the canonical
*specialization map*

$$
\alpha_{K,\bar x,\bar t}:K_{\bar x}\longrightarrow R\Gamma(F_{\bar x,\bar t},K).
$$
