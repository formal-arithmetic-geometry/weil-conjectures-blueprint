+++
id = "lem-sf-etale-origin-refinement"
kind = "lemma"
title = "Continuity for sheaves of étale origin: every class dies on a single pointed refinement"
order = 3736
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-pointed-etale-neighbourhoods-detailed", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "lem-sf-associated-sheaf-local-lifting", "lem-sf-disjoint-union-cohomology", "lem-weil-pbc-comparison-pullback", "thm-sf-continuity-arbitrary-sheaves-vanishing"]
+++
Let $V$ be a scheme with comparison morphism
$\nu_V:V_{\Proet}\to V_{\Et}$ as in
[def-weil-pbc-site-comparison-morphism], let $\mathcal G$ be a sheaf of
$A$-modules on the small étale site
$V_{\Et}$, in the sense of [def-weil-pbc-etale-sheaves], let
$\bar v\to V$ be a geometric point
of [def-weil-pbc-geometric-stalks], let $U\to V$ be étale with a lift
$\bar u$ of $\bar v$, so that $(U,\bar u)$ is a
pointed étale
neighbourhood of $\bar v$ in the sense of
[def-weil-pbc-pointed-etale-neighbourhoods-detailed], let $q\geq1$ and let

$$
c\in H^q\bigl(U_{\Proet},\nu_U^*(\mathcal G|_U)\bigr)
$$

be a cohomology class on the
small pro-étale site of $U$, the
coefficient sheaf $\nu_U^*(\mathcal G|_U)$ being the pullback of
$\mathcal G|_U$ along the comparison morphism of $U$ and hence an object of
[def-weil-pbc-proetale-modules]. Then there is a pointed refinement
$(U',\bar u')\to(U,\bar u)$ with

$$
c|_{U'}=0,
$$

namely $U'=\bigsqcup_{i\in I}U_i$ for an étale covering
$\lbrace U_i\to U\rbrace_{i\in I}$ of $U$ and $\bar u'$ any lift of
$\bar u$ to $U'$. Consequently statement $(\mathrm{C}_q)$ of
[thm-sf-continuity-arbitrary-sheaves-vanishing] holds at $V$, for every
$q\geq1$, for every sheaf of $A$-modules on $V_{\Proet}$ that is of
*étale origin*: for $\mathcal F=\nu_V^*\mathcal G$ the colimit
displayed there is zero.

## Proof

*Step 1: the two groups agree.* For the sheaf $\mathcal G|_U$ of
$A$-modules on the étale site of $U$, in the sense of
[def-weil-pbc-etale-sheaves], Stacks Project, Pro-étale
Cohomology, Lemma 61.19.6,
[Tag 099W](https://stacks.math.columbia.edu/tag/099W) gives

$$
H^q\bigl(U_{\Et},\mathcal G|_U\bigr)
=H^q\bigl(U_{\Proet},\nu_U^*(\mathcal G|_U)\bigr)
$$

for all $q$, so that $c$ is also a class in the étale cohomology of
$U$, and this identification is natural in the scheme $U$.

*Step 2: every class dies on an étale covering of $U$.* Put
$P(W)=H^q(W_{\Et},\mathcal G|_W)$ for étale $W\to U$; by Step 1 this is
also $H^q(W_{\Proet},\nu_W^*(\mathcal G|_W))$, the restriction of
$\nu_U^*(\mathcal G|_U)$ to $W$ being $\nu_W^*(\mathcal G|_W)$ by
[lem-weil-pbc-comparison-pullback], so that $P$ is the presheaf
of
pro-étale cohomology of the
restrictions of $\mathcal G$ that occurs in $(\mathrm{C}_q)$. By Stacks
Project, Cohomology on Sites, Lemma 21.7.4,
[Tag 072W](https://stacks.math.columbia.edu/tag/072W) the sheaf
$R^q\nu_{U,*}\nu_U^*(\mathcal G|_U)$ on the étale site of $U$ is the
sheaf associated to the presheaf $P$, and by Stacks Project, Pro-étale
Cohomology, Lemma 61.19.5,
[Tag 099V](https://stacks.math.columbia.edu/tag/099V) one has
$R\nu_{U,*}\nu_U^*(\mathcal G|_U)=\mathcal G|_U$, so that $P^{\#}=0$ in the
degree $q\geq1$ under consideration. In the two-step construction
$P\to P^{+}\to P^{\#}$ of the associated sheaf, the map $P\to P^{+}$ kills
exactly the classes that vanish on an étale covering and $P^{+}\to P^{\#}$
is injective, as recalled in the proof of
[lem-sf-associated-sheaf-local-lifting]; the image of $c\in P(U)$ in
$P^{\#}(U)=0$ being zero, there is therefore an étale covering
$\lbrace U_i\to U\rbrace_{i\in I}$ with $c|_{U_i}=0$ for every $i\in I$.

*Step 3: one refinement kills $c$.* Let $U'=\bigsqcup_{i\in I}U_i$
and let $\pi:U'\to U$ be the fold map. A disjoint union of étale morphisms
is étale, and $\pi$ is surjective because the family
$\lbrace U_i\to U\rbrace$ is jointly surjective, so $U'$ is an object of
the small étale site of $U$. By
[lem-sf-disjoint-union-cohomology] the restriction maps identify
$H^q(U'_{\Et},\mathcal G|_{U'})$ with the product of the groups
$H^q((U_i)_{\Et},\mathcal G|_{U_i})$, and the components of $c|_{U'}$ are
the classes $c|_{U_i}=0$, so $c$ vanishes on $U'$ in étale cohomology;
by Step 1 applied to the pair $(U,U')$, the identification being natural,
$c$ vanishes on $U'$ in
pro-étale cohomology as well.

*Step 4: the refinement is pointed.* It remains to produce the lift
$\bar u'$. Let $\Omega$ be the residue field of the geometric point
$\bar u$, an algebraically closed field by
[def-weil-pbc-scheme-conventions], and let $u\in U$ be the image of
$\bar u$. Since the family $\lbrace U_i\to U\rbrace$ is jointly
surjective, the fibre of $\pi$ over $u$ is nonempty, so
$U'\times_U\operatorname{Spec}\Omega$ is nonempty as well: it is the base
change of that fibre along the morphism
$\operatorname{Spec}\Omega\to\operatorname{Spec}\kappa(u)$, whose underlying
map of one-point spaces is surjective; and it is étale
over $\operatorname{Spec}\Omega$ because étale morphisms are stable under
base change. Choose a nonempty affine open $\operatorname{Spec}S$ of it;
the composite $\operatorname{Spec}S\to U'\times_U\operatorname{Spec}\Omega\to \operatorname{Spec}\Omega$ is étale, so by Stacks Project, Algebra, Lemma
10.143.4,
[Tag 00U3](https://stacks.math.columbia.edu/tag/00U3) the ring $S$ is a
finite product of finite separable extensions of $\Omega$, each of which is
$\Omega$ itself because $\Omega$ is algebraically closed. Hence $S$ is a
nonzero finite product of copies of $\Omega$, so the projection onto one
factor is a section of $\operatorname{Spec}S\to\operatorname{Spec}\Omega$,
and composing it with the open immersion of $\operatorname{Spec}S$ gives a
section $\bar u'$ of $U'\times_U\operatorname{Spec}\Omega\to \operatorname{Spec}\Omega$. By the universal property of the fibre product
the composite $\operatorname{Spec}\Omega\xrightarrow{\bar u'}U'\xrightarrow{\pi} U$ is the given geometric point $\bar u$, so
$(U',\bar u')\to(U,\bar u)$ is a pointed refinement in the sense of
[def-weil-pbc-pointed-etale-neighbourhoods-detailed], and $c|_{U'}=0$ by Step 3.

*Conclusion.* Let $\mathcal F=\nu_V^*\mathcal G$ be of étale origin.
For étale $U\to V$ the restriction of $\mathcal F$ to $U$ is
$\nu_U^*(\mathcal G|_U)$, by the compatibility of the comparison pullback
with scheme pullback, [lem-weil-pbc-comparison-pullback]. By Steps 1–4
every class in $H^q(U_{\Proet},\mathcal F|_U)$ for $q\geq1$ and every
pointed étale neighbourhood $(U,\bar u)$ of every geometric point
$\bar v$ of $V$ dies on a pointed refinement; this is statement
$(\mathrm{C}_q)$ of
[thm-sf-continuity-arbitrary-sheaves-vanishing] at $V$ for
$\mathcal F$. By the equivalence recalled in the proof of that theorem the
colimit displayed there is then zero for $\mathcal F$ and every $q\geq1$.
As $\mathcal G$ was an arbitrary sheaf of $A$-modules on $V_{\Et}$, this
holds for every sheaf on $V_{\Proet}$ of étale origin.
