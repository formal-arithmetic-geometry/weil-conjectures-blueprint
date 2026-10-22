+++
id = "lem-sp-grothendieck-edge-maps"
kind = "lemma"
title = "Edge maps of the Grothendieck spectral sequence"
lean = ["CategoryTheory.Functor.grothendieckBottomEdge", "CategoryTheory.Functor.grothendieckLeftEdge", "CategoryTheory.Functor.grothendieckBottomEdgeMap", "CategoryTheory.Functor.grothendieckLeftEdgeMap"]
order = 609
uses = ["def-sp-composite-acyclicity", "def-sp-convergence", "thm-sp-grothendieck"]
+++
Let $(F,G)$ be a composable pair [def-sp-composite-acyclicity] with $F$
sending injectives to $G$-acyclics, and let $X\in\mathcal A$. The *bottom
edge map* of the Grothendieck spectral sequence of $X$ is

$$
 R^nG(F(X))\longrightarrow R^n(G\circ F)(X),
$$

and the *left edge map* is

$$
 R^n(G\circ F)(X)\longrightarrow G(R^nF(X));
$$

both are functorial in $X$. In the sheaf setting $F=f_*$, $G=h_*$ of the
proper-base-change chapter they are respectively $R^nh_*f_*\mathcal F\to
R^n(hf)_*\mathcal F$ and $R^n(hf)_*\mathcal F\to h_*R^nf_*\mathcal F$.
