+++
id = "proposition-ordinary-external-kunneth--1"
kind = "proposition"
title = "Ordinary external Künneth for proper morphisms"
name_showing = false
order = 719001
aliases = ["bp-r217-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_prodLowerStarExternalProduct"]
uses = ["definition-constructible-sheaves", "definition-kunneth-map"]
+++
The mainline proof bypasses the general finite-coefficient statement at
this step and uses the following proper, $\Qbarl$-coefficient version.

Let $k$ be a field of characteristic $p>0$, let $\ell$ be a prime different
from $p$, and let $f_i:X_i\to Y_i$, $i=1,2$, be proper morphisms of separated
$k$-schemes of finite type. For $M_i\in\Dbc(X_i,\Qbarl)$, the Künneth map

$$
Rf_{1*}M_1\boxtimes Rf_{2*}M_2
\longrightarrow R(f_1\times f_2)_*(M_1\boxtimes M_2)
$$

is an isomorphism. Here the complexes are on the pro-étale sites with
coefficients in the condensed ring $\Qbarl$, and the map is defined by
the same adjunction and counits as in [definition-kunneth-map].
