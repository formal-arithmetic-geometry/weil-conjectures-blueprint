+++
id = "def-sfb-comap-mapmod-square"
kind = "definition"
title = "Restriction of scalars along a square of ring objects"
order = 1723
uses = ["sk-def-sfb-transport", "sk-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Mod.comapMapModComapIso"]
+++
Let $F\colon\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal categories, and
let

$$
\begin{array}{ccc}
R_Y & \xrightarrow{\ \varphi_Y\ } & S_Y\\
{\scriptstyle\eta_R}\downarrow & & \downarrow{\scriptstyle\eta_S}\\
FR_X & \xrightarrow{\ F\varphi_X\ } & FS_X
\end{array}
$$

be a commutative square of morphisms of monoid objects, with $\varphi_X\colon R_X\to S_X$ in
$\mathcal C$ and $R_Y,S_Y$ monoid objects of $\mathcal D$. With $\mathrm{mapMod}(F)$ the
transport of module objects of [sk-def-sfb-transport] and $\operatorname{Res}$ the restriction of
scalars of [sk-def-sfb-change-of-scalars], the natural isomorphism

$$
\operatorname{Res}_{\varphi_Y}\circ\operatorname{Res}_{\eta_S}\circ\mathrm{mapMod}(F)
\;\cong\;
\operatorname{Res}_{\eta_R}\circ\mathrm{mapMod}(F)\circ\operatorname{Res}_{\varphi_X}
\colon\Mod_{S_X}(\mathcal C)\longrightarrow\Mod_{R_Y}(\mathcal D)
$$

is the one under which both sides are $\mathrm{mapMod}(F)$ followed by the restriction of
scalars along the common composite $\eta_S\circ\varphi_Y=F\varphi_X\circ\eta_R$.
