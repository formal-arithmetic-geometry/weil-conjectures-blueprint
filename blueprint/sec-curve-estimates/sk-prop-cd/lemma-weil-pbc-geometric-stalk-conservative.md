+++
id = "lemma-weil-pbc-geometric-stalk-conservative"
kind = "lemma"
title = "Conservativity of geometric stalks"
order = 999
lean = ["AlgebraicGeometry.Scheme.isIso_of_isIso_sheafFiber_map"]
uses = ["def-kun-separably-closed", "def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "lemma-openclosed-point-ulift", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $S$ be a scheme and let $\mathcal A$ be a category with all (small)
colimits which is concrete over sets, with a forgetful functor that reflects
isomorphisms, preserves filtered colimits and is compatible with the sheaf
condition on $S_{\Et}$ (for instance etale sheaves of abelian groups or of
$\Lambda$-modules). For each point $s\in S$ let $\bar s$ be the geometric point
at an algebraic closure of $\kappa(s)$. A morphism $\varphi:F\to G$ of
$\mathcal A$-valued etale sheaves on $S$ is an isomorphism if the induced map
of geometric stalks [def-weil-pbc-geometric-stalks]
$\varphi_{\bar s}:F_{\bar s}\to G_{\bar s}$ is an isomorphism for every
$s\in S$.
