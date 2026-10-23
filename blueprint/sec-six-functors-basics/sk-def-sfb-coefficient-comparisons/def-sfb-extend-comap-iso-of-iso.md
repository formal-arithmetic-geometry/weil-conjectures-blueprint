+++
id = "def-sfb-extend-comap-iso-of-iso"
kind = "definition"
title = "Restriction of scalars and extension of scalars along isomorphisms"
order = 2605
uses = ["det-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Mod.extendScalarsComapIsoOfIsIso"]
+++
Let $\mathcal C$ be a braided monoidal closed category with equalizers and coequalizers in which
tensoring on either side preserves colimits, and let

$$
\begin{array}{ccc}
R & \xrightarrow{\ \varphi\ } & S\\
{\scriptstyle a}\downarrow & & \downarrow{\scriptstyle b}\\
R' & \xrightarrow{\ \psi\ } & S'
\end{array}
$$

be a commutative square ($\psi\circ a=b\circ\varphi$) of morphisms of monoid objects, with $R$,
$S$ commutative and $a$, $b$ isomorphisms. With $\operatorname{Res}$, $\operatorname{Ext}$ as in
[det-def-sfb-change-of-scalars], there is a natural isomorphism

$$
\operatorname{Res}_\psi\circ\operatorname{Ext}_b\;\cong\;\operatorname{Ext}_a\circ
\operatorname{Res}_\varphi\colon\Mod_S(\mathcal C)\longrightarrow\Mod_{R'}(\mathcal C).
$$
