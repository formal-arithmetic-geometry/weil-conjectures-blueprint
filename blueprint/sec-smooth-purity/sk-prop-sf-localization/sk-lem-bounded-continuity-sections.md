+++
id = "det-lem-bounded-continuity-sections"
kind = "lemma"
title = "Hypercohomology on a qcqs scheme commutes with bounded-below filtered colimits"
order = 3236
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections", "sk-thm-pe-weakly-contractible-basis"]
+++
Let $Y$ be a qcqs scheme, $A$ a sheaf of rings on $Y_{\mathrm{proét}}$, and let
$W_\bullet\to Y$ be a hypercovering by affine weakly contractible objects with each $W_n$
quasi-compact (a finite disjoint union of affines).

1. An additive functor $\Phi$ between Grothendieck abelian categories that is exact and
   commutes with arbitrary direct sums commutes with all small colimits; in particular
   $M\mapsto M(W_n)$, from $A$-modules to abelian groups, commutes with filtered colimits.
2. For a complex $K^\bullet$ of $A$-modules vanishing in degrees $<a$,
   $H^q(Y,K^\bullet)=H^q\operatorname{Tot}(K^m(W_n))_{m,n}$, and the degree-$q$ term
   $\bigoplus_{n+m=q,\,n\ge0,\,m\ge a}K^m(W_n)$ of the total complex is a finite direct sum.
3. For a filtered diagram $(K_i^\bullet)$ of such complexes with a common $a$, the map
   $\varinjlim_iH^q(Y,K_i^\bullet)\to H^q(Y,\varinjlim_iK_i^\bullet)$ is an isomorphism.
