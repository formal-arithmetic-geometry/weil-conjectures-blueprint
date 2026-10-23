+++
id = "lemma-weil-pbc-completed-pullback-reduction"
kind = "lemma"
title = "Reduction commutes with completed pullback"
order = 2041
lean = ["AlgebraicGeometry.ProEtale.completedUpperStar", "DerivedCategory.isIso_derivedCompletionAdjunction_unit_app"]
uses = ["det-pbc-complete-derived-completion"]
+++
In the notation of [det-pbc-complete-derived-completion], let $g:T'\to T$ be a
morphism of schemes. The *completed inverse image* of $M\in D(T)$ is the derived
completion of the derived inverse image,

$$
g^*_{\mathrm{comp}}M=\widehat{g^*M}\simeq R\varprojlim_n\bigl(g^*M\otimes^{\mathbf L}_RR/I^n\bigr)
\in D(T'),
$$

a functor from $D(T)$ to the derived complete objects of $D(T')$. Then:

1. $g^*_{\mathrm{comp}}M$ is derived complete, and for every $n$ there is an
   isomorphism $(g^*_{\mathrm{comp}}M)\otimes^{\mathbf L}_RR/I^n\simeq g^*(M_n)$,
   functorial in $M$ and compatible with the transition maps;
2. the completion map $\kappa_{g^*M}\colon g^*M\to g^*_{\mathrm{comp}}M$ is an
   isomorphism if and only if $g^*M$ is derived complete.
