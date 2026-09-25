+++
id = "thm-sf-continuity-arbitrary-sheaves-vanishing"
kind = "theorem"
title = "Continuity for arbitrary sheaves implies the vanishing"
order = 2157
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-pbc-strict-henselization-limit", "lem-sf-associated-sheaf-local-lifting", "lem-sf-stalk-limit-acyclic", "lemma-weil-pbc-geometric-stalk-conservative", "rem-sf-fullcd-general-form", "thm-sf-fullcd-etale-origin"]
+++
Let $V$ be a scheme with comparison morphism
$\nu_V:V_{\Proet}\to V_{\Et}$ as in
[def-weil-pbc-site-comparison-morphism], and fix an integer $q\geq1$.
Consider the following statement.

1. **$(\mathrm{C}_q)$** For every sheaf $\mathcal F$ of $A$-modules on
the small pro-étale site $V_{\Proet}$ of
[def-weil-pbc-proetale-site], that is, every object of
[def-weil-pbc-proetale-modules], and every
geometric point
$\bar v\to V$ in the sense of [def-weil-pbc-geometric-stalks], every
cohomology class on an étale neighbourhood of
$\bar v$ dies after refinement: for every étale $U\to V$ with a lift
$\bar u$ of $\bar v$ as in
[def-weil-pbc-pointed-etale-neighbourhoods], and every class
$c\in H^q(U_{\Proet},\mathcal F|_U)$, there is a pointed refinement
$(U',\bar u')\to(U,\bar u)$ with $c|_{U'}=0$.
Equivalently, the canonical map
$$
\varinjlim_{(U,\bar u)}H^q\bigl(U_{\Proet},\mathcal F|_U\bigr)
\longrightarrow
H^q\bigl(\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V,\bar v},
\mathcal F\bigr)
$$
is an isomorphism for every $\mathcal F$ and every $\bar v$, the colimit
running over the pointed étale neighbourhoods of $\bar v$; here
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V,\bar v}$ is the strict
henselization limit of [def-weil-pbc-strict-henselization-limit].

Then $(\mathrm{C}_q)$ implies

$$
R^q\nu_{V,*}\mathcal F=0
$$

for *every* sheaf $\mathcal F$ of $A$-modules on $V_{\Proet}$: the
statement $(\mathrm{G})$ of [rem-sf-fullcd-general-form] holds at $V$
in degree $q$ with the sharpest possible bound, in which no degree $q\geq1$
survives, uniformly in $\mathcal F$.

## Proof

*The two formulations of $(\mathrm{C}_q)$ agree.* The target of the
displayed map is zero for every $\mathcal F$ and every $q>0$ by
[lem-sf-stalk-limit-acyclic](iii), applied to the scheme $V$ and the
geometric point $\bar v$. A filtered colimit of abelian groups is zero if
and only if every element of every term is killed by some structure map of the
system, and the structure maps here are the restriction maps along pointed
refinements of
[def-weil-pbc-pointed-etale-neighbourhoods]; hence the displayed map is an
isomorphism if and only if every class dies after refinement, which is the
first formulation.

*The associated sheaf.* Fix $\mathcal F$ and put

$$
P(U)=H^q\bigl(U_{\Proet},\mathcal F|_U\bigr)
$$

for étale $U\to V$, a presheaf of $A$-modules on the
small étale site of $V$. By Stacks
Project, Cohomology on Sites, Lemma 21.7.4,
[Tag 072W](https://stacks.math.columbia.edu/tag/072W) the sheaf
$R^q\nu_{V,*}\mathcal F$ is the sheaf associated to $P$: this is the same
identification that is used in the proof of
[thm-sf-fullcd-etale-origin] for sheaves of étale origin, and it holds
verbatim for an arbitrary $\mathcal F$ because it only evaluates the derived
direct image of [def-weil-pbc-direct-image] on étale objects. Write
$P^{\#}=R^q\nu_{V,*}\mathcal F$.

*Every geometric stalk of $P^{\#}$ vanishes.* Fix $\bar v\to V$ and
let $s\in(P^{\#})_{\bar v}$ be a class in the
stalk; by
[def-weil-pbc-pointed-etale-neighbourhoods] it is represented by a section
$s_0\in P^{\#}(U)$ over a pointed étale neighbourhood $(U,\bar u)$ of
$\bar v$. Apply [lem-sf-associated-sheaf-local-lifting] to $P$,
$P^{\#}$ and $s_0$: there are an étale covering
$\lbrace U_i\to U\rbrace$ and elements $s_i\in P(U_i)$ with
$s_0|_{U_i}=\operatorname{im}(s_i)$ in $P^{\#}(U_i)$. Choose an index
$i$ such that the point of $U$ underlying $\bar u$ lies in the image of
$U_i\to U$, and lift $\bar u$ to a geometric point $\bar u_i$ of
$U_i$, which is possible because an étale morphism is surjective on
underlying topological spaces. Apply $(\mathrm{C}_q)$ to the class of
$s_i\in P(U_i)=H^q((U_i)_{\Proet},\mathcal F|_{U_i})$ at the geometric point
$\bar u_i$ of $V$: there is a pointed refinement
$(U',\bar u')\to(U_i,\bar u_i)$ with $s_i|_{U'} = 0$ in $P(U')$. By
naturality of the canonical map $P\to P^{\#}$,

$$
s_0|_{U'}
=\operatorname{im}(s_i)|_{U'}
=\operatorname{im}\bigl(s_i|_{U'}\bigr)
=\operatorname{im}(0)=0
\qquad\text{in }P^{\#}(U'),
$$

and $(U',\bar u')\to(U,\bar u)$ is a pointed refinement, so the class
$s=[s_0]$ is zero in the filtered colimit $(P^{\#})_{\bar v}$. Hence
$(P^{\#})_{\bar v}=0$ for every geometric point $\bar v$ of $V$.

*Conclusion.* The etale sheaf $P^{\#}=R^q\nu_{V,*}\mathcal F$ has all
geometric stalks zero, so it is zero by the conservativity of the geometric
stalks of [lemma-weil-pbc-geometric-stalk-conservative]. As
$\mathcal F$ was arbitrary this is the assertion.
