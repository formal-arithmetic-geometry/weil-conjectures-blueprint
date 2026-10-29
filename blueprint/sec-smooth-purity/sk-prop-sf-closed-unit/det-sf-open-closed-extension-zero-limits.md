+++
id = "det-sf-open-closed-extension-zero-limits"
kind = "lemma"
title = "Extension by zero preserves products and derived limits"
order = 3191
uses = ["det-sf-open-closed-pullback-limits", "det-sf-open-closed-sequence-ring-sheaf"]
+++
In the situation of [sk-prop-sf-open-closed-triangle], let $j:U\hookrightarrow X$
be a quasi-compact open immersion with closed complement $i:Z\hookrightarrow X$
and $B$ a sheaf of rings on $X_{\mathrm{proét}}$. Then:

1. for every $K\in D(U_{\mathrm{proét}},j^*B)$ there is a distinguished
triangle, functorial in $K$,
$$
j_!K\longrightarrow Rj_*K\longrightarrow i_*i^*Rj_*K\longrightarrow j_!K[1];
$$
2. $j_!:D(U_{\mathrm{proét}},j^*B)\to D(X_{\mathrm{proét}},B)$ preserves
products and derived inverse limits $R\varprojlim$ of sequences;
3. on module sheaves, $j_!$ preserves products.
