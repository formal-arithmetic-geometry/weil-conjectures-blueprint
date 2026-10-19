+++
id = "prop-weil-pbc-reduction-to-projective-line"
kind = "theorem"
title = "Reduction of proper base change to $\\mathbf P^1$"
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper_of_isAddTorsion"]
order = 1271
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-projective-embedding", "lem-weil-pbc-reduction-projective-space", "lemma-weil-pbc-cancellation", "lemma-weil-pbc-chow-factorization", "lemma-weil-pbc-composition", "lemma-weil-pbc-property-iff-acyclicity", "lemma-weil-pbc-symmetric-product-p1", "lemma-weil-pbc-target-locality", "prop-weil-pbc-composition-stability", "prop-weil-pbc-finite-morphism"]
+++
Assume that $\mathbf P^1_S\to S$ satisfies $\mathrm{PBC}$ in the sense of
[def-weil-pbc-property] for every scheme $S$. Then every proper morphism of
schemes satisfies $\mathrm{PBC}$. No finite-presentation hypothesis is
needed, because the Chow factorization [lemma-weil-pbc-chow-factorization]
holds for every proper morphism over an affine base.
