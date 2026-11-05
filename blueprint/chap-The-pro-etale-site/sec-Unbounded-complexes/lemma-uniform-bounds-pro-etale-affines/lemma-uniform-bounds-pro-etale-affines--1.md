+++
id = "lemma-uniform-bounds-pro-etale-affines--1"
kind = "lemma"
title = "Bound on pro-'etale affines"
order = 162002
aliases = ["bp-r047-1"]
lean = []
uses = ["definition-small-pro-etale-site", "definition-classical-pro-etale-sheaves", "definition-cohomological-dimension"]
+++
This bound is bypassed by the Lean proof of the main theorem. The affine
bound used in Lean concerns torsion étale cohomology of affine schemes of
finite type; the assertion below for arbitrary pro-étale affines has no
corresponding declaration in the current mainline.

For every classical sheaf $F$ of $A$-modules on $X_{\mathrm{pro}\acute{e}t}$ and every pro-étale affine $U$ over $X$, one has $H^q(U,F)=0$ for $q>d$.
