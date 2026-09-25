+++
id = "lem-sf-acyclic-hypercover-terms-vanishing"
kind = "lemma"
title = "Vanishing above the degree in which the coefficient sheaf dies on the terms"
order = 2154
uses = ["def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "lem-cbc-proetale-stalk-conservative", "lem-sf-stalk-limit-acyclic"]
+++
Let $T$ be a scheme, let $U\to T$ be an object of the
small pro-étale site $T_{\Proet}$ of
[def-weil-pbc-proetale-site], let $\mathcal F$ be a sheaf of
$A$-modules on $T_{\Proet}$, that is, an object of
[def-weil-pbc-proetale-modules], and let $K$ be a hypercovering of $U$
with $K_n=\{U_n\to U\}$ a single morphism for every $n\geq0$, the shape of
the hypercoverings considered in Stacks Project, Pro-étale Cohomology, Lemma
61.14.2, [Tag 09A2](https://stacks.math.columbia.edu/tag/09A2). Assume

1. **(a)** $H^q(U_n,\mathcal F)=0$ for every $n\geq0$ and every $q>0$
— for instance because every $U_n$ is weakly contractible, in which case
this is Stacks Project, Cohomology on Sites, Lemma 21.51.1,
[Tag 0946](https://stacks.math.columbia.edu/tag/0946) — and
1. **(b)** $\mathcal F(U_n)=0$ for every $n>N$, for some integer $N$.

Then $H^q(U,\mathcal F)=0$ for every $q>N$. The criterion is not vacuous:
for $U=\operatorname{Spec}\bar k$ with $\bar k$ separably closed and
$\mathcal F$ the sheafified quotient of clause (4) of
[lem-cbc-proetale-stalk-conservative], whose value on
$\operatorname{Spec}\bar k$ is zero, the constant simplicial object
$U_n=U$ is a hypercovering of $U$ that satisfies (a), by
[lem-sf-stalk-limit-acyclic](iii), and (b) with $N=-1$, so that
$H^q(\operatorname{Spec}\bar k,\mathcal F)=0$ for every $q\geq0$.

## Proof

*Step 1: the higher cohomology sheaves of $\mathcal F$ vanish.* For
$q>0$ let $\underline H^q(\mathcal F)$ be the sheaf associated to the
presheaf $V\mapsto H^q(V,\mathcal F)$ on $T_{\Proet}$. By (a) it vanishes on
$U_0$, and $\{U_0\to U\}$ is a covering of $U$ by (a) of the definition of a
hypercovering; a sheaf that vanishes on the members of a covering family vanishes
identically, because for an arbitrary $W\to U$ the base change
$\{U_0\times_UW\to W\}$, a covering of $W$ by
[def-weil-pbc-proetale-site], has members on which the restriction of
$\underline H^q(\mathcal F)$ vanishes, so that the sheaf axiom embeds
$\underline H^q(\mathcal F)(W)$ into a product of zero groups. Hence
$\underline H^q(\mathcal F)=0$ for every $q>0$.

*Step 2: the Čech complex of the hypercovering computes the
cohomology.* By Stacks Project, Hypercoverings, Lemma 25.5.3,
[Tag 01GY](https://stacks.math.columbia.edu/tag/01GY), applied to the
hypercovering $K$ of $U$ and the sheaf $\mathcal F$, there is a spectral
sequence

$$
E_2^{p,q}=\check H^p\bigl(K,\underline H^q(\mathcal F)\bigr)
\Longrightarrow H^{p+q}(U,\mathcal F).
$$

By Step 1 its rows with $q>0$ vanish, so $E_2=E_\infty$ and the abutment is
the remaining row:

$$
H^n(U,\mathcal F)=\check H^n(K,\mathcal F)
$$

for every $n$, the right hand side being the cohomology of the complex
$s(\mathcal F(K))$, whose term in degree $n$ is $\mathcal F(U_n)$ and whose
differentials are the alternating sums $\sum_i(-1)^id^i$ of the maps induced
by the face maps of $K$.

*Step 3: conclusion.* By (b) that complex vanishes in degrees $>N$,
hence so does its cohomology, which is $H^q(U,\mathcal F)$ for every $q$ by
Step 2.

*Step 4: the example.* For the constant simplicial object $U_n=U$ all
face and degeneracy maps are identities, so that $\{U_0\to U\}$,
$\{U_1\to U_0\times_UU_0\}$ and
$\{U_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nU)_{n+1}\}$, the last
being an isomorphism, are coverings as required by Stacks Project, Example
25.3.5, [Tag 0GM9](https://stacks.math.columbia.edu/tag/0GM9): $K$ is a
hypercovering of $U$, with $U_n=U$ for every $n$. Its terms are copies of
$U=\operatorname{Spec}\bar k$, and $\operatorname{Spec}\bar k$ is its own
strict henselization limit at its unique geometric point, so that hypothesis
(a) of the statement holds, by
[lem-sf-stalk-limit-acyclic](iii), the coefficient sheaf being an object of
[def-weil-pbc-proetale-modules]. Property (b) with $N=-1$ holds because
the sheaf of clause (4) of [lem-cbc-proetale-stalk-conservative] is the
sheafified quotient of $fun(-,A)$ by the image of the constant sheaf and has
value zero at the one-point object $\operatorname{Spec}\bar k$. Steps 1–3
therefore give $H^q(\operatorname{Spec}\bar k,\mathcal F)=0$ for every
$q\geq0$.
