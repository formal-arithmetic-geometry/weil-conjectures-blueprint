+++
id = "lem-weil-pbc-derived-exchange-replacement"
kind = "lemma"
title = "Replacement independence and naturality of derived exchange"
order = 1202
uses = ["def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-kinjective-resolutions", "lem-weil-pbc-derived-exchange-termwise"]
+++
Let $K\to I$ and $K\to J$ be two K-injective resolutions
[def-weil-pbc-kinjective-resolutions]. Every comparison $I\to J$ over $K$
gives the same derived exchange morphism of the derived exchange morphism
[def-weil-pbc-derived-exchange-detailed], and two such comparisons are
chain-homotopic. Consequently $\Ex_{\square,K}$ is independent of the
resolution and is natural in $K$.

## Proof

The comparison lemma for K-injective resolutions stated in
[def-weil-pbc-kinjective-resolutions] supplies the chain maps and their
homotopy uniqueness; by [lem-weil-pbc-derived-exchange-termwise] the termwise
underived exchange on such a resolution computes the derived exchange
morphism $\Ex_{\square,K}$ of [def-weil-pbc-derived-exchange-detailed], so
any two comparisons over $K$ give the same morphism of the derived category,
and the naturality of $\Ex_{\square,K}$ in $K$ follows from the naturality of
the underived exchange.
