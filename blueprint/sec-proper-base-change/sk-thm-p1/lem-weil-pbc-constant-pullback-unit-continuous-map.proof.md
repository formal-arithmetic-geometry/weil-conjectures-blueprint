+++
kind = "proof"
of = "lem-weil-pbc-constant-pullback-unit-continuous-map"
uses = ["lemma-constructible-pullback-constant"]
+++
Identify the constant sheaf $\underline M_T$ on $T_{\Et}$ with the sheaf $W\mapsto\{\text{continuous maps }|W|\to M\}$, a constant section $m$ corresponding to the constant function $m$. Define $\kappa:\underline M_Y\to i_*\underline M_{Y_0}$ on $W$ by sending a continuous map $\lambda:|W|\to M$ to $\lambda\circ|\mathrm{pr}_1|:|W\times_YY_0|\to M$. It is additive (pointwise addition) and natural in $W$ (the base-change squares commute).

Both $\kappa$ and the composite $\underline M_Y\xrightarrow{\eta}i_*i^*\underline M_Y\xrightarrow{i_*c}i_*\underline M_{Y_0}$ are maps out of the constant sheaf $\underline M_Y$, so by the constant-sheaf/global-sections adjunction they are determined by their adjuncts $M\to\Gamma(Y,i_*\underline M_{Y_0})=\Gamma(Y_0,\underline M_{Y_0})$. The comparison $c$ is the uniqueness isomorphism between the adjunction (constant sheaf on $Y$ followed by $i^*$) and (constant sheaf on $Y_0$), both left adjoint to global sections on $Y_0$ [lemma-constructible-pullback-constant]; hence the adjunct of $i_*(c)\circ\eta$ sends $m$ to the constant section $m$ of $\underline M_{Y_0}$. The adjunct of $\kappa$ sends $m$ to the constant function $m\circ|\mathrm{pr}_1|=m$ as well (also on empty objects). So the two adjuncts agree, hence $\kappa=i_*(c)\circ\eta$, and evaluating at $W$ and $g$ gives $\lambda_{Y_0}(c(\eta(g)))=\lambda_Y(g)\circ|\mathrm{pr}_1|$.
