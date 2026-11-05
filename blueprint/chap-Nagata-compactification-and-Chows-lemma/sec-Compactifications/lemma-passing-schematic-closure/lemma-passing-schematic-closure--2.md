+++
id = "lemma-passing-schematic-closure--2"
kind = "lemma"
title = "Direct image along a refinement"
name_showing = false
order = 1412002
aliases = ["bp-r437-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerShriekRefinementIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleLowerShriekRefinementIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso'"]
uses = ["lemma-passing-schematic-closure--1", "definition-compactification-refinement"]
+++
Lean uses the following composition of the refinement comparison with
derived direct image in place of a separate schematic-closure statement.

Keep the field, coefficients, open immersions and cartesian square of
[lemma-passing-schematic-closure--1], but allow $h$ to be any $k$-morphism.
Let $S$ be separated and of finite type over $k$, and let
$p:\overline X\to S$ and $q:Z\to S$ be $k$-morphisms with $p\circ h=q$.
Assume that the natural comparison $\rho:j_!\to Rh_*j'_!$ is an
isomorphism. Then there is a canonical natural isomorphism of functors
$\Dbc(X,\Lambda)\to\Dbc(S,\Lambda)$,

$$
Rp_*j_!\simeq Rq_*j'_!.
$$

For $\Lambda=\Qbarl$ there is also a construction with the hypothesis
that the exchange map $j_!R(\mathrm{id}_X)_*\to Rh_*j'_!$ is an
isomorphism. In particular, when $h$ is proper both hypotheses hold.
For a refinement of compactifications as in
[definition-compactification-refinement], this identifies the two
functors defining direct image with compact support. Taking
$h=i:Z\hookrightarrow\overline X$ to be the schematic-closure inclusion
gives, in this coefficient and bounded constructible setting,

$$
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K.
$$
