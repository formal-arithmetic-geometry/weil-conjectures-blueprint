+++
id = "lem-weil-pbc-underived-exchange-sectionwise"
kind = "lemma"
title = "The underived exchange map on pulled-back sections"
order = 1402
lean = ["AlgebraicGeometry.Etale.baseChangeMap_app_pullSection", "AlgebraicGeometry.Etale.baseChangeSectionMap"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-underived-exchange"]
+++
Let $\square$ be a commutative square of schemes as in
[def-weil-pbc-underived-exchange] (for instance a cartesian square
[def-weil-pbc-cartesian-square]) and let $F\in\Ab(X_{\Et})$. Let $W\to Y$
and $V\to Y'$ be etale, let $\phi:V\to W$ be a morphism with
$(W\to Y)\circ\phi=g\circ(V\to Y')$, and let
$s\in(f_*F)(W)=F(X\times_YW)$ [def-weil-pbc-direct-image]. Write
$\phi^*s\in(g^{-1}f_*F)(V)$ for the pullback of $s$ along $\phi$: the image
of $s$ under the unit $(f_*F)(W)\to(g_*g^{-1}f_*F)(W)=(g^{-1}f_*F)(W\times_YY')$
of $g^{-1}\dashv g_*$ [def-weil-pbc-inverse-image], restricted along the
morphism $V\to W\times_YY'$ with components $\phi$ and $V\to Y'$ (it is the
section represented by $W$, $V\to W\times_YY'$ and $s$). Let
$\beta:X'\times_{Y'}V\to X\times_YW$ be the morphism with components
$X'\times_{Y'}V\to V\xrightarrow{\phi}W$ and
$X'\times_{Y'}V\to X'\xrightarrow{g'}X$. Then the underived exchange
morphism $\Ex^0_{\square,F}$ of [def-weil-pbc-underived-exchange] sends
$\phi^*s$ to the pullback $\beta^*s$ of $s$ along $\beta$ (a morphism over
$g'$), as a section of $g'^{-1}F$ over $X'\times_{Y'}V$, i.e. of
$f'_*g'^{-1}F$ over $V$.
