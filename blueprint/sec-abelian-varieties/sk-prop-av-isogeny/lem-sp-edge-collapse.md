+++
id = "lem-sp-edge-collapse"
kind = "lemma"
title = "Edge collapse and edge maps"
lean = ["CategoryTheory.ExactCouple.ConvergenceData.edge", "CategoryTheory.ExactCouple.edge_collapse", "CategoryTheory.ExactCouple.isIso_edge"]
order = 498
uses = ["def-sp-convergence", "def-sp-exact-couple"]
+++
Let $(D,E,\alpha,f,g)$ be an exact couple [def-sp-exact-couple] whose
spectral sequence converges [def-sp-convergence] to a filtration of an object
$A$ with a finite, exhaustive, separated filtration, and suppose that for
some $r_0$ all entries $E_{r_0}^{p,q}$, $p\ne0$, vanish. Then every
differential $d_r$ with $r\geq r_0$ vanishes, all pages equal $E_{r_0}$,
$E_\infty=E_{r_0}$, and the edge map

$$
 A^n\longrightarrow E_{r_0}^{0,n}
$$

is an isomorphism in each degree $n$.
