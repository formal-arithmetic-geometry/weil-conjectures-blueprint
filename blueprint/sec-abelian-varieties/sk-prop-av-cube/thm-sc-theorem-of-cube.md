+++
id = "thm-sc-theorem-of-cube"
kind = "theorem"
title = "The theorem of the cube"
lean = ["AlgebraicGeometry.nonempty_iso_cube"]
order = 480
uses = ["def-sc-abelian-variety", "def-sc-invertible-module", "lem-sc-abelian-variety-characterization"]
+++
Let $A$ be an abelian variety
over a field $k$, and let $\mathcal L$ be an
invertible $\mathcal O_A$-module. For $1\leq i_1<\cdots<i_t\leq3$ let
$m_{i_1,\dots,i_t}:A\times_kA\times_kA\to A$ be the partial sum
map $(x_1,x_2,x_3)\mapsto x_{i_1}+\cdots+x_{i_t}$. Then

$$
m_{123}^*\mathcal L\otimes m_1^*\mathcal L\otimes m_2^*\mathcal L
\otimes m_3^*\mathcal L
\cong m_{12}^*\mathcal L\otimes m_{13}^*\mathcal L\otimes
m_{23}^*\mathcal L
$$

on $A\times_kA\times_kA$.
