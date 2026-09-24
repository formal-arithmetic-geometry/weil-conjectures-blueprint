+++
id = "exceptional-inverse-images-what-must-be-proved-before-restriction"
kind = "section"
title = "Exceptional inverse images: what must be proved before restriction"
order = 3305
uses = ["def-weil-constructible-intervals", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-extension-by-zero", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed", "lem-fet-locally-trivial", "lem-weil-extension-by-zero-adjunction", "lem-weil-extension-by-zero-exact"]
+++
All derived categories in this section are ordinary categories of complexes
localized at quasi-isomorphisms. The adjunction has direction
$Rf_!\dashv Rf^{\times}$. We first work in the ambient categories;
writing down a right adjoint does not assert that its values are
constructible. The results below do not assume exceptional-adjoint
admissibility.

The site is part of every category notation below. On either specified
site, Tor amplitude $[a,b]$ means that
$\mathcal H^q(K\otimes_A^L M)=0$ for $q\notin[a,b]$ and
every module sheaf $M$ on that same site, placed in degree zero.
Thus an etale Tor bound tests all etale module sheaves, whereas a
pro-etale Tor bound tests all pro-etale module sheaves. The pullback
of a bounded flat representative is the reason that our comparison
arguments pass from the first test to the second.
