+++
id = "lem-weil-pbc-leray-acyclicity"
kind = "lemma"
title = "Leray acyclicity criterion"
order = 2122
lean = ["AlgebraicGeometry.Etale.rightDerived_of_acyclicResolution"]
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-kinjective-resolutions"]
+++
Let $F\to I^\bullet$ be a resolution by $f'_*$-acyclic sheaves and let $v$ be
a left exact functor. If every $I^m$ is $v$-acyclic, then $Rv(F)$ is
represented by $v(I^\bullet)$. Applied to $v=f'_*$ and $g'^{-1}I^m$, this
identifies the cohomology of the target of exchange with the cohomology of
the termwise underived target.

## Proof

Resolve $K\to I^\bullet$ by a bounded-below Cartan--Eilenberg double complex
and apply $v$: filtering the total complex by the first degree gives the
spectral sequence

$$
 E_1^{r,s}=R^rv(I^s)\Longrightarrow\mathcal H^{r+s}(RvK).
$$

The assumed acyclicity collapses the first column, so the edge map identifies
$\mathcal H^q(vI^\bullet)$ with $R^qvK$, compatibly with the K-injective
presentation of [def-weil-pbc-kinjective-resolutions].
