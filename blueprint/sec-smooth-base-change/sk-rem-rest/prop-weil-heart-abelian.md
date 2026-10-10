+++
id = "prop-weil-heart-abelian"
kind = "theorem"
title = "The heart is abelian"
order = 1425
uses = ["def-weil-t-structure"]
tags = ["latex:proposition"]
+++
For a t-structure $(\mathcal T^{\le0},\mathcal T^{\ge0})$ on a triangulated
category, the heart $\mathcal T^{\le0}\cap\mathcal T^{\ge0}$ of
[def-weil-t-structure] is abelian. Consequently every idempotent of the heart
splits: an idempotent $e:A\to A$ of an abelian category splits as
$A\cong\ker(e)\oplus\ker(\operatorname{id}_A-e)$, with $e$ carried to the
projection onto the second summand.

## Proof

For the heart defined in [def-weil-t-structure], the abelianity assertion is
the classical theorem of Beilinson, Bernstein and Deligne (Faisceaux
pervers, Théorème 1.3.6). Its only use below is that
the heart is idempotent complete: for an idempotent $e$ in an abelian
category the kernels $\ker(e)$ and $\ker(\operatorname{id}_A-e)$ are
supplementary subobjects of $A$, the map
$\ker(e)\oplus\ker(\operatorname{id}_A-e)\to A$ is an isomorphism
($\operatorname{id}_A=e+(\operatorname{id}_A-e)$, and the two kernels have
zero intersection), and under it $e$ becomes the projection onto the second
summand with the canonical maps of the split.
