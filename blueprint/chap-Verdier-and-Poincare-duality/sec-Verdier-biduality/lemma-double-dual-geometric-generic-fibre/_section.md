+++
id = "lemma-double-dual-geometric-generic-fibre"
kind = "lemma"
title = "Double duals on the geometric generic fibre"
order = 841
lean = ["AlgebraicGeometry.Etale.exists_iso_leftDerivedUpperStar_dualizingComplex_of_generic", "AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff_of_generic"]
uses = ["definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
In the setting of Lemma [lemma-restriction-geometric-generic-fibre],
let $B=\mathbf A^1_k$ and $K\in D^b_{\mathrm{ctf}}(X,A)$. For every affine open $V$
of $X$ there is an isomorphism
$g_V^*\omega_V\simeq\omega_{V_{\bar\eta}}(1)[2]$, and the
isomorphism
$g_V^*\mathbb D_V\mathbb D_V(K|_V)\simeq\mathbb D_{V_{\bar\eta}}
\mathbb D_{V_{\bar\eta}}g_V^*(K|_V)$ obtained from it and from the
comparison for internal Hom (applied twice) carries
$g_V^*\delta_{K|_V}$ to $\delta_{g_V^*(K|_V)}$.
