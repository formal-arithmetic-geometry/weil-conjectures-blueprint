+++
id = "proposition-six-operations-change-coefficients--19"
kind = "proposition"
title = "Transport of counits through a mate square"
order = 645038
aliases = ["bp-r197-19"]
lean = ["CategoryTheory.NatTrans.SquareCompatible.counit"]
uses = []
+++
Let $F\dashv G$ and $F'\dashv G'$ be adjunctions, and suppose that the comparison isomorphisms $c_F:T_2F\simeq F'T_1$ and $c_G:T_1G\simeq G'T_2$ form a mate square, with $c_G$ the mate of $c_F^{-1}$. If $\varepsilon,\varepsilon'$ are the counits, then
$$
\varepsilon'_{T_2N}\circ F'(c_G(N))\circ c_F(GN)=T_2(\varepsilon_N).
$$

For $F=f^*$ and $G=Rf_*$, this is compatibility of the counit with coefficient change whenever these comparison isomorphisms form a mate square.
