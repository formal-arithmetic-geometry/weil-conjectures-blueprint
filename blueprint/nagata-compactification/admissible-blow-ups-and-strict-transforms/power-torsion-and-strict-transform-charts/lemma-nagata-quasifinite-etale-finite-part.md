+++
id = "lemma-nagata-quasifinite-etale-finite-part"
kind = "lemma"
title = "Etale finite part of a quasi-finite separated morphism, [stacks-project]"
order = 369
uses = ["lemma-nagata-standard-etale-finite-part-package"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be quasi-finite and separated and let $x\in X$.
There is an elementary etale neighbourhood $(T,t)\to(X,x)$ and a
decomposition $Z\times_XT=V\amalg W$ into open-and-closed subschemes such
that $V\to T$ is finite and $W_t=\varnothing$.

## Proof

Apply [lemma-nagata-standard-etale-finite-part-package]; its $T,t,V$
and open-and-closed complement $W$ give the required decomposition.
