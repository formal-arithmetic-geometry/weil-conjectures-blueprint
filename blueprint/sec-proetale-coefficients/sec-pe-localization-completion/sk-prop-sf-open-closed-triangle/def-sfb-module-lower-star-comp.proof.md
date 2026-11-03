+++
kind  = "proof"
of    = "def-sfb-module-lower-star-comp"
uses = ["lem-sfb-pushforward-comp-monoidal", "det-def-sfb-transport", "det-def-sfb-change-of-scalars", "lem-sfb-eta-comp"]
+++
Let $c\colon g^{\Ab}_*f^{\Ab}_*\Lambda_X\xrightarrow{\sim}(g\circ f)^{\Ab}_*\Lambda_X$
be the composition isomorphism at $\Lambda_X$. Transport commutes with restriction of
scalars, so

$$
g_*\circ f_*
=\operatorname{Res}_{\eta_g}\circ\operatorname{mapMod}(g^{\Ab}_*)\circ
\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)
\cong\operatorname{Res}_{\eta_g}\circ\operatorname{Res}_{g^{\Ab}_*\eta_f}\circ
\operatorname{mapMod}(g^{\Ab}_*)\circ\operatorname{mapMod}(f^{\Ab}_*)
$$

([det-def-sfb-transport]). The composition isomorphism of pushforwards of abelian
sheaves is monoidal ([lem-sfb-pushforward-comp-monoidal]), so it lifts to an
isomorphism
$\operatorname{mapMod}(g^{\Ab}_*)\circ\operatorname{mapMod}(f^{\Ab}_*)\cong
\operatorname{Res}_c\circ\operatorname{mapMod}((g\circ f)^{\Ab}_*)$. Restrictions of
scalars compose ([det-def-sfb-change-of-scalars]), and the composite ring morphism is
$c\circ g^{\Ab}_*\eta_f\circ\eta_g=\eta_{g\circ f}$ by the compatibility of $\eta$
with composition ([lem-sfb-eta-comp]). Hence
$g_*\circ f_*\cong\operatorname{Res}_{\eta_{g\circ f}}\circ
\operatorname{mapMod}((g\circ f)^{\Ab}_*)=(g\circ f)_*$, and on underlying sheaves
this isomorphism is the composition isomorphism.
