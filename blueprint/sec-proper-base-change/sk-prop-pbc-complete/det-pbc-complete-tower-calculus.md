+++
id = "det-pbc-complete-tower-calculus"
kind = "lemma"
title = "Calculus of towers: evaluation, derived limits, direct and inverse images"
order = 1324
uses = ["det-pbc-complete-towers", "sk-prop-pe-products", "sk-prop-pe-milnor", "lem-weil-derived-limit-existence", "sk-prop-sfb-module-pullback-exact"]
+++
In the notation of [det-pbc-complete-towers], let $u\colon T'\to T$ be a
morphism of schemes.

1. $\operatorname{Tow}(T)$ is a Grothendieck abelian category. Each
   $\operatorname{ev}_n$ is exact and has an exact left adjoint, so it carries
   K-injective complexes of towers to K-injective complexes of modules.
2. A morphism $a$ of $D(\operatorname{Tow}(T))$ is an isomorphism if and only if
   $\operatorname{ev}_n(a)$ is an isomorphism in $D(T_{\mathrm{proét}},\mathcal O_E)$
   for every $n$.
3. $\operatorname{ev}_n\circ u^*_{\operatorname{Tow}}=u^*\circ\operatorname{ev}_n$ and
   $\operatorname{ev}_n\circ Ru^{\operatorname{Tow}}_*\simeq Ru_*\circ\operatorname{ev}_n$,
   compatibly with the units and counits of $u^*\dashv Ru_*$ and
   $u^*_{\operatorname{Tow}}\dashv Ru^{\operatorname{Tow}}_*$.
4. There is a canonical isomorphism
   $Ru_*\circ R\varprojlim\simeq R\varprojlim\circ Ru_*^{\operatorname{Tow}}$ of
   functors $D(\operatorname{Tow}(T'))\to D(T_{\mathrm{proét}},\mathcal O_E)$.
5. $R\varprojlim$ is exact. For an exact equivalence
   $F\colon\Mod_{\mathcal O_{E,T}}\to\Mod_{\mathcal O_{E,T'}}$, applied levelwise
   as $F^{\operatorname{Tow}}$, one has $F\circ R\varprojlim\simeq
   R\varprojlim\circ F^{\operatorname{Tow}}$; and
   $R\varprojlim(M_\bullet)\otimes_{\mathcal O_{E,T}}P\simeq
   R\varprojlim(M_\bullet\otimes_{\mathcal O_{E,T}}P)$ for every bounded complex
   $P$ of finite free $\mathcal O_{E,T}$-modules.
