+++
id = "cor-zl-rfshriek-sheaf"
kind = "theorem"
title = "Cohomology-sheaf form of the direct-image theorem"
order = 3054
uses = ["def-weil-complex-weights", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "lem-zl-finite-pushforward", "lem-zl-open-closed-weight", "lem-zl-shriek-composition", "thm-zl-relative-line-step", "thm-zl-relative-noether"]
+++
If $f:X_0\to Y_0$ is separated and of finite type and a Weil sheaf
$\mathcal F$ is $\iota$-mixed of weights at most $w$, then
$R^if_!\mathcal F$ is $\iota$-mixed of weights at most $w+i$ for
every $i$.

## Proof

Regard $\mathcal F$ as a complex concentrated in degree zero. The
definition [def-weil-complex-weights] identifies its upper bound
with membership in $D_{\le w}$. Noetherian induction and the localization rule
[lem-zl-open-closed-weight] reduce to the source and target strata
of [thm-zl-relative-noether]. The finite first arrow
$\nu$ preserves the upper weight bound by
[lem-zl-finite-pushforward]; every subsequent affine-line
projection preserves it by [thm-zl-relative-line-step]. Repeated
use of the composition isomorphism [lem-zl-shriek-composition]
gives the bound for the whole factorization. The same localization
induction glues all strata, so $Rf_!\mathcal F\in D_{\le w}(Y_0)$;
reading the $i$th cohomology
sheaf gives the asserted bound $w+i$ (in the punctual sense of
[def-weil-punctual-weights]).
