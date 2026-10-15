+++
id = "det-pe-topos-functoriality-inverse-image"
kind = "lemma"
title = "The geometric morphism attached to a morphism of schemes"
uses = ["det-pe-topos-functoriality-site", "def-sfb-finite-lower-star", "def-sfb-finite-lower-star-comp"]
+++
Let $f\colon X\to Y$ be a morphism of schemes and let
$u\colon Y_{\mathrm{proét}}\to X_{\mathrm{proét}}$ be base change, $u(V)=V\times_YX$.

1. $u$ preserves finite limits (it sends $Y$ to $X$ and fibre products to fibre products)
   and sends coverings to coverings.
2. $f_*G:=G\circ u$ defines a functor
   $f_*\colon\Sh(X_{\mathrm{proét}})\to\Sh(Y_{\mathrm{proét}})$, and
   $f^{-1}F:=\bigl(\operatorname{Lan}_{u^{\mathrm{op}}}F\bigr)^{\#}$ (left Kan extension
   followed by sheafification) is left adjoint to it.
3. $f^{-1}$ preserves all colimits and finite limits, so
   $(f^{-1},f_*)$ is a geometric morphism $f_{\mathrm{proét}}$.
4. On abelian sheaves, $f^{-1}$ (computed on underlying sheaves of sets) is exact.
5. For $g\colon Y\to Z$ there are canonical isomorphisms $(g\circ f)_*\cong g_*\circ f_*$
   and $(g\circ f)^{-1}\cong f^{-1}\circ g^{-1}$, so
   $(g\circ f)_{\mathrm{proét}}\cong g_{\mathrm{proét}}\circ f_{\mathrm{proét}}$.
