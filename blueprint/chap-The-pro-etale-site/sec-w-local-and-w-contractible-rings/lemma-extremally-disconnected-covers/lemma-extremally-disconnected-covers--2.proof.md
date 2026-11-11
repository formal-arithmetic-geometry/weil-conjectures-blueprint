+++
kind = "proof"
of = "lemma-extremally-disconnected-covers--2"
order = 53005
uses = ["lemma-extremally-disconnected-covers--1"]
+++
A profinite space is compact Hausdorff, so clause [lemma-extremally-disconnected-covers--1] gives a
continuous surjection $S\to T$ with $S$ compact Hausdorff and extremally
disconnected, for instance $S=\beta(T^\delta)$. It remains to see that $S$ is
profinite. By the definition of extremal disconnectedness
(clause [definition-w-local-w-strictly-local--1]), the closure of every open subset of $S$ is open,
hence clopen. Let $s\neq s'$ be points of $S$. Since $S$ is Hausdorff, there
are disjoint open sets $U\ni s$ and $V\ni s'$. The closure $\overline U$ is
clopen and contains $s$. It does not contain $s'$, because $V$ is an open
neighbourhood of $s'$ that does not meet $U$. Thus clopen subsets separate
the points of $S$. A compact Hausdorff space in which clopen subsets separate points is profinite: the map to the inverse limit of its finite quotients by finite partitions into clopen subsets is continuous, injective because clopen subsets separate points, and surjective by compactness, and a continuous bijection from a compact space to a Hausdorff space is a homeomorphism. Hence $S$ is profinite.

*Source:* the proof of Lemma [lemma-extremally-disconnected-covers].
