+++
id = "lemma-nagata-flat-pullback-ideal-pow"
kind = "lemma"
title = "Flat pullback commutes with ideal powers"
lean = ["Ideal.range_powLiftBaseChange", "Ideal.injective_powLiftBaseChange_of_flat"]
order = 236
uses = ["def-nagata-extended-ideal"]
+++
Let $A\to B$ be a ring map, let $I\subseteq A$ be an ideal and let
$n\geq0$. The image of the $B$-linear map

$$
B\otimes_A I^n\longrightarrow B,\qquad b\otimes x\longmapsto bx,
$$

is $(IB)^n$. If $B$ is flat over $A$, this map is injective, so
$B\otimes_A I^n\cong(IB)^n$.
