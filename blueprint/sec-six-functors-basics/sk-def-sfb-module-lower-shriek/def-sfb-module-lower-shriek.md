+++
id = "def-sfb-module-lower-shriek"
kind = "definition"
title = "Lower shriek of module objects"
order = 2522
uses = ["def-sfb-module-compactification-lower-shriek", "sk-def-sfb-finite-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes admitting a compactification. The *lower shriek*
$f_!\colon\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y}$ is the functor $f^c_!=g_*\circ i_!$ of
[def-sfb-module-compactification-lower-shriek] for a chosen compactification
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ of $f$. Its underlying sheaf functor is
the lower shriek of abelian sheaves $g^{\Ab}_*\circ i^{\Ab}_!$ for the same
compactification ([sk-def-sfb-finite-lower-shriek]), and $f_!$ is additive and left
exact.
