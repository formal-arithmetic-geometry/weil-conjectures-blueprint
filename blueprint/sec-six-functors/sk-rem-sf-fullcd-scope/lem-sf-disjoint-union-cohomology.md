+++
id = "lem-sf-disjoint-union-cohomology"
kind = "lemma"
title = "Cohomology of a disjoint union"
order = 2132
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension", "lem-weil-pbc-etale-restriction-injectives"]
+++
Let $T=\bigsqcup_{i\in I}T_i$ be a scheme written as the disjoint union of
its open subschemes $T_i$, with inclusions
$j_i:T_i\hookrightarrow T$, let $A$ be a commutative ring and let
$\mathcal F$ be a sheaf of $A$-modules on the
small étale site $T_{\Et}$, in the
sense of [def-weil-pbc-etale-sheaves]. Then for every $q\geq0$ the
restriction maps induce an isomorphism

$$
H^q\bigl(T_{\Et},\mathcal F\bigr)\xrightarrow{\ \sim\ }
\prod_{i\in I}H^q\bigl((T_i)_{\Et},\mathcal F|_{T_i}\bigr).
$$

## Proof

Write $j_i^*\mathcal F$ for the restriction of $\mathcal F$ to $T_i$, the
inverse image along the étale morphism $j_i$ of
[def-weil-pbc-etale-site].

*(a) Global sections.* The open immersions $j_i$ are étale, so
$\lbrace j_i:T_i\to T\rbrace_{i\in I}$ is a covering family of the site
[def-weil-pbc-etale-site], and the sheaf axiom of
[def-weil-pbc-etale-sheaves] writes $\mathcal F(T)$ as the equalizer of
the two restriction maps

$$
\prod_{i\in I}\mathcal F(T_i)\rightrightarrows
\prod_{(i,i')\in I\times I}\mathcal F(T_i\cap T_{i'}).
$$

For $i\neq i'$ the intersection $T_i\cap T_{i'}$ is empty and
$\mathcal F(\emptyset)=0$, the empty product of $A$-modules; so the
equalizer is the first factor and

$$
\Gamma(T,\mathcal F)=\prod_{i\in I}\Gamma(T_i,j_i^*\mathcal F)
$$

for every sheaf $\mathcal F$ of $A$-modules on $T_{\Et}$.

*(b) Injectives.* By [lem-weil-pbc-etale-restriction-injectives]
the functor $j_{i,!}$ of [def-weil-pbc-etale-sum-extension] is exact and
left adjoint to $j_i^*$, and consequently $j_i^*$ carries injective module
sheaves on $T_{\Et}$ to injective module sheaves on $(T_i)_{\Et}$.

*(c) Exactness.* The functor $j_i^*$ is a right adjoint, hence left
exact. It preserves epimorphisms as well: an epimorphism of étale sheaves is
locally surjective, and an étale covering of an étale $T$-scheme $V$
whose members factor through $T_i$ is an étale covering of the
$T_i$-scheme $V$, the members still being étale over $T_i$ and still
jointly surjective. Hence $j_i^*$ is exact.

*(d) Conclusion.* Let $\mathcal F\to\mathcal I^\bullet$ be an injective
resolution of $\mathcal F$ on $T_{\Et}$. By (b) each $j_i^*\mathcal I^\bullet$ is a bounded below complex of injective sheaves on
$(T_i)_{\Et}$ and by (c) its cohomology is $j_i^*\mathcal F$ in degree
$0$ and zero in the positive degrees; a bounded below complex of injectives
whose cohomology is concentrated in degree $0$ computes the right derived
functors of the functor $\Gamma$ applied to its degree-$0$ cohomology, so

$$
H^q\bigl(\Gamma(T_i,j_i^*\mathcal I^\bullet)\bigr)
=H^q\bigl((T_i)_{\Et},j_i^*\mathcal F\bigr)
$$

for every $i\in I$ and every $q$. By (a), applied degreewise to the
complex $\mathcal I^\bullet$,

$$
\Gamma(T,\mathcal I^\bullet)
=\prod_{i\in I}\Gamma(T_i,j_i^*\mathcal I^\bullet),
$$

and kernels and images of a product of complexes of $A$-modules are computed
componentwise, so the cohomology of the product complex is the product of the
cohomologies of its factors. As $\Gamma(T,\mathcal I^\bullet)$ computes
$H^*(T_{\Et},\mathcal F)$, the displayed isomorphism follows.
