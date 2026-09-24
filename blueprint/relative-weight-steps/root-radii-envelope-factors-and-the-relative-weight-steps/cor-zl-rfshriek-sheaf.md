+++
id = "cor-zl-rfshriek-sheaf"
kind = "theorem"
title = "Cohomology-sheaf form of the direct-image theorem"
order = 4334
tags = ["latex:corollary"]
uses = ["def-weil-complex-weights", "def-weil-pbc-qbar-category", "def-weil-punctual-weights", "thm-zl-wme-deligne-estimate"]
+++
If $f:X_0\to Y_0$ is separated and of finite type and a Weil sheaf
$\mathcal F$ is $\iota$-mixed of weights at most $w$, then
$R^if_!\mathcal F$ is $\iota$-mixed of weights at most $w+i$ for
every $i$.

## Proof

Regard $\mathcal F$ as a complex concentrated in degree zero. The
definition [def-weil-complex-weights] identifies its upper bound
with membership in $D_{\le w}$. Applying
[thm-zl-wme-deligne-estimate] and reading the $i$th cohomology
sheaf gives the asserted bound $w+i$ (in the punctual sense of
[def-weil-punctual-weights]).
