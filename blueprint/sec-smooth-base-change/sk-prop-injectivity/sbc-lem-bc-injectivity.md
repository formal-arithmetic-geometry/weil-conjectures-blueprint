+++
id = "sbc-lem-bc-injectivity"
kind = "lemma"
title = "Injectivity of the critical map and its cokernel"
order = 1440
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lemma-weil-pbc-five-lemma-transfer", "lemma-weil-pbc-leray-acyclicity", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-bc-naturality"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property], assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q-1)$ holds universally (in the
single degree $q-1$).
Let $S'\to S$ be a morphism, $f':X'=X\times_SS'\to S'$ the base change,
$g:T\to S'$ a quasi-compact and quasi-separated morphism, and
$h:Y=X'\times_{S'}T\to X'$, $e:Y\to T$ the projections. Then for
every abelian sheaf $\mathcal F$ on $T_{\Et}$ annihilated by $n$:

1. the base-change map
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is
injective;
1. if $\mathcal F\subset\mathcal G$ with $\mathcal G$ annihilated by
$n$, then
$$
\operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal F\to
R^qh_*e^{-1}\mathcal F\bigr)
\subset\operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal G\to
R^qh_*e^{-1}\mathcal G\bigr);
$$
1. if in (2) the sheaf $\mathcal G$ is an injective sheaf of
$\mathbf Z/n\mathbf Z$-modules, then
$$
\operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal F\to
R^qh_*e^{-1}\mathcal F\bigr)
\subset R^qh_*e^{-1}\mathcal G.
$$
