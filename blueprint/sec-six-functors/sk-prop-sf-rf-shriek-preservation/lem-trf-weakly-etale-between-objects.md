+++
id = "lem-trf-weakly-etale-between-objects"
kind = "lemma"
title = "Morphisms between weakly etale objects"
order = 2073
lean = ["AlgebraicGeometry.WeaklyEtale.of_comp"]
+++
Let $U\to S$ and $V\to S$ be weakly etale morphisms.
Every $S$-morphism $f:U\to V$ is weakly etale.

## Proof

The morphism $V\to S$ is weakly etale and its composite with $f$ is the
weakly etale $U\to S$; a morphism whose composite with a weakly etale
morphism is weakly etale is itself weakly etale
([Stacks, Tag 0951](https://stacks.math.columbia.edu/tag/0951)).
