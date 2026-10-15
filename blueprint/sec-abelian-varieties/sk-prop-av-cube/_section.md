+++
id = "sk-prop-av-cube"
kind = "proposition"
title = "The theorem of the cube"
lean = ["AlgebraicGeometry.nonempty_iso_cube"]
order = 540
uses = ["sk-def-av", "sk-def-av-pic"]
tags = ["sketch"]
+++
Let $A$ be an abelian variety over a field $k$ and let $\cL$ be an
invertible $\cO_A$-module. For $1\le i_1<\dots<i_t\le3$ let
$m_{i_1\dots i_t}:A\times_kA\times_kA\to A$ be the partial sum map
$(x_1,x_2,x_3)\mapsto x_{i_1}+\dots+x_{i_t}$. Then

$$
m_{123}^*\cL\otimes m_1^*\cL\otimes m_2^*\cL\otimes m_3^*\cL
\;\cong\;
m_{12}^*\cL\otimes m_{13}^*\cL\otimes m_{23}^*\cL
$$

on $A\times_kA\times_kA$.
