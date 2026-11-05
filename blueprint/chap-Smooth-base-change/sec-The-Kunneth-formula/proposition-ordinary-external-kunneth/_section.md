+++
id = "proposition-ordinary-external-kunneth"
kind = "proposition"
title = "Ordinary external Künneth"
order = 719
lean = ["AlgebraicGeometry.Etale.isIso_kunnethMap_of_isSepClosed", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_prodLowerStarExternalProduct"]
uses = ["definition-kunneth-map"]
+++
Let $f_i:X_i\to Y_i$, $i=1,2$, be morphisms of separated $k$-schemes of finite
type, and let $M_i\in D^b_{\mathrm{ctf}}(X_i,A)$. Then the Künneth map
(8.3)

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow R(f_1\times f_2)_*(M_1\boxtimes M_2)
$$

is an isomorphism.
