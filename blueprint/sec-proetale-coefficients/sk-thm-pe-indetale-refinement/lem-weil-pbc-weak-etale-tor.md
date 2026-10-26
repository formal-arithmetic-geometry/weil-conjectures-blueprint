+++
id = "lem-weil-pbc-weak-etale-tor"
kind = "lemma"
title = "Flat diagonal and Tor groups"
order = 914
lean = ["Ring.AbsolutelyFlat", "Ring.AbsolutelyFlat.of_flat_lmul'", "Ring.WeakDimensionLEOne", "Ring.WeakDimensionLEOne.of_weaklyEtale"]
uses = ["def-weil-pbc-ind-etale-algebra"]
+++
Let $A\to B$ be weakly etale [def-weil-pbc-ind-etale-algebra].

1. If $A$ is absolutely flat, i.e. every $A$-module is flat, then so is $B$.
2. If every finitely generated ideal of $A$ is flat (weak dimension at most
   one), then every finitely generated ideal of $B$ is flat.
