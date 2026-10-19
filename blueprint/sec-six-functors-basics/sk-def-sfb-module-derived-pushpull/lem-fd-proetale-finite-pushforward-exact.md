+++
id = "lem-fd-proetale-finite-pushforward-exact"
kind = "lemma"
title = "Exactness of finite pushforward on the pro-étale site"
order = 1702
lean = ["AlgebraicGeometry.ProEtale.preservesFiniteColimits_lowerStar_of_isFinite"]
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-module-objects", "sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-module-derived-pushpull"]
+++
Let $f\colon X\to Y$ be a finite morphism of finite presentation.

1. For every ring $R$, the pushforward
   $f_*\colon\Sh(X_{\mathrm{proét}},\Mod_R)\to\Sh(Y_{\mathrm{proét}},\Mod_R)$
   ([sk-def-sfb-finite-pushforward-pullback]) is exact.
2. For every commutative condensed ring $\Lambda$, the pushforward of module objects
   $f_*\colon\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y}$
   ([sk-def-sfb-module-pushforward-pullback]) is exact. Consequently
   $Rf_*K\simeq f_*K$, computed term by term, for every
   $K\in D(\Mod_{\Lambda_X})$ ([sk-def-sfb-module-derived-pushpull]), and
   $R^qf_*M=0$ for every $M\in\Mod_{\Lambda_X}$ and $q>0$.
