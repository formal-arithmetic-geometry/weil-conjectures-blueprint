+++
id = "lem-exc-closed-restriction-extension-zero"
kind = "lemma"
title = "Closed restriction of open extension by zero"
order = 1911
uses = ["def-weil-extension-by-zero", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "lem-weil-extension-by-zero-adjunction", "prop-weil-pbc-proetale-constant-ring-map"]
+++
For complementary open and closed immersions $j:U\hookrightarrow X$ and
$i:Z\hookrightarrow X$, one has $i^*j_!M=0$ for every
constant-coefficient pro-etale module sheaf $M$ on $U$.

## Proof

Write $\Lambda[V]$ for the free module sheaf on the representable sheaf of
an object $V\to U$. The extension-by-zero adjunction identifies
$j_!\Lambda[V]$ with the free module sheaf on the same scheme $V$, now over
$X$: both have maps to $N$ equal to $N(V)$. Scheme inverse image sends a
representable to its base change. It preserves free modules, since it
preserves coproducts and the constant ring. Thus
$i^*j_!\Lambda[V]=\Lambda[V\times_XZ]=0$. Every module sheaf has a
presentation by direct sums of such free sheaves: take one generator for
each local section and then generators for the kernel of the resulting
epimorphism. Both $j_!$ and $i^*$ preserve coproducts and cokernels as left
adjoints. Applying them to this presentation proves $i^*j_!M=0$ for
arbitrary $M$.
