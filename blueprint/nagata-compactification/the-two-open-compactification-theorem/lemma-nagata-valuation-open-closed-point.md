+++
id = "lemma-nagata-valuation-open-closed-point"
kind = "lemma"
title = "An open containing the closed point of a valuation spectrum is total"
order = 488
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint.avoids"]
+++
Let $A$ be a valuation ring and let $O\subseteq\operatorname{Spec}(A)$ be
open. If the closed point $\mathfrak m_A$ belongs to $O$, then
$O=\operatorname{Spec}(A)$.

## Proof

Choose a basic open $D(a)$ with $\mathfrak m_A\in D(a)\subseteq O$.
Then $a\notin\mathfrak m_A$, hence $a$ is a unit of the local ring $A$ and
$D(a)=\operatorname{Spec}(A)$.
