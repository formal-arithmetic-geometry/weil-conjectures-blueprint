+++
kind  = "proof"
of    = "lem-weil-pbc-underived-exchange-sectionwise"
uses  = ["def-weil-pbc-underived-exchange", "def-weil-pbc-inverse-image", "def-weil-pbc-direct-image"]
+++
By definition $\phi^*s$ is the restriction, along $V\to W\times_YY'$, of the
image $\eta_g(s)$ of $s$ under the unit $\eta_g:f_*F\to g_*g^{-1}f_*F$ at
$W$. Since $\Ex^0_{\square,F}$ is a morphism of sheaves, it commutes with this
restriction, so it suffices to compute $g_*(\Ex^0_{\square,F})(\eta_g(s))$,
a section of $f'_*g'^{-1}F$ over $W\times_YY'$, and then restrict it to $V$.

By [def-weil-pbc-underived-exchange], $\Ex^0_{\square,F}$ is the mate of the
square isomorphism $\theta_\square$; taking the mate once more along the
adjunctions $g^{-1}\dashv g_*$ and $g'^{-1}\dashv g'_*$ [def-weil-pbc-inverse-image]
gives the unit form
$$
 g_*(\Ex^0_{\square,F})\circ\eta_{g,f_*F}=c\circ f_*(\eta_{g',F}),
$$
where $c:f_*g'_*\xrightarrow{\sim}g_*f'_*$ is the composition isomorphism of
the direct images along $fg'=gf'$ [def-weil-pbc-direct-image]. Evaluated at
$W$, the right side sends $s\in F(X\times_YW)$ to $\eta_{g'}(s)$, a section of
$g'^{-1}F$ over $(X\times_YW)\times_XX'$, transported along the canonical
isomorphism of this scheme with $(W\times_YY')\times_{Y'}X'$. Restricting
along $V\to W\times_YY'$, i.e. along $X'\times_{Y'}V\to(W\times_YY')\times_{Y'}X'$,
the composite of these restrictions and of the unit of $g'^{-1}\dashv g'_*$
is the pullback of $s$ along the morphism $X'\times_{Y'}V\to X\times_YW$ whose
components are the projection to $V$ followed by $\phi$ and the projection to
$X'$ followed by $g'$, which is $\beta$. Hence
$\Ex^0_{\square,F}(\phi^*s)=\beta^*s$.
