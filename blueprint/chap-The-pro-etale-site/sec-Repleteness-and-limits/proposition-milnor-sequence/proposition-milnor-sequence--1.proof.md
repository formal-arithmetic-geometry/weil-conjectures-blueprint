+++
kind = "proof"
of = "proposition-milnor-sequence--1"
order = 91002
+++
Everything follows from the triangle (2.1). For a tower of
modules, $R\varprojlim_nM_n$ is the fibre of a map between two sheaves in
degree $0$, so it has cohomology only in degrees $0$ and $1$, namely the
kernel and the cokernel of $1-T$. The kernel is $\varprojlim_nM_n$, and
the cokernel is $R^1\varprojlim_nM_n$, which proves the first two
assertions. For a tower of complexes, the long exact cohomology sequence
of (2.1) reads

$$
\prod_nH^{q-1}(K_n)\xrightarrow{1-T}\prod_nH^{q-1}(K_n)
\to H^q(R\varprojlim_nK_n)\to\prod_nH^q(K_n)\xrightarrow{1-T}\prod_nH^q(K_n),
$$

where we used that by Proposition [proposition-exact-products] the cohomology of each
product is the product of the cohomology sheaves. The cokernel on the left
is $R^1\varprojlim_nH^{q-1}(K_n)$ and the kernel on the right is
$\varprojlim_nH^q(K_n)$, which gives (2.2).

*Source:* the proof of Proposition [proposition-milnor-sequence].
