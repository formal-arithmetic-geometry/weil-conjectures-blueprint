+++
id = "fin4-lem-domination-trick"
kind = "lemma"
title = "The domination trick"
order = 1678
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-fin-closed-immersion", "lem-finrepair-modification-c", "lem-finrepair-modification-extension-zero", "lem-weil-pbc-grothendieck-spectral-sequence", "sbc-def-coefficient-conventions"]
+++
Let $S$ be of finite type over $k$, let $f:X\to S$ be
proper, let
$\pi:\bar X\to X$ be proper and surjective, and assume $\pi$ is an
isomorphism over a dense open $U\hookrightarrow X$; put
$\bar f=f\circ\pi$ and let $\iota:Z=X\setminus U\hookrightarrow X$ be
the closed complement. Write $P(g;e)$ for the assertion that for a
morphism $g$ all of whose
geometric fibres have
dimension at most $e$, the higher direct images $R^qg_*$ of
[def-weil-pbc-direct-image] preserve
constructible
$\Lambda$-sheaves (the ring $\Lambda$ of
[sbc-def-coefficient-conventions]) and vanish for $q>2e$. If
$P(\bar f;e)$ and $P(f\circ\iota;e)$ hold, then $P(f;e)$ holds.

## Proof

Discarding the bound clauses of the two hypotheses,
[lem-finrepair-modification-c] gives constructibility.
For vanishing use its exact sequence
$0\to j_!j^*F\to F\to\iota_*\iota^*F\to0$.
If $\bar j:\pi^{-1}(U)\hookrightarrow\bar X$, then
[lem-finrepair-modification-extension-zero] and
[lem-weil-pbc-grothendieck-spectral-sequence] identify
$R^qf_*j_!j^*F$ with
$R^q\bar f_*\bar j_!(\pi|_U)^*j^*F$.
It is zero for $q>2e$ by the first hypothesis.
The other outer term is $R^q(f\iota)_*\iota^*F$, using
[lem-fin-closed-immersion] and the same composition sequence;
it is zero for $q>2e$ by the second hypothesis.
The exact segment with these two outer terms proves vanishing
of $R^qf_*F$ for $q>2e$.
