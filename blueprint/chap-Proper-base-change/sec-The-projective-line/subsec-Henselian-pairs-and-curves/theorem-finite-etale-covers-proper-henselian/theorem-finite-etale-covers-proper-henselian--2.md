+++
id = "theorem-finite-etale-covers-proper-henselian--2"
kind = "remark"
title = "Lifting finite covers"
order = 357001
aliases = ["bp-r108-2"]
lean = ["AlgebraicGeometry.Scheme.isEquivalence_pullback_finiteEtale_of_henselianRing"]
uses = []
+++
*Lifting finite étale covers over a proper henselian pair.*
Let $(B,J)$ be a henselian pair, let $Y$ be proper over $B$, and let
$i:Y_0\to Y$ be the closed fibre
$Y_0=Y\times_{\operatorname{Spec}B}\operatorname{Spec}(B/J)$.
Base change along $i$ is an equivalence between the categories of finite
étale schemes over $Y$ and over $Y_0$,

$$
\textit{F\'Et}_Y\xrightarrow{\sim}
\textit{F\'Et}_{Y_0}.
$$

This is [Stacks, [0GS2](https://stacks.math.columbia.edu/tag/0GS2)].

*Proof.* We prove full faithfulness and essential surjectivity separately.

For full faithfulness, let $U,V$ be finite étale over $Y$. A morphism
$U\to V$ over $Y$ is determined by its graph in $V\times_YU$, an open
and closed subscheme whose projection to $U$ is an isomorphism. This
description commutes with base change. Restriction to the closed fibre
is a bijection on open and closed subsets of any proper scheme over the
henselian pair. Apply this to $U$ and $V\times_YU$, which are proper
over $B$. A graph on the closed fibre therefore lifts uniquely to an
open and closed subscheme $W\subset V\times_YU$. The finite étale map
$W\to U$ has rank one on the closed fibre. Its rank-one locus is open
and closed, and injectivity of restriction on open and closed subsets
of $U$ shows that this locus is all of $U$. Thus $W\to U$ is an
isomorphism. We have lifted the morphism uniquely, proving full
faithfulness.

For essential surjectivity, first suppose that $B$ is Noetherian and
$J$-adically complete. A finite étale cover of $Y_0$ lifts compatibly to
the infinitesimal thickenings over $B/J^{n+1}$ by topological invariance
of the étale site. Grothendieck algebraization gives a finite cover of
$Y$. It is étale near the closed fibre; properness and the inclusion of
$J$ in the Jacobson radical show that every point of the cover
specializes to the closed fibre, so it is étale everywhere.

For a Noetherian henselian G-ring, apply the complete case after
completion and descend the resulting cover to a finitely presented
$B$-algebra mapping to the completion. Henselian approximation gives
a map from this algebra to $B$ agreeing modulo $J$. Pulling back along
this map gives the desired lift. For a general henselian pair, descend
the proper scheme and its finite étale closed-fibre cover to finite-type
models over $\mathbf Z$, henselize the corresponding pairs, and apply
the G-ring case. Base change back to $B$ gives the prescribed cover of
$Y_0$. The proper-model approximation uses Chow's lemma
[theorem-chow-s-lemma-projective-form] and scheme-theoretic images
[lemma-schematic-closure-uniqueness].

This constructs a lift on the chosen fibre product. Transport along
the canonical isomorphism from $Y_0$ to that fibre product gives
essential surjectivity for the specified map $i$. Together with full
faithfulness, it proves the equivalence.
