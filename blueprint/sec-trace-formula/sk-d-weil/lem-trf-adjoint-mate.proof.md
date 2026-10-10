+++
kind  = "proof"
of    = "lem-trf-adjoint-mate"
+++
In the framework of [rem-trf-classical-framework], for every
$x\in\mathcal C_1$, $y\in\mathcal C_2$, the adjunctions give
natural bijections

$$
\begin{aligned}
\operatorname{Hom}(x,G_1y)
&\simeq\operatorname{Hom}(F_1x,y)\\
&\xrightarrow{\ h\mapsto h\circ\alpha_x^{-1}\ }
\operatorname{Hom}(F_2x,y)
\simeq\operatorname{Hom}(x,G_2y).
\end{aligned}
$$

Yoneda gives a unique natural isomorphism $\beta:G_1\to G_2$.
Applying the bijection to $x=G_1y$ and
$\operatorname{id}_{G_1y}$ gives exactly the formula for $\beta_y$
in (1). Replacing $\alpha^{-1}$ with $\alpha$ in the reversed
bijection gives the displayed formula for $\beta^{-1}$; these maps
are inverse because the two Hom-bijections are inverse.

The unit $\eta_{1,x}$ corresponds to
$\operatorname{id}_{F_1x}$. The displayed bijection sends it to the
adjoint of $\alpha_x^{-1}:F_2x\to F_1x$, namely
$G_2(\alpha_x^{-1})\eta_{2,x}$.
Consequently $\beta_{F_1x}\eta_{1,x} =G_2(\alpha_x^{-1})\eta_{2,x}$, which proves the unit formula.
The counit corresponds to the identity of $G_1y$. Hence
$\beta_y$ is adjoint to
$\varepsilon_{1,y}\alpha_{G_1y}^{-1}$, giving

$$
\varepsilon_{2,y}F_2(\beta_y)
=\varepsilon_{1,y}\alpha_{G_1y}^{-1}.
$$

Precompose with $\alpha_{G_1y}$ and use naturality of $\alpha$ to
obtain
$\varepsilon_{2,y}\alpha_{G_2y}F_1(\beta_y)=\varepsilon_{1,y}$,
the counit formula of (2). The reversed bijections give the analogous
identities for the inverse. Finally, either adjunction compatibility
forces the displayed Hom-bijection, so Yoneda proves uniqueness.
