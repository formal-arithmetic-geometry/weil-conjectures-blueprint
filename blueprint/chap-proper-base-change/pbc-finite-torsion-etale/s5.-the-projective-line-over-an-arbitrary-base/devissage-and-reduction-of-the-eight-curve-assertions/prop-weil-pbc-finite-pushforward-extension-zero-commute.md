+++
id = "prop-weil-pbc-finite-pushforward-extension-zero-commute"
kind = "theorem"
title = "Finite pushforward commutes with extension by zero"
order = 1719
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-finite-pushforward-extension-zero", "lem-weil-pbc-finite-stalk-formula", "lem-weil-pbc-geometric-stalk-conservative"]
tags = ["latex:proposition"]
+++
The morphism $\beta_{\bar v,j_V,G}$ of
[def-weil-pbc-finite-pushforward-extension-zero] is an isomorphism. It is
natural in $G$, compatible with identity and composite finite maps, and stable
under extension of the ground field.

## Proof

At a geometric point $\bar y\to Y$, the stalk of the left side is
$(v_*G)_{\bar y}$ if $\bar y\in V$ and $0$ otherwise; the stalk of the right
side is the sum over the geometric points of the finite fibre $X_{\bar y}$ of
the stalks of the extension by zero [def-weil-pbc-extension-by-zero], namely
$G_{\bar x}$ for $\bar x\in U_{\bar y}$ and $0$ otherwise, and $U_{\bar
y}=X_{\bar y}$ precisely when $\bar y\in V$. By
[lem-weil-pbc-finite-stalk-formula] both sides are the same finite direct sum,
and the map of [def-weil-pbc-finite-pushforward-extension-zero] is the
identity on each summand; conservativity of geometric stalks gives the
isomorphism. The remaining compatibilities are built into the construction.
