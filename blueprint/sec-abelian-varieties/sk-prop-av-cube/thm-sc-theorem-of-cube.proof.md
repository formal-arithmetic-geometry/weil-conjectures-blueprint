+++
kind  = "proof"
of    = "thm-sc-theorem-of-cube"
+++
*Reference: Stacks Project, Groupoid Schemes, Lemma 39.9.6,
[Tag 0BFE](https://stacks.math.columbia.edu/tag/0BFE).* Apply
the general theorem of the cube (More on Morphisms, Theorem
37.33.8, [Tag 0BF4](https://stacks.math.columbia.edu/tag/0BF4)) to the difference

$$
\mathcal M=m_{123}^*\mathcal L\otimes m_1^*\mathcal L\otimes
m_2^*\mathcal L\otimes m_3^*\mathcal L\otimes
m_{12}^*\mathcal L^{-1}\otimes m_{13}^*\mathcal L^{-1}\otimes
m_{23}^*\mathcal L^{-1}
$$

with $X=Y=Z=A$ over $S=\operatorname{Spec}k$ and the unit
sections $x=y=e$. The hypotheses of [Tag 0BF4](https://stacks.math.columbia.edu/tag/0BF4) hold:
$A\to\operatorname{Spec}k$ is flat, proper and of finite
presentation with geometrically integral fibres ($A$ is smooth,
proper and connected, hence geometrically integral by [lem-sc-abelian-variety-characterization] and Groupoid
Schemes, Remark 39.9.12,
[Tag 0H2U](https://stacks.math.columbia.edu/tag/0H2U)), and
$A$ is connected, so it has a $k$-point (the unit). On
$A\times A\times e$ the restriction of $\mathcal M$ is

$$
n_{12}^*\mathcal L\otimes n_1^*\mathcal L\otimes n_2^*\mathcal
L\otimes e^*\mathcal L\otimes n_{12}^*\mathcal L^{-1}\otimes
n_1^*\mathcal L^{-1}\otimes n_2^*\mathcal L^{-1}\cong\mathcal O,
$$

where $n_{i_1,\dots,i_t}(x_1,x_2)=x_{i_1}+\cdots+x_{i_t}$ and
$e^*\mathcal L\cong\mathcal O$ (an invertible module on the
point); the same computation on $A\times e\times A$ and
$e\times A\times A$ shows $\mathcal M$ trivial on the slices
required by [Tag 0BF4](https://stacks.math.columbia.edu/tag/0BF4), and $\mathcal M$ is trivial on the fibre
$A\times A\times e$. Hence $\mathcal M\cong\mathcal O$, which
is the displayed relation.
