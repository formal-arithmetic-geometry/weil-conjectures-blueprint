+++
id = "thm-weil-pbc-hypercover-cohomology"
kind = "theorem"
title = "Cohomology is computed after hypercover refinement"
order = 957
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-finite-split-hypercover", "lem-weil-pbc-hypercover-free-resolution", "lem-weil-pbc-hypercover-refinement"]
+++
For a quasi-compact quasi-separated scheme $X$, an abelian etale sheaf $F$,
and $q\geq0$, there is a natural isomorphism

$$
 \varinjlim_{U}H^q(C^\bullet(U,F))
 \xrightarrow{\sim} H^q(X_{\Et},F).
$$

The limit is over refinements, modulo simplicial homotopy, of the hypercovers
finite in each degree [def-weil-pbc-finite-split-hypercover]. The right side
is the derived cohomology of [def-weil-pbc-etale-cohomology]. A
representative, and a relation between representatives, use only finitely
many degrees. The same assertion holds for sheaves of modules over a fixed
constant ring, with cohomology derived in that module category.
