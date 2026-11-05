+++
id = "lemma-uniform-bounds-pro-etale-affines--2"
kind = "lemma"
title = "Uniform bound after base change"
order = 162003
aliases = ["bp-r047-2"]
lean = []
uses = ["definition-small-pro-etale-site", "definition-classical-pro-etale-sheaves"]
+++
This uniform bound is bypassed by the Lean proof of the main theorem.
The current mainline uses bounds on the étale site, without a declaration
of the following bound over all pro-étale affine base changes.

There is an integer $c$, depending only on $X$, such that for every classical sheaf $F$ of $A$-modules on $X_{\mathrm{pro}\acute{e}t}$ and every pro-étale affine $V$ over $Y$, one has $H^q(X\times_YV,F)=0$ for $q>c$.
