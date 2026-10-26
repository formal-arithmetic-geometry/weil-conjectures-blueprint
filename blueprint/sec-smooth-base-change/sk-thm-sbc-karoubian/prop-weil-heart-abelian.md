+++
id = "prop-weil-heart-abelian"
kind = "theorem"
title = "The heart is abelian"
lean = ["CategoryTheory.Triangulated.TStructure.abelianHeart", "CategoryTheory.Triangulated.TStructure.isIdempotentComplete_heart"]
order = 2093
uses = ["def-weil-t-structure"]
tags = ["latex:proposition"]
+++
For a t-structure $(\mathcal T^{\le0},\mathcal T^{\ge0})$ on a triangulated
category, the heart $\mathcal T^{\le0}\cap\mathcal T^{\ge0}$ of
[def-weil-t-structure] is abelian. Consequently every idempotent of the heart
splits: an idempotent $e:A\to A$ of an abelian category splits as
$A\cong\ker(e)\oplus\ker(\operatorname{id}_A-e)$, with $e$ carried to the
projection onto the second summand.
