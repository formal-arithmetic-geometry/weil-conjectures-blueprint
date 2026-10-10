+++
id = "sk-prop-picard-schemes-criterion"
kind = "proposition"
title = "The general representability criterion"
order = 775
uses = ["sk-def-av-jacobian"]
lean = ["AlgebraicGeometry.Scheme.LocalRepresentability.isRepresentable"]
tags = ["sketch"]
+++
Let $G:\Sch^{\mathrm{op}}\to\mathsf{Set}$ be a Zariski sheaf on the category of schemes and
$(F_i)_{i\in I}$, indexed by a set $I$, representable subfunctors, each representable by
open immersions, with $G=\bigcup_iF_i$ in the sense that for every
$T$ and $\xi\in G(T)$ there is an open covering $T=\bigcup_aT_a$ and
indices $i_a$ with $\xi|_{T_a}\in F_{i_a}(T_a)$. Then $G$ is
representable.
