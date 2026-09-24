+++
id = "lem-chow-closed-model"
kind = "lemma"
title = "Closed model of a quasi-compact immersion"
order = 619
lean = ["AlgebraicGeometry.ProperClosedModel", "AlgebraicGeometry.nonempty_properClosedModel"]
uses = ["lem-chow-affine-immersion"]
+++
Let $S$ be a scheme and let $j\colon V\to\mathbf P^n_S$ be a quasi-compact
immersion. Let $Z\subseteq\mathbf P^n_S$ be the scheme-theoretic image of $j$.
Then $Z$ is a closed subscheme of $\mathbf P^n_S$, the induced morphism
$V\to Z$ is an open immersion identifying $V$ with a scheme-theoretically dense
open subscheme of $Z$, and $Z\to S$ is proper.

The formalisation packages this data as a structure
`ProperClosedModel`, in the case in which it is used below: $S$ is
noetherian and $g\colon V\to S$ is locally of finite type with $V$ affine, so
that $j$ is supplied by [lem-chow-affine-immersion] and is automatically
quasi-compact because $V$ is then noetherian.

## Proof

The first two assertions are 01RG applied to the quasi-compact
immersion $j$. For the last one, $\mathbf P^n_S\to S$ is proper by
01WC, a closed immersion is proper by 01W5, and
a composition of proper morphisms is proper; hence $Z\to S$ is proper.
