+++
id = "proposition-six-operations-change-coefficients--20"
kind = "proposition"
title = "Transport of the unit for $Rf_{!,\\Lambda}\\dashv f^!_\\Lambda$"
order = 646040
aliases = ["bp-r197-20"]
lean = ["CategoryTheory.NatTrans.SquareCompatible.unit"]
+++
Suppose the compact-support and exceptional-image comparisons for a coefficient change are natural isomorphisms $c_!:T_YRf_!\simeq Rf'_!T_X$ and $c^!:T_Xf^!\simeq f'^!T_Y$, and $c^!$ is the mate of $c_!^{-1}$. Then

$$
f'^!(c_!(K))\circ c^!(Rf_!K)\circ T_X(\eta_K)=\eta'_{T_XK},
$$

where $\eta,\eta'$ are the units of $Rf_!\dashv f^!$ in the two coefficient categories.

The compactly supported comparison of Definition [definition-change-of-coefficients-maps](5) and the exceptional comparison $\beta$ satisfy these hypotheses on $D^b_{\mathrm{ctf}}$: $\beta$ is by definition the mate of the inverse of the former, and both are invertible by [proposition-six-operations-change-coefficients--4] and [proposition-six-operations-change-coefficients--5]. Hence scalar extension of the unit of $Rf_{!,\Lambda}\dashv f^!_\Lambda$ is the unit of the same adjunction over $\Lambda'$.
