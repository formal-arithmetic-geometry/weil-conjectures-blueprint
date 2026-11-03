+++
id = "lem-weil-pbc-open-cohomology-whole-restriction-naturality"
kind = "lemma"
title = "Restriction from the whole scheme commutes with cohomology pullback"
uses = ["def-pc-scheme", "def-weil-pbc-cohomology-pullback", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.openCohomologyPullback_restrict"]
order = 2006
+++
Let $g:Y\to X$ be a morphism of schemes [def-pc-scheme], $W\subseteq X$ an open subscheme with inclusion $j_W:W\to X$, $j'_W:g^{-1}W\to Y$ the inclusion of its preimage and $g_W:g^{-1}W\to W$ the restriction of $g$, so that $j_W\circ g_W=g\circ j'_W$. Let $G$ be an abelian sheaf on the small etale site of $X$ and $q\ge0$. Write $u^*:H^q(X,G)\to H^q(X',u^{-1}G)$ for the cohomology pullback along a morphism $u:X'\to X$ [def-weil-pbc-cohomology-pullback], and let
$$P_W:H^q(W,j_W^{-1}G)\to H^q(g^{-1}W,j'^{-1}_Wg^{-1}G)$$
be the pullback $g_W^*$ followed by the map induced by the coefficient isomorphism $g_W^{-1}j_W^{-1}G\cong(j_W\circ g_W)^{-1}G=(g\circ j'_W)^{-1}G\cong j'^{-1}_Wg^{-1}G$ given by the composition isomorphisms of inverse images [lem-weil-pbc-inverse-image-composition]. Then for every $x\in H^q(X,G)$
$$j'^*_W\bigl(g^*x\bigr)=P_W\bigl(j_W^*x\bigr)\quad\text{in }H^q(g^{-1}W,j'^{-1}_Wg^{-1}G).$$
