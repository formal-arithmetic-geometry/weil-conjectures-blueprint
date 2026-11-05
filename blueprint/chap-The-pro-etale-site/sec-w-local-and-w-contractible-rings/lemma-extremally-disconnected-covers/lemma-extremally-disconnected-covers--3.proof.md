+++
kind = "proof"
of = "lemma-extremally-disconnected-covers--3"
order = 53007
+++
Let $S$ be extremally disconnected and Hausdorff. By
clause [definition-w-local-w-strictly-local--1], the closure of every open subset of $S$ is open,
hence clopen. Let $s\neq s'$ be points of $S$, and choose disjoint open sets
$U\ni s$ and $V\ni s'$, which exist because $S$ is Hausdorff. The closure
$\overline U$ is clopen and contains $s$. It does not contain $s'$, since $V$
is an open neighbourhood of $s'$ that does not meet $U$. Hence $\overline U$
separates $s$ from $s'$. Neither compactness nor regularity is used.

If $S$ is moreover compact, then it is a compact Hausdorff space in which
clopen subsets separate points. A compact Hausdorff space in which clopen subsets separate points is profinite: the map to the inverse limit of its finite quotients by finite partitions into clopen subsets is continuous, injective because clopen subsets separate points, and surjective by compactness, and a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

*Source:* the proof of Lemma [lemma-extremally-disconnected-covers].
