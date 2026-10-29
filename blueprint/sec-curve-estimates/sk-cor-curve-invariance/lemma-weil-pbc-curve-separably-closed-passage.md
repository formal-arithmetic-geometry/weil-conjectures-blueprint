+++
id = "lemma-weil-pbc-curve-separably-closed-passage"
kind = "lemma"
title = "Passage between separably closed fields"
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed_of_isAlgClosed"]
order = 1622
uses = ["lem-pc-homeo-pure-insep", "lem-pc-kbar-pure-insep", "lemma-weil-pbc-universal-homeomorphism-coverings", "lemma-weil-pbc-universal-homeomorphism-site-equivalence"]
+++
Let $k\subseteq k'$ be separably closed fields, let $C$ be proper of
dimension at most one over $k$, and let $F$ be a torsion etale sheaf. If
proper-curve cohomology is invariant for algebraically closed extensions,
then the specified restriction
$H^q(C,F)\to H^q(C_{k'},F|)$ is an isomorphism for every $q$.
