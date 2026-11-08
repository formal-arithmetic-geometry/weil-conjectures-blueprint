+++
id = "proposition-six-operations-change-coefficients--19"
kind = "proposition"
title = "Transport of counits through a mate square"
order = 646038
aliases = ["bp-r197-19"]
lean = ["CategoryTheory.mateEquiv_counit"]
+++
Let $F\dashv G$ and $F'\dashv G'$ be adjunctions, and suppose that the comparison isomorphisms $c_F:T_2F\simeq F'T_1$ and $c_G:T_1G\simeq G'T_2$ form a mate square, with $c_G$ the mate of $c_F^{-1}$. If $\varepsilon,\varepsilon'$ are the counits, then

$$
\varepsilon'_{T_2N}\circ F'(c_G(N))\circ c_F(GN)=T_2(\varepsilon_N).
$$

For $F=f^*$ and $G=Rf_*$, with $T_1,T_2$ scalar extension along $\Lambda\to\Lambda'$, the comparisons of Definition [definition-change-of-coefficients-maps](1) and (4) form such a mate square by construction, and on $D^b_{\mathrm{ctf}}$ they are invertible by [proposition-six-operations-change-coefficients--2] and [proposition-six-operations-change-coefficients--3]. Hence, under these comparisons, scalar extension of the counit of $f^*_\Lambda\dashv Rf_{*,\Lambda}$ is the counit of the same adjunction over $\Lambda'$.
