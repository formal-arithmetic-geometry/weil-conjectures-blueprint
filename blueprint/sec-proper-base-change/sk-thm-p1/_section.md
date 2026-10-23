+++
id = "sk-thm-p1"
kind = "proposition"
title = "Proper base change for the projective line"
order = 1588
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLine", "AlgebraicGeometry.Etale.hasInjectiveAcyclicity_projectiveLine"]
uses = ["sk-thm-br", "sk-def-pbc", "sk-thm-curveestimate", "sk-def-exchange", "sk-def-ia", "sk-prop-pbc-p1-henselian", "sk-lem-pbc-curve-field-extension"]
tags = ["sketch"]
+++
Let $S$ be any scheme and $\Lambda$ any commutative ring. In the cartesian
square

$$
\begin{array}{ccc}
\mathbf P^1_T & \xrightarrow{g'} & \mathbf P^1_S\\
{\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p}\\
T & \xrightarrow{g} & S
\end{array}
$$

the exchange map [sk-def-exchange]

$$
g^{-1}Rp_*K\longrightarrow Rp'_*g'^{-1}K
$$

is an isomorphism in $D^+(T_{\Et},\Lambda)$ for every
$K\in D^+(\mathbf P^1_{S,\Et},\Lambda)$ with torsion cohomology sheaves. In
particular, $\mathrm{IA}_r(p)$ [sk-def-ia] holds for every prime $r$.
