+++
id = "proposition-six-operations-change-coefficients--18"
kind = "proposition"
title = "Transport of units through a mate square"
order = 646036
aliases = ["bp-r197-18"]
lean = ["CategoryTheory.unit_mateEquiv"]
+++
Let $F\dashv G$ and $F'\dashv G'$ be adjunctions, and let $T_1,T_2$ be functors between their source and target categories. Suppose

$$
c_F:T_2F\xrightarrow{\sim}F'T_1,\qquad c_G:T_1G\xrightarrow{\sim}G'T_2
$$

are natural isomorphisms and $c_G$ is the mate of $c_F^{-1}$. If $\eta,\eta'$ are the units, then

$$
G'(c_F(M))\circ c_G(FM)\circ T_1(\eta_M)=\eta'_{T_1M}.
$$

For $F=f^*$ and $G=Rf_*$, with $T_1,T_2$ scalar extension along $\Lambda\to\Lambda'$, the comparisons of Definition [definition-change-of-coefficients-maps](1) and (4) form such a mate square by construction, and on $D^b_{\mathrm{ctf}}$ they are invertible by [proposition-six-operations-change-coefficients--2] and [proposition-six-operations-change-coefficients--3]. Hence, under these comparisons, scalar extension of the unit of $f^*_\Lambda\dashv Rf_{*,\Lambda}$ is the unit of the same adjunction over $\Lambda'$.
