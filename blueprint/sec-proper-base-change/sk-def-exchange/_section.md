+++
id = "sk-def-exchange"
kind = "definition"
title = "Exchange morphism"
order = 1043
lean = ["AlgebraicGeometry.Etale.baseChange"]
uses = ["sk-def-conv"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category carrying a closed symmetric
monoidal structure, additive in each variable, with functorial flat
resolutions. For a commutative square of schemes

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
f'\downarrow & & \downarrow f\\
Y' & \xrightarrow{g} & Y
\end{array}
$$

(i.e. $f\circ g'=g\circ f'$; for instance $X'=X\times_YY'$) there is an
*exchange morphism*, natural in $F\in\Dplus(X_{\Et},\mathcal A)$,

$$
\Ex_{\square,F}\ :\ g^{-1}Rf_*F\ \longrightarrow\ Rf'_*g'^{-1}F,
$$

namely the adjoint, under $f'^{-1}\dashv Rf'_*$, of the composite

$$
f'^{-1}g^{-1}Rf_*F\ \cong\ g'^{-1}f^{-1}Rf_*F
\xrightarrow{\ g'^{-1}\varepsilon_f\ }g'^{-1}F,
$$

where the isomorphism is induced by $f\circ g'=g\circ f'$ and
$\varepsilon_f$ is the counit of $f^{-1}\dashv Rf_*$. That is,
$\Ex_{\square,F}$ is the unit of $f'^{-1}\dashv Rf'_*$ at $g^{-1}Rf_*F$,
followed by $Rf'_*$ of this composite. Here all functors are taken on the
bounded below derived categories of $\mathcal A$-valued étale sheaves, and
the adjunctions are the derived adjunctions.
