+++
id = "det-thm-sfb-proper-base-change-rational"
kind = "lemma"
title = "Proper direct image, base change and projection formula for $E$ and $\\overline{\\mathbf Q}_\\ell$"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_rationalizationPushHom_boundedBelow"]
order = 2392
uses = ["det-thm-sfb-proper-base-change-integral", "sk-cor-pe-bounded-continuity", "det-lem-integral-models-generators", "det-cor-coefficient-heart-ii-triangulated", "det-prop-sfb-cartesian-coefficients-finite-free"]
+++
Let $\Lambda=E$ or $\Qlb$ and $p\colon X\to Y$ proper between standing schemes.

1. For $K\in D(X_{\mathrm{proét}},\cO_E)$ bounded below,
   $Rp_*(K[1/\ell])\simeq(Rp_*K)[1/\ell]$; for $K\in D(X_{\mathrm{proét}},E)$ bounded below and
   $F/E$ finite, $Rp_*(K_F)\simeq(Rp_*K)_F$ and $Rp_*(K_{\Qlb})\simeq(Rp_*K)_{\Qlb}$, via the
   canonical maps.
2. $Rp_*$ maps $\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$.
3. The proper base change and projection formula maps are isomorphisms on $\Dbc(-,\Lambda)$.
