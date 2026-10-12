+++
id = "lemma-weil-pbc-leray-acyclicity"
kind = "lemma"
title = "Leray acyclicity criterion"
order = 1066
uses = ["def-sp-acyclic", "def-sp-injective-resolutions", "def-sp-kinjective-bridge", "def-sp-left-exact-additive", "def-weil-pbc-direct-image", "def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-kinjective-resolutions", "lem-sp-derived-well-defined", "lem-sp-kinjective-computes", "thm-sp-if-e1"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor
[def-sp-left-exact-additive] between abelian categories with enough
injectives, with right derived functors $R^qv$.

1. Injective objects of $\mathcal A$ are $v$-acyclic [def-sp-acyclic].
2. **(Acyclicity criterion.)** If $F\to I^\bullet$ is a resolution of an
   object $F\in\mathcal A$ by $v$-acyclic objects (i.e. $I^m=0$ for $m<0$,
   the augmented complex $0\to F\to I^0\to I^1\to\cdots$ is exact, and
   $R^qvI^m=0$ for $q>0$), then the natural map is an isomorphism

   $$
    \mathcal H^q(vI^\bullet)\xrightarrow{\ \sim\ }R^qvF\qquad(q\geq0):
   $$

   the cohomology of a termwise-acyclic resolution computes the derived
   functor. Here the natural map is the one induced by any morphism of
   complexes $I^\bullet\to J^\bullet$ over $\mathrm{id}_F$ into an injective
   resolution [def-sp-injective-resolutions] $F\to J^\bullet$.
3. **(Complexes.)** If moreover $\mathcal A$ is Grothendieck abelian, so that
   $Rv$ is defined on $\operatorname{Ch}^+(\mathcal A)$ by
   [def-sp-kinjective-bridge], and $K\to I^\bullet$ is a quasi-isomorphism
   from a bounded-below complex $K$ to a bounded-below complex $I^\bullet$ of
   $v$-acyclic objects, then the natural map
   $\mathcal H^q(vI^\bullet)\to R^qvK$ is an isomorphism for every $q$.

In particular, for the etale direct image $v=f'_*$ [def-weil-pbc-direct-image]
on sheaves of $\mathbf F_\ell$-modules: a (bounded-below) complex $I^\bullet$
of $f'_*$-acyclic sheaves quasi-isomorphic to $K$ satisfies
$\mathcal H^q(f'_*I^\bullet)\cong R^qf'_*K$, computed with the K-injective
resolutions of [def-weil-pbc-kinjective-resolutions]. In particular, under
the injective-acyclicity property $\mathrm{IA}(f)$
[def-weil-pbc-injective-acyclicity-property] the sheaves $g'^{-1}I^m$ of an
injective resolution $E\to I^\bullet$ are $f'_*$-acyclic, so
$f'_*g'^{-1}I^\bullet$ computes $Rf'_*g'^{-1}E$.
