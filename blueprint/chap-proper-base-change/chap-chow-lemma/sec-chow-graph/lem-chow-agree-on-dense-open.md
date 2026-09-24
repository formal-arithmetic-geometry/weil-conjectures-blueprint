+++
id = "lem-chow-agree-on-dense-open"
kind = "lemma"
title = "Two morphisms agreeing on a scheme-theoretically dense open"
order = 624
lean = ["AlgebraicGeometry.ext_of_isSchemeTheoreticallyDominant"]
+++
Let $T$ and $Y$ be schemes over $S$ with $Y\to S$ separated, let
$a,b\colon T\to Y$ be morphisms of $S$-schemes and let $V\subseteq T$ be a
scheme-theoretically dense open subscheme with $a|_V=b|_V$. Then $a=b$.

## Proof

This is 01RH. Concretely, the equaliser of $a$ and $b$ is the
base change of the diagonal $Y\to Y\times_S Y$ along
$(a,b)\colon T\to Y\times_S Y$, hence a closed subscheme of $T$ because
$Y\to S$ is separated; it contains $V$, which is scheme-theoretically dense, so
it is all of $T$.
