+++
id = "lem-kun-stalks-commute-colimits"
kind = "lemma"
title = "Geometric stalks commute with colimits"
order = 1633
lean = ["AlgebraicGeometry.Scheme.geometricStalk_preservesColimits"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $T$ be a scheme and $\bar t$ a geometric point of $T$. The
stalk functor $F\mapsto F_{\bar t}$ of
[def-weil-pbc-geometric-stalks] commutes with arbitrary colimits
of abelian sheaves on $T_{\Et}$; consequently, in each degree, it commutes with
colimits of complexes of abelian sheaves, computed termwise.
