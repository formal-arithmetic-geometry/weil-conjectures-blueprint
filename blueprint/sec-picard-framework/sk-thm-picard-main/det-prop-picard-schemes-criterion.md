+++
id = "det-prop-picard-schemes-criterion"
kind = "proposition"
title = "The general representability criterion"
order = 850
lean = ["AlgebraicGeometry.isRepresentable_of_isSheaf_of_zariskiCovers"]
+++
Let $S$ be a scheme, $G:(\Sch/S)^{\mathrm{op}}\to\mathsf{Set}$ a Zariski sheaf on the category of
$S$-schemes with small values, and
$(F_i)_{i\in I}$, indexed by a set $I$, representable subfunctors, each representable by
open immersions, with $G=\bigcup_iF_i$ in the sense that for every
$T$ and $\xi\in G(T)$ there is an open covering $T=\bigcup_aT_a$ and
indices $i_a$ with $\xi|_{T_a}\in F_{i_a}(T_a)$. Then $G$ is
representable.
