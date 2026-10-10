+++
id = "lem-weil-pbc-derived-functor-truncation-iso"
kind = "lemma"
title = "Low-degree cohomology of a right derived functor sees only low degrees"
uses = ["def-sp-left-exact-additive", "def-sp-grothendieck-abelian", "def-sp-kinjective-bridge", "def-weil-pbc-bounded-derived-subcategories", "def-weil-abstract-derived-category", "def-sbc-standard-tstructure-derived-category"]
refines = "proof/lemma-weil-pbc-exact-couple-abutment"
tags = ["sheaf-dag", "stacks-05TC"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor [def-sp-left-exact-additive] between Grothendieck abelian categories [def-sp-grothendieck-abelian], with right derived functor $Rv:D^+(\mathcal A)\to D^+(\mathcal B)$ computed by K-injective resolutions [def-sp-kinjective-bridge]. Let $n\in\mathbf Z$ and let $c:L\to M$ be a morphism of $D^+(\mathcal A)$ [def-weil-pbc-bounded-derived-subcategories] such that $\mathcal H^i(c):\mathcal H^i(L)\to\mathcal H^i(M)$ (cohomology functors of [def-weil-abstract-derived-category]) is an isomorphism for every $i\leq n$ and a monomorphism for $i=n+1$. Then $\mathcal H^j(Rv(c)):\mathcal H^j(RvL)\to\mathcal H^j(RvM)$ is an isomorphism for every $j\leq n$. In particular, for $K\in D^+(\mathcal A)$ and the canonical truncation $c_n:\tau_{\leq n}K\to K$ [def-sbc-standard-tstructure-derived-category] (of a bounded below complex representing $K$), the map $\mathcal H^n(Rv\,\tau_{\leq n}K)\to\mathcal H^n(RvK)$ induced by $c_n$ is an isomorphism.
