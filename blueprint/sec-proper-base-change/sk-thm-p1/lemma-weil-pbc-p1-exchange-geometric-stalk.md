+++
id = "lemma-weil-pbc-p1-exchange-geometric-stalk"
kind = "lemma"
title = "Exchange on a geometric stalk"
lean = ["AlgebraicGeometry.Etale.exists_addEquiv_sheafFiber_baseChangeHomologyMap_projectiveLine"]
order = 1717
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-etale-sheaves", "prop-weil-pbc-p1-strict-henselian-comparison", "prop-weil-pbc-strict-henselization-stalk-formula", "prop-weil-pbc-strict-local-exchange"]
+++
Let $p:\mathbf P^1_S\to S$, let $g:T\to S$, and let $\bar t\to T$ have image
$\bar s\to S$, where $\kappa(\bar s)$ and $\kappa(\bar t)$ are separably
closed and algebraic over the residue fields of the image points. For a
torsion sheaf $F$ of $\Lambda$-modules on $\mathbf P^1_S$ ($\Lambda$ a commutative ring) and every $q$, the stalk of the
exchange morphism [def-weil-pbc-derived-exchange] is the canonical restriction

$$
 H^q(\mathbf P^1_{\kappa(\bar s)},F|)
 \longrightarrow
 H^q(\mathbf P^1_{\kappa(\bar t)},F|),
$$

up to the identifications of both stalks with these cohomology groups.
