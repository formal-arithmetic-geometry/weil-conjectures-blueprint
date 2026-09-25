+++
id = "sk-lem-minimal"
kind = "section"
title = "Minimal counterexamples occur over a point"
order = 1397
uses = ["sk-def-bc"]
+++
*Lemma (sketch).*

(Stacks Project, Lemma 59.88.5, Tag `0F06`.) Let $T$ be
quasi-compact quasi-separated and let $P$ be a property of qcqs
schemes over $T$ such that: (1) $P$ is invariant under thickenings;
(2) $P$ is compatible with limits with affine transition morphisms;
(3) if $Z\subseteq T'$ is closed with quasi-compact complement $V$
and $P(T')$ holds, then $P(V)$ or $P(Z)$ holds. Then $P(T)$
implies $P(\Spec K)$ for some morphism $\Spec K\to T$ with $K$ a
field.

## Proof

Zorn's lemma on the closed subschemes of $T$ satisfying $P$ gives a
minimal $T'$; it is reduced (by (1)), and its generic point
$\eta=\Spec K$ is the limit of the affine neighbourhoods $V$, whose
$P$-property follows from (3) by minimality; (2) gives
$P(\eta)$.

Uses: [sk-def-bc]
