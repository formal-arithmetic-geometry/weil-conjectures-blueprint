+++
id = "lem-chow-closed-model"
kind = "lemma"
title = "Closed model of a quasi-compact immersion"
order = 1054
lean = ["AlgebraicGeometry.ProperClosedModel", "AlgebraicGeometry.nonempty_properClosedModel"]
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-chow-affine-immersion", "lem-weil-pbc-closed-immersion-proper", "lem-weil-pbc-proper-composition", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $S$ be a noetherian scheme, let $V$ be an affine scheme and let
$g\colon V\to S$ be locally of finite type. Then $g$ admits a *proper closed
model*: there are a finite set $n$, a scheme $Z$ with a closed immersion
$Z\to\mathbf P^n_S$ (homogeneous coordinates indexed by $n$), and an open
immersion $V\to Z$ identifying $V$ with a scheme-theoretically dense open
subscheme of $Z$, such that $V\to Z\to\mathbf P^n_S\to S$ equals $g$. For any
such model, $Z\to S$ is proper.

Concretely, one may take for $Z$ the scheme-theoretic image of a
(quasi-compact) immersion $j\colon V\to\mathbf P^n_S$ over $S$ as in
[lem-chow-affine-immersion].

## Proof

The first two assertions are 01RG applied to the quasi-compact
immersion $j$. For the last one, $\mathbf P^n_S\to S$ is proper by
01WC, a closed immersion is proper by 01W5, and
a composition of proper morphisms is proper; hence $Z\to S$ is proper.
