+++
id = "lem-chow-agree-on-dense-open"
kind = "lemma"
title = "Two morphisms agreeing on a scheme-theoretically dense open"
order = 1056
lean = ["AlgebraicGeometry.ext_of_isSchemeTheoreticallyDominant"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-closed-immersion-products"]
+++
Let $g\colon Y\to S$ be a separated morphism of schemes, let
$a,b\colon T\to Y$ be morphisms with $g\circ a=g\circ b$, and let
$v\colon V\to T$ be a scheme-theoretically dominant morphism
[def-nagata-scheme-theoretic-image] (for instance the inclusion of a
scheme-theoretically dense open subscheme) with $a\circ v=b\circ v$. Then
$a=b$.

## Proof

This is 01RH. Concretely, the equaliser of $a$ and $b$ is the
base change of the diagonal $Y\to Y\times_S Y$ along
$(a,b)\colon T\to Y\times_S Y$, hence a closed subscheme of $T$ because
$Y\to S$ is separated; it contains $V$, which is scheme-theoretically dense, so
it is all of $T$.
