+++
id = "lemma-nagata-compactification-base-change"
kind = "lemma"
title = "Base change of a compactification"
order = 76
lean = ["AlgebraicGeometry.HasCompactification.of_isPullback"]
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-compactification-base-change"]
+++
The constructed factorization $C_{S'}$ is a compactification of
$X\times_SS'\to S'$. Consequently, if $f\colon X\to S$ is compactifiable,
then so is every base change $u\colon X'\to S'$ of $f$ along a morphism
$S'\to S$.

## Proof

Let $C=(X\xrightarrow{j}\overline X\xrightarrow{p}S)$. Open immersions and
proper morphisms are stable under arbitrary base change, so
$X\times_SS'\to\overline X\times_SS'$ (the base change of $j$) is an open
immersion and $\overline X\times_SS'\to S'$ (the base change of $p$) is
proper. The factorization equality follows from the universal property of
the two fibre products. Hence $C_{S'}$ is a compactification of
$X\times_SS'\to S'$.

For the second assertion, let $u\colon X'\to S'$ be a base change of $f$
along $S'\to S$, i.e. a cartesian square with top map $h\colon X'\to X$, and
choose a compactification $C$ of $f$ ([def-nagata-compactifiable]). The
square identifies $X'$ with $X\times_SS'$ over $S'$, and under this
isomorphism the base-changed factorization of $u$ in
[def-nagata-compactification-base-change] is $C_{S'}$ composed with an
isomorphism; composing an open immersion with an isomorphism is again an
open immersion. Hence it is a compactification of $u$, and $u$ is
compactifiable.
