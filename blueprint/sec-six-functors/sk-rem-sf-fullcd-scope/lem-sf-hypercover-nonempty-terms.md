+++
id = "lem-sf-hypercover-nonempty-terms"
kind = "lemma"
title = "No hypercovering of a nonempty object has an empty term"
order = 2153
uses = ["def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions"]
+++
Let $T$ be a scheme, let $U\to T$ be a nonempty object of the
small pro-étale site
$T_{\Proet}$ of [def-weil-pbc-proetale-site], and let $K$ be a
hypercovering of $U$ in the sense of Stacks Project, Definition 25.3.3,
[Tag 01G5](https://stacks.math.columbia.edu/tag/01G5): a simplicial object
of $\mathrm{SR}(T_{\Proet},U)$, whose terms are the families
$K_n=\{U_{n,i}\to U\}_{i\in I_n}$ of
weakly étale $U$-schemes
satisfying

1. **(a)** $K_0$ is a covering of $U$ for the pro-étale topology of
[def-weil-pbc-proetale-site], and
1. **(b)** for every $n\geq0$ the canonical morphism
$K_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nK)_{n+1}$ is a covering
in the sense of Stacks Project, Definition 25.3.1,
[Tag 01G3](https://stacks.math.columbia.edu/tag/01G3).

Then for every $n\geq0$ there is $i\in I_n$ with $U_{n,i}\neq\emptyset$.
In particular there is no integer $N$ with $K_n=\{U_{n,i}\to U\}_{i\in I_n}$
empty — that is, with $U_{n,i}=\emptyset$ for all $i\in I_n$ — for all
$n>N$:
*no hypercovering of a nonempty object of $T_{\Proet}$ is bounded*. If
moreover $K_n=\{U_n\to U\}$ is a single morphism for every $n$, as in the
hypercoverings constructed in Stacks Project, Pro-étale Cohomology, Lemma
61.14.1, [Tag 09A1](https://stacks.math.columbia.edu/tag/09A1), and used in
Lemma 61.14.2, [Tag 09A2](https://stacks.math.columbia.edu/tag/09A2), then
$U_n\neq\emptyset$ for every $n\geq0$.

## Proof

By [def-weil-pbc-proetale-site] a covering family of an object of
$T_{\Proet}$ is a jointly surjective family of weakly étale morphisms, the
notion of weakly étale being that of
[def-weil-pbc-scheme-conventions]. Three consequences of joint
surjectivity are used below: a family all of whose members are empty covers only
the empty scheme; a morphism of schemes whose source is nonempty has nonempty
target; and a covering family of a nonempty scheme has a nonempty member.

*Step 1: $K_0$ has a nonempty member.* By (a) the family
$\{U_{0,i}\to U\}_{i\in I_0}$ is a covering of $U$, hence jointly
surjective; were every $U_{0,i}$ empty, its image would be empty and the
family would cover only the empty scheme, contrary to $U\neq\emptyset$.

*Step 2: the matching objects have a nonempty member.* Fix $n\geq0$ and
put $M_{n+1}=(\operatorname{cosk}_n\operatorname{sk}_nK)_{n+1}$, an object of
$\mathrm{SR}(T_{\Proet},U)$, that is, a family
$\{M_{n+1,j}\to U\}_{j\in J_{n+1}}$ of $U$-schemes. The simplicial object
$K$ carries degeneracies, and the codegeneracy $\sigma:[n+1]\to[0]$ of the
simplex category induces the structure morphism $K(\sigma):K_0\to K_{n+1}$.
Composing it with the canonical morphism $K_{n+1}\to M_{n+1}$ of (b) gives a
morphism $K_0\to M_{n+1}$ of $\mathrm{SR}(T_{\Proet},U)$, that is, a map
$\alpha:I_0\to J_{n+1}$ of index sets together with morphisms
$U_{0,i}\to M_{n+1,\alpha(i)}$ over $U$, for every $i\in I_0$. Choose
$i\in I_0$ with $U_{0,i}\neq\emptyset$, which exists by Step 1; then
$M_{n+1,\alpha(i)}$ receives a morphism from a nonempty scheme and is
therefore nonempty.

*Step 3: $K_{n+1}$ has a nonempty member.* By (b) the morphism
$K_{n+1}\to M_{n+1}$ is a covering in the sense of Definition 25.3.1,
[Tag 01G3](https://stacks.math.columbia.edu/tag/01G3), which says that for
every $j\in J_{n+1}$ the family of those $U_{n+1,k}\to U$ that are mapped to
$M_{n+1,j}$ is a covering of the site. Applying this to the index
$j=\alpha(i)$ of Step 2, whose member $M_{n+1,j}$ is nonempty, and using
that a covering family of a nonempty scheme has a nonempty member, we find
$k\in I_{n+1}$ with $U_{n+1,k}\neq\emptyset$. As $n\geq0$ was arbitrary,
this proves the first assertion, and the second is its immediate consequence.

*The single-morphism case.* If $K_n=\{U_n\to U\}$ for every $n$, the
coverings of (a) and (b) are the three families recorded in Stacks Project,
Example 25.3.5, [Tag 0GM9](https://stacks.math.columbia.edu/tag/0GM9),
namely $\{U_0\to U\}$, $\{U_1\to U_0\times_UU_0\}$ and
$\{U_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nU)_{n+1}\}$ for
$n\geq1$. The argument above reads $U_0\neq\emptyset$ from the first
family; it reads $U_1\neq\emptyset$ from the second, whose target
$U_0\times_UU_0$ contains the diagonal copy of the nonempty $U_0$; and it
reads $U_{n+1}\neq\emptyset$, $n\geq1$, from the third, applied to the
degenerate simplex $U_0\to U_{n+1}$.
