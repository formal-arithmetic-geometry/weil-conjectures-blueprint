+++
id = "lem-sf-stalk-limit-acyclic"
kind = "lemma"
title = "The strictly henselian limit has no higher cohomology"
order = 2149
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-strict-henselization-limit"]
+++
Let $S$ be a scheme, let $\bar s\to S$ be a
geometric point in the sense of
[def-weil-pbc-geometric-stalks], and let
$S_{(\bar s)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}$ be the
strict henselization
limit of [def-weil-pbc-strict-henselization-limit], the inverse limit of
the pointed étale neighbourhoods of
[def-weil-pbc-pointed-etale-neighbourhoods]. Then:

1. **(i)** $S_{(\bar s)}$ is an object of the
small pro-étale site
$S_{\Proet}$ of [def-weil-pbc-proetale-site], and every sheaf
$\mathcal F$ of $A$-modules on $S_{\Proet}$ – that is, every object of
[def-weil-pbc-proetale-modules] – satisfies
$$
\mathcal F\bigl(S_{(\bar s)}\bigr)=\mathcal F_{\bar s},
$$
the right-hand side being the stalk
of $\mathcal F$ at $\bar s$;
1. **(ii)** the functor
$\mathcal F\mapsto\mathcal F(S_{(\bar s)})$ on sheaves of $A$-modules on
$S_{\Proet}$ is exact;
1. **(iii)** consequently
$$
H^q\bigl(S_{(\bar s),\Proet},\mathcal F\bigr)=0\qquad(q>0)
$$
for *every* sheaf $\mathcal F$ of $A$-modules on $S_{\Proet}$,
without any hypothesis of constructibility or of étale origin.

## Proof

*(i).* The scheme $S_{(\bar s)}$ is the spectrum of the filtered
colimit of the etale algebras $\mathcal O(V)$ over the affine pointed etale
neighbourhoods, by
[def-weil-pbc-strict-henselization-limit]; each of those maps is etale,
hence weakly etale, and a filtered colimit of weakly etale maps is weakly
etale, so $\mathcal O^{\mathrm{sh}}_{S,\bar s}$ is weakly etale over
$\mathcal O(S)$ and $S_{(\bar s)}\to S$ is an object of the
small pro-étale site
[def-weil-pbc-proetale-site] on which the module sheaves of
[def-weil-pbc-proetale-modules] live; equivalently
this is the description of the strict henselization by its isomorphism on
strict henselizations, Stacks Project, More on Morphisms, Lemma 37.64.11,
[Tag 094Z](https://stacks.math.columbia.edu/tag/094Z). The category of
pro-étale neighbourhoods of $\bar s$ is cofiltered (Stacks Project,
Pro-étale Cohomology, Lemma 61.18.2,
[Tag 0F6B](https://stacks.math.columbia.edu/tag/0F6B)) and
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}$ is an initial object
of it, by Olivier's theorem, so that the colimit over all pro-étale
neighbourhoods is the value at that object: this is Stacks Project,
Pro-étale Cohomology, Lemma 61.18.4,
[Tag 0993](https://stacks.math.columbia.edu/tag/0993), whose two
assertions are exactly the two displayed statements of (i). On module sheaves
the same identification holds, the forgetful functor to sheaves of sets
commuting with the colimit.

*(ii).* It was recalled in Section 61.18 of the Stacks Project that the
stalk functor defines a point of the pro-étale topos and is therefore exact
and commutes with arbitrary colimits; this is Stacks Project, Pro-étale
Cohomology, Section 61.18,
[Tag 0991](https://stacks.math.columbia.edu/tag/0991), where the
cofilteredness input is Lemma 61.18.2 and the identification of the point with
the strict henselization limit is Lemma 61.18.4. Combined with (i) this says
that the functor $\mathcal F\mapsto\mathcal F(S_{(\bar s)})$ is exact on
sheaves of $A$-modules: it is the composite of the exact forgetful functor
with the stalk functor of
[def-weil-pbc-geometric-stalks], and exactness of a functor on sheaves of
sets implies exactness on the category of module sheaves of
[def-weil-pbc-etale-sheaves] over a constant ring.

*(iii).* The groups $H^q(S_{(\bar s),\Proet},\mathcal F)$ are by
definition the derived functors of the left exact functor
$\mathcal F\mapsto\mathcal F(S_{(\bar s)})$ evaluated at $\mathcal F$.
By (ii) that functor is exact, so its higher derived functors vanish and every
one of those groups is zero. Nothing in the argument used constructibility or
étale origin of $\mathcal F$, which is the point of the statement.
