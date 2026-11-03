+++
id = "lem-weil-pbc-constant-module-pushforward-functoriality"
kind = "lemma"
title = "Functoriality of the maps between direct images of constant module sheaves"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-constructible-pullback-constant"]
lean = ["AlgebraicGeometry.Etale.constantModulePushforwardMap", "AlgebraicGeometry.Etale.constantModulePushforwardMap_id_comp"]
order = 1951
+++
Let $\Lambda$ be a commutative ring (in the coefficient universe one above that of the schemes [def-weil-pbc-scheme-conventions]) and $M$ a $\Lambda$-module; write $\underline M_T$ for the constant sheaf of $\Lambda$-modules with value $M$ on $T_{\Et}$ [def-weil-pbc-etale-sheaves]. For morphisms $f_1:Y_1\to X$, $f_2:Y_2\to X$ and $g:Y_2\to Y_1$ with $f_1\circ g=f_2$, let
$$c_g:f_{1*}\underline M_{Y_1}\longrightarrow f_{2*}\underline M_{Y_2}$$
be $f_{1*}$ of the inverse-image unit $\underline M_{Y_1}\to g_*g^{-1}\underline M_{Y_1}$ followed by $g_*$ of the canonical comparison $g^{-1}\underline M_{Y_1}\cong\underline M_{Y_2}$ [lemma-constructible-pullback-constant], composed with the direct-image composition isomorphism $f_{1*}g_*\cong f_{2*}$ [def-weil-pbc-direct-image]. Then $c_{\mathrm{id}_{Y}}=\mathrm{id}$ for every $f:Y\to X$, and for $g:Y_2\to Y_1$, $g':Y_3\to Y_2$ over $X$ (with $f_1\circ g=f_2$, $f_2\circ g'=f_3$) one has $c_{g\circ g'}=c_{g'}\circ c_g:f_{1*}\underline M_{Y_1}\to f_{3*}\underline M_{Y_3}$. No finiteness assumptions are imposed.
