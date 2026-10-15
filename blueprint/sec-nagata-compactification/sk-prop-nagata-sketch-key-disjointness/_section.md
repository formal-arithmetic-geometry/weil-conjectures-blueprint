+++
id = "sk-prop-nagata-sketch-key-disjointness"
kind = "proposition"
title = "Improved comparison and key disjointness"
order = 125
uses = ["sk-lem-nagata-sketch-image-transform", "sk-lem-nagata-sketch-near-closure"]
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
tags = ["sketch"]
+++
Let $S$ be Noetherian, let $U\to S$ be separated and of finite type, and
let $U=U_1\cup U_2$ be an open cover with each $U_i\to S$ compactifiable.
For prepared sides, set

$$
V_{12}=V_1\times_UV_2,\qquad
X_{12}=\SIm(V_{12}\longrightarrow X_1\times_SX_2).
$$

After a further $V_1$-admissible blow-up (the sides remain prepared), the proper projection
$p_1:X_{12}\to X_1$ is an isomorphism near $B_{1,2}$, and

$$
X_{12}\cap(B_{1,2}\times_SB_{2,1})=\varnothing.
$$
