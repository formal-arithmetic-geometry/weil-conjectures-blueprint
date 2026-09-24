+++
id = "lemma-weil-pbc-epsilon-factorization-index-filtered-v1"
kind = "lemma"
title = "The etale factorization index is filtered"
order = 1871
uses = ["def-weil-pbc-epsilon-factorization-index-v1", "lemma-weil-pbc-etale-proetale-left-exact"]
+++
For every $W$, the category $I_W$ is nonempty and filtered.

## Proof

The structural map $W\to X=\iota_XX$ gives an object. Two factorizations
through $U_1$ and $U_2$ are dominated by the factorization through
$U_1\times_XU_2$, since $\iota_X$ preserves this fibre product. For two
parallel arrows $h_0,h_1:U'\rightrightarrows U$ that agree after precomposition
with $W\to\iota_XU'$, their equalizer is the pullback of the diagonal of the
etale morphism $U\to X$. This diagonal is an open immersion, so the
equalizer is an etale open subobject of $U'$ through which $W$ factors. The
resulting object receives a morphism from $(a',U')$ and equalizes the two
arrows in $I_W$. These are the three filteredness axioms.
