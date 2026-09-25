+++
id = "lem-sf-etale-neighbourhoods-not-cofinal"
kind = "lemma"
title = "The pointed étale neighbourhoods are not cofinal among the pointed pro-étale ones"
order = 2160
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "lem-sf-proetale-neighbourhood-colimit", "lemma-weil-pbc-affine-neighbourhood-cofinal", "thm-sf-continuity-arbitrary-sheaves-vanishing"]
+++
Let $k$ be a field that is not separably closed, let $\Omega$ be an
algebraically closed field containing $k$, let
$\bar v:\operatorname{Spec}\Omega\to\operatorname{Spec}k$ be the resulting
geometric point, and let
$K\subseteq\Omega$ be an infinite separable extension of $k$, for instance
the separable closure of $k$ in $\Omega$. Then:

1. **(i)** $\operatorname{Spec}K\to\operatorname{Spec}k$ is weakly étale,
and with the lift of $\bar v$ given by the inclusion $K\subseteq\Omega$ the
pair $(\operatorname{Spec}K,\bar v')$ is a pointed
pro-étale neighbourhood of
$\bar v$;
1. **(ii)** there is no $k$-morphism $U\to\operatorname{Spec}K$ with
$U\to\operatorname{Spec}k$ étale and
$U$ nonempty; in particular no
pointed étale neighbourhood of $\bar v$ in the sense of
[def-weil-pbc-pointed-etale-neighbourhoods] admits a morphism to
$(\operatorname{Spec}K,\bar v')$;
1. **(iii)** consequently the colimit of the groups
$H^q(U_{\Proet},\mathcal F|_U)$ over the pointed étale neighbourhoods of
$\bar v$ is not related to the colimit over the pointed pro-étale
neighbourhoods computed in [lem-sf-proetale-neighbourhood-colimit] by a
cofinality argument, and the vanishing recorded there does not descend to the
étale system of $(\mathrm{C}_q)$ of
[thm-sf-continuity-arbitrary-sheaves-vanishing].

## Proof

*(i).* Write $K=\varinjlim_{\alpha}K_{\alpha}$ as the filtered colimit
of the finite subextensions $K_{\alpha}\subseteq K$ of $k$ inside $K$.
Each $k\to K_{\alpha}$ is finite separable, hence étale by Stacks Project,
Algebra, Lemma 10.143.4,
[Tag 00U3](https://stacks.math.columbia.edu/tag/00U3). An étale ring
map is weakly étale and a filtered colimit of weakly étale maps is weakly
étale, so $k\to K$ is weakly étale, that is,
$\operatorname{Spec}K$ is an object of the
small pro-étale site of
$\operatorname{Spec}k$; and the composite
$\operatorname{Spec}\Omega\to\operatorname{Spec}K\to\operatorname{Spec}k$ is
the geometric point $\bar v$, so the inclusion $K\subseteq\Omega$ is a
lift $\bar v'$ of $\bar v$.

*(ii).* Let $U\to\operatorname{Spec}k$ be étale and nonempty, and
suppose that $\phi:U\to\operatorname{Spec}K$ is a $k$-morphism; it
corresponds to a unital $k$-algebra map
$K\to\Gamma(U,\mathcal O_U)$. Choose a nonempty affine open
$\operatorname{Spec}S\subseteq U$. The composite
$K\to\Gamma(U,\mathcal O_U)\to S$ is a unital $k$-algebra map into the
nonzero ring $S$, and $S$ is étale over the field $k$, so by Stacks
Project, Algebra, Lemma 10.143.4,
[Tag 00U3](https://stacks.math.columbia.edu/tag/00U3) the ring $S$ is a
finite product $\prod_{j=1}^{n}L_j$ of finite separable extensions
$L_j/k$. Composing with the projection onto one factor gives a unital ring
map $K\to L_j$ from the field $K$ into the nonzero ring $L_j$, which is
injective; hence $K$ embeds into the finite extension $L_j$ of $k$ and
$[K:k]<\infty$, contradicting that $K/k$ is infinite. A morphism of
pointed étale
neighbourhoods would in particular induce such a
$k$-morphism $U\to\operatorname{Spec}K$, so none exists.

*(iii).* A full subcategory computes the colimit over the ambient
category when every object of the ambient category admits a morphism from an
object of the subcategory: this is the criterion in whose form the affine
pointed étale neighbourhoods are used in
[lemma-weil-pbc-affine-neighbourhood-cofinal]. By (ii) the pointed
pro-étale neighbourhood $(\operatorname{Spec}K,\bar v')$ receives no
morphism from any pointed étale neighbourhood, so the criterion fails and the
two colimits are not compared by it. Nothing here asserts that
$(\mathrm{C}_q)$ is false; it asserts that the acyclicity device of
[lem-sf-proetale-neighbourhood-colimit] does not settle it, so that the
remaining case of $(\mathrm{C}_q)$ is the coefficient sheaves that are not of
étale origin.
