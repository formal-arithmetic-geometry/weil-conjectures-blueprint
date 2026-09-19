+++
id = "lemma-nagata-standard-etale-finite-part-package"
kind = "lemma"
title = "Standard-etale finite-part package"
order = 368
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

If $q\colon Z\to X$ is separated and quasi-finite and $x\in X$, there are
finitely many points $z_i\in Z_x$ and an elementary etale neighbourhood
$(T,t)\to(X,x)$ on which pairwise disjoint standard-etale neighbourhoods of
the $z_i$ glue to an open-and-closed finite part $V\subseteq Z_T$; the
complement has empty fibre over $t$.

## Proof

Quasi-finiteness makes $Z_x$ finite. For each $z_i$, choose an affine
neighbourhood and an element whose image in the fibre cuts out only $z_i$.
The corresponding standard-etale algebra is finite over a neighbourhood of
$x$ and etale at $z_i$. Shrinking the base and taking the fibre product of
these finitely many neighbourhoods makes them pairwise disjoint. Their
union is open-and-closed and finite over the resulting elementary etale
neighbourhood; separatedness identifies its complement, which misses $t$.
