+++
id = "lem-wf-smooth-components-disjoint"
kind = "lemma"
title = "Irreducible components of a smooth variety do not meet"
lean = ["PrimeSpectrum.disjoint_of_mem_irreducibleComponents", "PrimeSpectrum.isClopen_of_mem_irreducibleComponents", "PrimeSpectrum.connectedComponent_eq_of_mem_irreducibleComponents"]
order = 2831
uses = ["lem-sc-regular-local-domain", "lem-wf-affine-noetherian-components"]
+++
Let $X$ be an affine scheme of finite type over a field $k$ whose local
ring at every closed point is regular (for instance a smooth affine
variety). Then any two distinct irreducible components of $X$ are
disjoint. Consequently the (finitely many) irreducible components of $X$
are open and closed, and are its connected components.
