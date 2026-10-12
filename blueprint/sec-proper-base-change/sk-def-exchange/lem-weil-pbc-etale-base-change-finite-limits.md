+++
id = "lem-weil-pbc-etale-base-change-finite-limits"
kind = "lemma"
title = "The base-change functor between small etale sites commutes with finite limits"
order = 1056
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["CategoryTheory.MorphismProperty.Over.instPreservesFiniteLimitsTopPullback"]
tags = ["mathlib", "stacks-021D"]
+++
Let $u:U\to V$ be a morphism of schemes [def-pc-scheme], and let $V_{\Et}$, $U_{\Et}$ be the small etale sites [def-weil-pbc-etale-site] (objects: etale morphisms $W\to V$, resp. $W'\to U$; morphisms: morphisms over the base). Then:

1. for an object $W\to V$ of $V_{\Et}$ the base change $U\times_VW\to U$ is etale, and $W\mapsto U\times_VW$, $(g:W_1\to W_2)\mapsto\mathrm{id}_U\times g$, is a functor $b_u:V_{\Et}\to U_{\Et}$;
2. the categories $V_{\Et}$ and $U_{\Et}$ have all finite limits: $\mathrm{id}_V:V\to V$ is a final object of $V_{\Et}$, and for morphisms $W_1\to W\leftarrow W_2$ in $V_{\Et}$ the scheme-theoretic fibre product $W_1\times_WW_2$, with its map to $V$, is etale over $V$ and is a fibre product in $V_{\Et}$;
3. $b_u$ commutes with finite limits: $b_u(V/V)=U\times_VV\cong U$ is a final object of $U_{\Et}$, and the canonical morphism $U\times_V(W_1\times_WW_2)\to(U\times_VW_1)\times_{U\times_VW}(U\times_VW_2)$ is an isomorphism.
