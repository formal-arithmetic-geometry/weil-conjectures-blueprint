+++
id = "thm-sp-grothendieck"
kind = "theorem"
title = "Grothendieck spectral sequence"
order = 524
uses = ["def-sp-composite-acyclicity", "def-sp-convergence", "def-sp-double-complex-total", "def-sp-exact-couple", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "lem-sp-edge-collapse", "thm-sp-double-complex-spectral-sequences", "thm-sp-if-e1"]
+++
Let $(F,G)$ be a composable pair [def-sp-composite-acyclicity] with $F$
sending injectives to $G$-acyclics. For every $X\in\mathcal A$ there is a
functorial first-quadrant spectral sequence whose $E_2$-page is

$$
 E_2^{p,q}=R^pG\bigl(R^qF(X)\bigr)
$$

and which converges to $R^{p+q}(G\circ F)(X)$; its edge maps in degree $n$
have directions $R^nG(F(X))\to R^n(G\circ F)(X)\to G(R^nF(X))$, and the
spectral sequence depends functorially on $X$.
