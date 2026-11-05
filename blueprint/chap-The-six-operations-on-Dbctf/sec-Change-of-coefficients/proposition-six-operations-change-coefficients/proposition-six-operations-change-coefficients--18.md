+++
id = "proposition-six-operations-change-coefficients--18"
kind = "proposition"
title = "Transport of units through a mate square"
order = 645036
aliases = ["bp-r197-18"]
lean = ["CategoryTheory.NatTrans.SquareCompatible.unit"]
uses = []
+++
Let $F\dashv G$ and $F'\dashv G'$ be adjunctions, and let $T_1,T_2$ be functors between their source and target categories. Suppose
$$
c_F:T_2F\xrightarrow{\sim}F'T_1,\qquad c_G:T_1G\xrightarrow{\sim}G'T_2
$$
are natural isomorphisms and $c_G$ is the mate of $c_F^{-1}$. If $\eta,\eta'$ are the units, then
$$
G'(c_F(M))\circ c_G(FM)\circ T_1(\eta_M)=\eta'_{T_1M}.
$$

For $F=f^*$ and $G=Rf_*$, this transports the unit whenever the coefficient comparisons are invertible and form this mate square.
