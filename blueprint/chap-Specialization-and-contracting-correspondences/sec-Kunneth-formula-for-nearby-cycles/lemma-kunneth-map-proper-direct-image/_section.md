+++
id = "lemma-kunneth-map-proper-direct-image"
kind = "lemma"
title = "The Künneth map and proper direct image"
order = 1645
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.kunnethMap_comp_pushforwardExchange"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "definition-pro-etale-base-change-map"]
+++
Let $f:X\to X_1$ and $g:Y\to Y_1$ be proper morphisms of separated
$S$-schemes of finite type, and let $L\in D^b_{\mathrm{ctf}}(X_\eta,A)$
and $M\in D^b_{\mathrm{ctf}}(Y_\eta,A)$. Identify direct images of
external products by the ordinary Künneth formula, and direct images
of nearby cycles by the base change isomorphism for proper maps. Then
$R(f_s\times g_s)_*\Pi_{L,M}$ becomes
$\Pi_{Rf_{\eta*}L,Rg_{\eta*}M}$.
