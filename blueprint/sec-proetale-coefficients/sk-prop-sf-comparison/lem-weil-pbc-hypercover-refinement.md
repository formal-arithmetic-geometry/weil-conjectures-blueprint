+++
id = "lem-weil-pbc-hypercover-refinement"
kind = "lemma"
title = "Finite refinements and local lifting"
order = 1019
lean = ["AlgebraicGeometry.FiniteSplitEtaleHypercover.exists_and_cofiltered", "AlgebraicGeometry.FiniteSplitEtaleHypercover.exists_refinement_solving_local_requirements", "AlgebraicGeometry.FiniteSplitEtaleHypercover.exists_truncated_refinement"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-finite-split-hypercover"]
+++
For a quasi-compact quasi-separated $X$, split etale hypercovers finite in
each degree [def-weil-pbc-finite-split-hypercover] exist. Their homotopy
category is cofiltered. A finite collection of local lifting requirements on
their terms in finitely many degrees can be satisfied after refinement,
provided each requirement is locally solvable for the etale topology.
Consequently an arbitrary etale hypercover can, through any specified finite
degree, be refined by one finite in each degree.
