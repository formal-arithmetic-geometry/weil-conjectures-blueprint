+++
id = "lem-sf-proetale-neighbourhood-colimit"
kind = "lemma"
title = "The pro-étale form of the continuity statement: every class dies on the strict henselization limit"
order = 3489
uses = ["def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lem-sf-stalk-limit-acyclic"]
+++
Let $T$ be a scheme, let $\bar t\to T$ be a
geometric point of $T$ and let
$\mathcal F$ be a sheaf of $A$-modules on the
small pro-étale site $T_{\Proet}$,
that is, an object of [def-weil-pbc-proetale-modules]. Let $W\to T$ be
weakly étale and let
$\bar w\to W$ be a lift of $\bar t$, so that $(W,\bar w)$ is a pointed
pro-étale neighbourhood of $\bar t$. Then:

1. **(i)** there is a $T$-morphism
$T_{(\bar t)}\to W$ from the
strict henselization
limit $T_{(\bar t)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{T,\bar t}$
of [def-weil-pbc-strict-henselization-limit] to $W$, carrying the
closed geometric point of $T_{(\bar t)}$ to $\bar w$;
1. **(ii)** for every such morphism and every $q\geq1$ the induced map
$$
H^q\bigl(W_{\Proet},\mathcal F|_W\bigr)\longrightarrow
H^q\bigl(T_{(\bar t),\Proet},\mathcal F\bigr)
$$
is zero, its target being zero by [lem-sf-stalk-limit-acyclic](iii);
1. **(iii)** consequently every class on a pointed pro-étale neighbourhood of
$\bar t$ dies on the single pro-étale refinement
$T_{(\bar t)}\to W$, and the colimit of the groups
$H^q(W_{\Proet},\mathcal F|_W)$, $q\geq1$, over the pointed pro-étale
neighbourhoods of $\bar t$ is zero.

## Proof

*(i).* By Stacks Project, Pro-étale Cohomology, Lemma 61.18.4,
[Tag 0993](https://stacks.math.columbia.edu/tag/0993) the scheme
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{T,\bar t}$ is an object of
$T_{\Proet}$, the
small pro-étale site of
[def-weil-pbc-proetale-site], and is an initial object of the category of
pro-étale neighbourhoods of $\bar t$, the input of its proof being
Olivier's theorem, Stacks Project, More on Algebra, Theorem 15.106.24,
[Tag 092Z](https://stacks.math.columbia.edu/tag/092Z). Initiality
supplies a $T$-morphism $T_{(\bar t)}\to W$ compatible with the chosen
geometric points, and by [def-weil-pbc-strict-henselization-limit] the
scheme $T_{(\bar t)}$ is the spectrum of the strict henselization, the limit
of the affine pointed étale neighbourhoods of $\bar t$.

*(ii).* The functor $G\mapsto G(T_{(\bar t)})$ on sheaves of
$A$-modules on $T_{\Proet}$, that is, on the objects of
[def-weil-pbc-proetale-modules], is exact, being the geometric-point
stalk functor at $\bar t$: this is clause (ii) of
[lem-sf-stalk-limit-acyclic], and by clause (iii) of the same lemma
$H^q(T_{(\bar t),\Proet},\mathcal F)=0$ for every $q>0$ and every sheaf
$\mathcal F$ of $A$-modules on $T_{\Proet}$. Hence the displayed map has
zero target and is zero.

*(iii).* The morphism of (i) is a refinement of the pointed pro-étale
neighbourhood $(W,\bar w)$ whose coefficient sheaf is $\mathcal F$, and by
(ii) it kills every class in every degree $q\geq1$. Thus every element of
every term of the colimit is killed by a structure map, namely by the one to
the term $T_{(\bar t)}$, and the colimit of the groups with zero target is
zero.
