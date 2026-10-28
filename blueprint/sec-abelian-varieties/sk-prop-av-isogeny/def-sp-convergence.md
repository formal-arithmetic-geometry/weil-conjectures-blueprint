+++
id = "def-sp-convergence"
kind = "definition"
title = "Convergence of a couple"
lean = ["CategoryTheory.ExactCouple.IsRegular", "CategoryTheory.ExactCouple.IsComplete", "CategoryTheory.ExactCouple.ConvergenceData", "CategoryTheory.ExactCouple.ConvergesTo", "CategoryTheory.ExactCouple.abutmentConvergenceData", "CategoryTheory.ExactCouple.convergesTo_abutmentFiltration"]
order = 514
uses = ["def-sp-exact-couple", "def-sp-filtration"]
+++
In the situation of [def-sp-exact-couple], regard all cycle and boundary
objects as subobjects of the initial page $E_2$. Set $Z_2=E_2$, $B_2=0$.
Given $E_r=Z_r/B_r$, define $Z_{r+1}\subseteq Z_r$ as the inverse image of
$\ker d_r$, and $B_{r+1}\subseteq Z_r$ as the inverse image of
$\operatorname{im}d_r$ under $Z_r\twoheadrightarrow E_r$, component by
component. Thus $E_{r+1}=Z_{r+1}/B_{r+1}$, the $Z_r$ decrease, and the $B_r$
increase inside $E_2$. When these limits exist, put
$Z_\infty=\bigcap_rZ_r$, $B_\infty=\bigcup_rB_r$, and
$E_\infty=Z_\infty/B_\infty$. The couple is *regular* if at every $(p,q)$
the differentials $d_r$ arriving at $(p,q)$ vanish for $r\gg0$, that is,
each $B_r^{p,q}\subseteq E_2^{p,q}$ is eventually constant. It is *complete*
if the subobjects $\operatorname{im}(\alpha^r:D^{p+r,q-r}\to D^{p,q})$ have
zero intersection for every $(p,q)$.

Let $(A^n)_{n\in\mathbb Z}$ be objects with filtrations [def-sp-filtration]
$F^\bullet A^n$, and let $\iota^{p,q}:D^{p,q}\to A^{p+q}$ be morphisms (the
structure maps of the *abutment*). Write $(D^{(N)},E^{(N)},\alpha^{(N)},f^{(N)},g^{(N)})$ for the
$N$-th derived couple, so that $E^{(N)}$ is the page $E_{N+2}$ (for a couple
started at the page $r_0$, as in the general form of [def-sp-exact-couple],
read $E_{N+r_0}$ throughout),
$D^{(N)p,q}\subseteq D^{p,q}$, and $g^{(N)}:D^{(N)p-N,q+N}\to E^{(N)p,q}$. The
spectral sequence of the couple *converges to the filtrations $F$ of $A$
along $\iota$* if for every $(p,q)$ there is an $N_0$ such that for every
$N\geq N_0$ the differentials of the page $E_{N+2}$ leaving and arriving at
$(p,q)$ vanish (so that the entry has reached its stable value
$E_\infty^{p,q}$), and there is an isomorphism
$\theta_N:E^{(N)p,q}\xrightarrow{\sim}\operatorname{gr}^pA^{p+q}$ such that
$\theta_N\circ g^{(N)}$ is the map induced by the composite
$D^{(N)p-N,q+N}\subseteq D^{p-N,q+N}\xrightarrow{\iota}A^{p+q}$, which
factors through $F^pA^{p+q}$. In particular
$E_\infty^{p,q}\cong\operatorname{gr}^pA^{p+q}$, compatibly with the
structure maps.
