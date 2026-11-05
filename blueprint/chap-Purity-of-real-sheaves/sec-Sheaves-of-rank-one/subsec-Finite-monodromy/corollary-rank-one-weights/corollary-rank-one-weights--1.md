+++
id = "corollary-rank-one-weights--1"
kind = "corollary"
title = "Local weights of a rank-one character"
order = 1110001
aliases = ["bp-r339-1"]
lean = ["AlgebraicGeometry.WeilGroup.frobeniusWeight_eq_of_continuous"]
+++
Let $U_0/\Fq$ be a smooth geometrically connected curve, put
$U=U_0\times_{\Fq}\Fbar$, and fix a prime $\ell\nmid q$ and an embedding
$\iota:\Qbarl\hookrightarrow\mathbf C$ as in [sec-Weil-sheaves-and-weights]. Let $W(U_0)$
be its Weil group, with geometric subgroup $\ker(\deg)=\pi_1(U)$ and chosen
degree-one lift $s$.

Let $\chi:W(U_0)\to\Qbarl^\times$ be a character whose restriction to
$\pi_1(U)$ is continuous, and put $c=\chi(s)$. For every closed point
$x$ of $U_0$, the local weight is

$$
\frac{2\log|\iota(\chi(\operatorname{Frob}_x))|}{\log q_x}
=\frac{2\log|\iota(c)|}{\log q}
=\lambda_\iota(c).
$$

In particular, every rank-one lisse Weil sheaf on $U_0$ is punctually
$\iota$-pure of weight $\lambda_\iota(c)$, where $\chi$ is its character.
