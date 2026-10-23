+++
id = "det-sp-trace-transitivity-steps"
kind = "lemma"
title = "Transitivity of the smooth trace, step by step"
order = 3062
uses = ["det-sp-composition-comparisons", "det-sp-composition-factors", "det-sp-trace-basic"]
+++
In the situation of the sketch, write $L=g^*K(e)[2e]$. Then, after the
identifications $R(g\circ f)_!\simeq Rg_!Rf_!$, $(g\circ f)^*\simeq f^*g^*$ and
twist additivity:

1. by naturality of $\operatorname{Tr}_f$ in its argument, applied to
   $\gamma_g(K):L\to g^!K$,
   $$
   \gamma_g(K)\circ\operatorname{Tr}_f(L)=\operatorname{Tr}_f(g^!K)\circ Rf_!\bigl(f^*\gamma_g(K)(d)[2d]\bigr);
   $$
2. $\operatorname{Tr}_g(K)\circ Rg_!\operatorname{Tr}_f(L)
   =\varepsilon_g(K)\circ Rg_!\varepsilon_f(g^!K)\circ Rg_!Rf_!\bigl(\gamma_f(g^!K)\circ f^*\gamma_g(K)(d)[2d]\bigr)$;
3. the right side of (2) equals $\varepsilon_{g\circ f}(K)\circ R(g\circ f)_!\gamma_{g\circ f}(K)=\operatorname{Tr}_{g\circ f}(K)$.
