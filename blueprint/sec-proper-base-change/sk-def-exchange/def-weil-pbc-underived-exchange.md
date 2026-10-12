+++
id = "def-weil-pbc-underived-exchange"
kind = "definition"
title = "Underived exchange map: corrected categorical construction"
order = 1036
lean = ["AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.upperStar_map_baseChangeMap_app_counit"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image"]
+++
Let $\mathcal A$ be a Grothendieck abelian category for which $\mathcal A$-valued
sheaves on small étale sites admit sheafification, and consider a commutative
square of schemes, $f\circ g'=g\circ f'$ (for instance a cartesian square
[def-weil-pbc-cartesian-square])

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
f'\downarrow & & \downarrow f\\
Y' & \xrightarrow{g} & Y
\end{array}
$$

The composition isomorphisms of inverse images identify both $f'^{-1}g^{-1}$
and $g'^{-1}f^{-1}$ with the inverse image along $f\circ g'=g\circ f'$; this
gives the *square isomorphism*

$$
 \theta_\square:f'^{-1}g^{-1}\xrightarrow{\ \sim\ }g'^{-1}f^{-1}
$$

of functors from $\mathcal A$-valued sheaves on $Y_{\Et}$ to $\mathcal A$-valued
sheaves on $X'_{\Et}$. The *underived exchange morphism* is the natural
transformation

$$
 \Ex^0_{\square}:g^{-1}f_*\longrightarrow f'_*g'^{-1}
$$

of functors from $\mathcal A$-valued sheaves on $X_{\Et}$ to $\mathcal A$-valued
sheaves on $Y'_{\Et}$ obtained as the mate of $\theta_\square$ with respect to
the adjunctions $f^{-1}\dashv f_*$ and $f'^{-1}\dashv f'_*$
[def-weil-pbc-inverse-image], [def-weil-pbc-direct-image]. Concretely, for a
sheaf $F$ on $X_{\Et}$, $\Ex^0_{\square,F}$ is the adjoint, under
$f'^{-1}\dashv f'_*$, of the composite

$$
 f'^{-1}g^{-1}f_*F\xrightarrow{\theta_\square}
 g'^{-1}f^{-1}f_*F\xrightarrow{g'^{-1}\varepsilon_f}g'^{-1}F,
$$

where $\varepsilon_f$ is the counit of $f^{-1}\dashv f_*$; that is,
$\varepsilon_{f'}\circ f'^{-1}\Ex^0_{\square,F}=g'^{-1}\varepsilon_f\circ
\theta_\square$.

On sections, for a cartesian square and a sheaf of abelian groups $F$: for an
etale $V\to Y'$, a representative of a section of $g^{-1}f_*F$ on $V$ consists
of an etale $W\to Y$, a map $V\to W\times_YY'$, and a section of $F$ on
$X\times_YW$; its image under $\Ex^0_{\square,F}$ is the restriction of that
section along

$$
 X'\times_{Y'}V\longrightarrow X\times_YW,
$$

followed by sheafification.
