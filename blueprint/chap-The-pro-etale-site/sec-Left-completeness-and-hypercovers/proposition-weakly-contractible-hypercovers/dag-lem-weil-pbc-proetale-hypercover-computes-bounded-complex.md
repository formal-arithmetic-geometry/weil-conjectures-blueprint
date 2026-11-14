+++
id = "dag-lem-weil-pbc-proetale-hypercover-computes-bounded-complex"
kind = "dag-lemma"
title = "Acyclic pro-etale hypercover model for a bounded-below module complex"
name_showing = false
order = 103509
tags = ["sheaf-dag"]
split_from = "proposition-weakly-contractible-hypercovers--2"
dag_id = "lem-weil-pbc-proetale-hypercover-computes-bounded-complex"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.ProEt.hypercover_computes_boundedBelow_complex"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be a scheme `def-pc-scheme`, with small pro-etale site and universes [dag-def-weil-pbc-proetale-site] `def-weil-size-convention`. Let $R$ be a sheaf of commutative rings on that site, $W$ a site object, and $U_\bullet\to W$ a hypercover whose terms are weakly contractible, with these notions as in `lem-weil-pbc-proetale-affine-acyclic-hypercover`. Let $E^\bullet$ be a complex of sheaves of $R$-modules `def-weil-sheaf-of-modules-category` with $E^q=0$ for $q<N$, for some integer $N$. Define the total complex of $B^{p,q}=E^q(U_p)$, $p\geq0$, by $\operatorname{Tot}(B)^r=\bigoplus_{p+q=r,\,p\geq0}E^q(U_p)$ and differential $\delta+(-1)^p d_E$ on $B^{p,q}$, where $\delta=\sum_{j=0}^{p+1}(-1)^j d_j^*$ is the alternating face restriction. Each displayed sum is finite because $N\leq q\leq r$. Then there is an isomorphism in $D(R(W)\text{-}\operatorname{Mod})$ `def-weil-abstract-derived-category`, natural in $E^\bullet$, $$\operatorname{Tot}(B)\simeq R\Gamma(W,QE^\bullet).$$ Here $Q$ is localization at quasi-isomorphisms and $R\Gamma(W,-)$ means derived evaluation: replace $E^\bullet$ by a bounded-below complex $J^\bullet$ of injective module sheaves and a quasi-isomorphism $E^\bullet\to J^\bullet$, and take $J^\bullet(W)$. Existence of such chain-level resolutions and their K-injectivity are as in `lem-sc-bounded-below-injective-resolution`. In particular every quasi-isomorphism of bounded-below complexes induces a quasi-isomorphism of these total complexes.

(SHEAF DAG node `lem-weil-pbc-proetale-hypercover-computes-bounded-complex`; machine-alignment layer.) Split from [proposition-weakly-contractible-hypercovers--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-abstract-derived-category`, `def-weil-pbc-proetale-hypercover-total`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `lem-weil-pbc-simplicial-matching-object`, `sk-def-pbc-conventions`.
