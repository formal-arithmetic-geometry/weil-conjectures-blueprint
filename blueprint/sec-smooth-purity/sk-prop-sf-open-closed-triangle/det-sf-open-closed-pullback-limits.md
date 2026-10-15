+++
id = "det-sf-open-closed-pullback-limits"
kind = "lemma"
title = "Closed inverse image preserves limits"
uses = ["def-exc-closed-site-lift", "lem-exc-closed-site-adjunction", "lem-exc-closed-inverse-image-formula", "lem-exc-closed-localization"]
+++
Let $X$ be quasi-compact and quasi-separated, $i:Z\hookrightarrow X$ a
closed immersion with quasi-compact open complement, and $B$ a sheaf of rings
on $X_{\mathrm{proét}}$. Then:

1. for every weakly contractible affine $V$ in the affine ind-étale basis of
$Z_{\mathrm{proét}}$ (over an affine open of $X$) and every $B$-module sheaf $F$,
the canonical map $F(v(V))\to(i^*F)(V)$ is an isomorphism, where $v(V)$ is the
henselian lift of [def-exc-closed-site-lift];
2. the functor $i^*$ from $B$-module sheaves on $X_{\mathrm{proét}}$ to
$i^*B$-module sheaves on $Z_{\mathrm{proét}}$ is exact and preserves all small
limits and all small colimits.
