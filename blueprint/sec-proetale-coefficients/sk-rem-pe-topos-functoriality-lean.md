+++
id = "sk-rem-pe-topos-functoriality-lean"
kind = "remark"
title = "Coefficients in the formalization"
order = 925
uses = ["sk-def-sfb-finite-pushforward-pullback"]
tags = ["sketch"]
+++
The Lean formalization treats only the case of Grothendieck abelian
coefficients. For a Grothendieck abelian category $\mathcal A$ (with
morphism groups in the universe one above that of the schemes) it
constructs the adjunction $f^*\dashv f_*$ between
$\Sh(Y_{\mathrm{proét}},\mathcal A)$ and $\Sh(X_{\mathrm{proét}},\mathcal A)$, with
$f^*$ exact and compatible with composition, and with $f^*\dashv f_*$
monoidal when $\mathcal A$ is closed symmetric monoidal
([prop-pe-topos-functoriality-abelian]). The geometric
morphism on sheaves of sets is not formalized. This suffices for
everything below, where $f^{-1}$ is only applied to abelian sheaves and
sheaves of modules, and the coefficient sheaves are pulled back as
monoid objects of abelian sheaves.
