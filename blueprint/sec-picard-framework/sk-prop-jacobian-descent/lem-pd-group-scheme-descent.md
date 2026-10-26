+++
id = "lem-pd-group-scheme-descent"
kind = "lemma"
title = "The descended scheme is a group scheme"
lean = ["CategoryTheory.Over.DescentDatum.existsUnique_grpObj_of_isPullback", "CategoryTheory.Over.DescentDatum.exists_commGrpObj_of_isPullback"]
order = 860
uses = ["def-pc-base-change", "def-pd-descent-datum", "def-sc-group-scheme", "lem-pd-morphisms-descend"]
+++
Let $p:X\to Y$ be a faithfully flat (flat and surjective) and quasi-compact
morphism of schemes, and let $V$ be a group scheme over $X$ (defined as in
[def-sc-group-scheme], with the base field replaced by the base scheme $X$).
Let $V$ carry a descent datum over
$X/Y$ which is effective with descended scheme $V_0$ over $Y$, so that
$V\cong V_0\times_YX$, and suppose that the multiplication and the unit of $V$
are compatible with the descent datum. Then $V_0$ carries a unique group
scheme structure over $Y$ whose base change to $X$ is the given one. If
moreover $V$ is commutative, so is $V_0$.
