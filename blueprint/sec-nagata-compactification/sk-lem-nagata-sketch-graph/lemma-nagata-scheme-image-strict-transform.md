+++
id = "lemma-nagata-scheme-image-strict-transform"
kind = "lemma"
title = "[stacks-project]"
order = 240
lean = ["AlgebraicGeometry.Scheme.Hom.ker_lift_admissibleBlowup"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "lemma-nagata-scheme-image-ideal-qc", "prop-nagata-global-blowup-cover-independent"]
+++
Let $x\colon X\to S$ and $y\colon Y\to S$ be morphisms of schemes, let
$U\subseteq X$ be an open subscheme, and let $X'\to X$ be a $U$-admissible
blow-up, i.e. the blow-up of a finite-type quasi-coherent ideal sheaf $I$
whose support is disjoint from $U$. Write $W\subseteq X$ for the complement
of the support of $I$ and $\rho\colon X'\times_SY\to X\times_SY$ for the base
change of the blow-up. Let $h\colon V\to X\times_SY$ be quasi-compact, and
assume its projection to $X$ factors through $U$. Let $Z$ be its
scheme-theoretic image. Let $h'\colon V\to X'\times_SY$ be a lift of $h$,
i.e. $\rho\circ h'=h$ (such a lift exists and is unique, via the canonical
isomorphism $\varepsilon\colon X'\times_XU\cong U$ from
[thm-nagata-global-blowup-complement]: its $X'$-component is obtained from
$V\to U$ by $\varepsilon^{-1}\colon U\to X'\times_XU\to X'$ and its
$Y$-component is the given projection $V\to Y$). Assume that the inclusion of
the open part of $Z\times_{X\times_SY}(X'\times_SY)$ lying over the preimage
of $W$ in $X\times_SY$ is a quasi-compact morphism. Then the scheme-theoretic
image of $h'$ equals the strict transform of $Z$ along $\rho$ (relative to the
preimage of $W$), as closed subschemes of $X'\times_SY$; that is, the two
closed immersions into $X'\times_SY$ have the same kernel ideal sheaf.
