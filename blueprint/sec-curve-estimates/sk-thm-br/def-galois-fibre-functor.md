+++
id = "def-galois-fibre-functor"
kind = "definition"
title = "The fibre functor"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.fiber", "CategoryTheory.PreGaloisCategory.IsFundamentalGroup", "AlgebraicGeometry.Scheme.FiniteEtale.exists_isFundamentalGroup", "CategoryTheory.PreGaloisCategory.toAutHomeo", "ContAction"]
order = 1375
uses = ["def-galois-categories", "thm-galois-lc-etale"]
+++
In the situation of [def-galois-categories], let the geometric point be
$\bar y:\operatorname{Spec}\Omega\to Y$ with $\Omega$ separably closed.
The *fibre functor* is

$$
F_{\bar y}:\mathrm{F\acute Et}(Y)\longrightarrow(\text{finite sets}),\qquad
P\longmapsto|P_{\bar y}|=\operatorname{Hom}_Y(\operatorname{Spec}\Omega,P),
$$

the geometric fibre of [def-galois-categories]. Its *automorphism group*
$\operatorname{Aut}(F_{\bar y})$ is the group of natural automorphisms of
$F_{\bar y}$, embedded into
$\prod_P\operatorname{Aut}(F_{\bar y}(P))$ by evaluation and endowed with
the topology induced from the product of the discrete topologies.

For $Y$ connected, a *fundamental group* of $F_{\bar y}$ is a compact
topological group $G$ acting on every $F_{\bar y}(P)$, naturally in $P$
and continuously for the discrete topology, transitively on the fibres
of Galois objects, and such that only the identity acts trivially on all
fibres. The group $\operatorname{Aut}(F_{\bar y})$ is one, every
fundamental group is canonically isomorphic to it as a topological group,
and there is a profinite one; any of them is the *etale fundamental
group* $\pi_1(Y,\bar y)$. A $\pi_1(Y,\bar y)$-set is a finite set with a
continuous action of $\pi_1(Y,\bar y)$, and such sets form the category
$\pi_1(Y,\bar y)\text{-}\mathbf{Set}$.

Under the equivalence $\mathrm{F\acute Et}(Y)\simeq\mathrm{FLC}(Y)$ of
[thm-galois-lc-etale], $F_{\bar y}$ corresponds to the stalk functor
$\mathcal F\mapsto\mathcal F_{\bar y}$ on $\mathrm{FLC}(Y)$ (for $\Omega$
algebraically closed).
