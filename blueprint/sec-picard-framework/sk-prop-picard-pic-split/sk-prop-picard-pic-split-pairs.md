+++
id = "det-picard-pic-split-pairs"
kind = "lemma"
title = "Rigidified pairs have no automorphisms and compute the Picard functor"
uses = ["thm-pc-pic-split", "def-pc-pic-sigma-functor", "def-pc-picard-functor"]
+++
Let $f:C\to S$ be a morphism of schemes with a section $\sigma$ such that
$\cO_T\to f_{T,*}\cO_{C_T}$ is an isomorphism for every $S$-scheme $T$.
For an $S$-scheme $T$, a *rigidified pair* on $C_T$ is a pair
$(\cL,\alpha)$ with $\cL$ an invertible $\cO_{C_T}$-module and
$\alpha:\sigma_T^*\cL\xrightarrow{\sim}\cO_T$; an isomorphism
$(\cL,\alpha)\to(\cL',\alpha')$ is an isomorphism $\varphi:\cL\to\cL'$
with $\alpha'\circ\sigma_T^*\varphi=\alpha$. Then:

1. every rigidified pair has only the identity automorphism, and
between two isomorphic rigidified pairs there is exactly one
isomorphism;
1. the map $(\cL,\alpha)\mapsto[\cL]$ is a bijection from the set of
isomorphism classes of rigidified pairs on $C_T$ onto
$\operatorname{Pic}_{C/S,\sigma}(T)=\ker\bigl(\sigma_T^*:\operatorname{Pic}(C_T)\to\operatorname{Pic}(T)\bigr)$,
natural in $T$ (pullback of pairs);
1. composing with the isomorphism
$\operatorname{Pic}_{C/S,\sigma}\xrightarrow{\sim}\operatorname{Pic}_{C/S}$
of [thm-pc-pic-split], $\operatorname{Pic}_{C/S}(T)$ is naturally the set
of isomorphism classes of rigidified pairs on $C_T$.
