+++
id = "finite-hypercovers-and-descent-at-an-inverse-limit"
kind = "section"
title = "Finite hypercovers and descent at an inverse limit"
order = 1218
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
+++
Cohomology computed by hypercovers that are finite in each degree
[def-weil-pbc-finite-split-hypercover], which exist and form a cofiltered
homotopy category [lem-weil-pbc-hypercover-refinement]; the augmented free
complex of such a hypercover is exact
[lem-weil-pbc-hypercover-free-resolution], so the colimit over refinements
computes etale cohomology [thm-weil-pbc-hypercover-cohomology]. Finiteness in
each degree is what makes the data descend along an affine inverse limit
[lem-weil-pbc-etale-finite-data-descent],
[lem-weil-pbc-finite-hypercover-descent], and that descent is what gives
continuity of sections [lem-weil-pbc-etale-section-continuity] and, in the
next sections, continuity of cohomology.
