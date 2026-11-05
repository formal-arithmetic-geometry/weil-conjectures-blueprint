+++
kind = "proof"
of = "proposition-milnor-sequence--2"
order = 91004
uses = ["proposition-exact-products--1"]
+++
Everything follows from the triangle (2.1). The cone
is formed on the level of complexes, so the triangle
$\Cone(1-T)[-1]\to\prod_nK_n\xrightarrow{1-T}\prod_nK_n\to$ is functorial in
the tower, and its long exact cohomology sequence reads

$$
\prod_nH^{q-1}(K_n)\xrightarrow{1-T}\prod_nH^{q-1}(K_n)
\to H^q(\Cone(1-T)[-1])\to\prod_nH^q(K_n)\xrightarrow{1-T}\prod_nH^q(K_n),
$$

where we used that by Proposition [proposition-exact-products] the
cohomology of each product is the product of the cohomology sheaves. The
kernel of $1-T$ on the right is $\varprojlim_nH^q(K_n)$. Let $a_K$ be the
map induced on the cokernel on the left and $b_K$ the map to this kernel;
both are natural in the tower because the triangle and its long exact
sequence are. This gives the first sequence. By clause [proposition-milnor-sequence--1],
applied to the tower of sheaves $(H^{q-1}(K_n))$, the isomorphism $e_1$
identifies $R^1\varprojlim_nH^{q-1}(K_n)=H^1(R\varprojlim_nH^{q-1}(K_n))$
with the cokernel on the left, and $\Cone(1-T)[-1]=R\varprojlim_nK_n$ by
(2.1). This gives (2.2).

For the general statement, the homotopy limit $L$ sits in a distinguished
triangle $L\to\prod_nF_n\xrightarrow{1-T}\prod_nF_n\to L[1]$ in
$D(\mathcal A)$, whose first map has the maps $L\to F_n$ as components.
The product in $D(\mathcal A)$ is the termwise product of K-injective
representatives. Since countable products in $\mathcal A$ are exact, they
commute with cohomology, so $H^i(\prod_nF_n)=\prod_nH^i(F_n)=P$, and
$H^i(1-T)$ is $1-T$ for the endomorphism $T$ of the statement. The long
exact cohomology sequence of the triangle,

$$
P\xrightarrow{1-T}P\to H^j(L)\to\prod_nH^j(F_n)\xrightarrow{1-T}\prod_nH^j(F_n),
$$

then gives the asserted sequence, since the kernel on the right is
$\varprojlim_nH^j(F_n)$.

*Source:* the proof of Proposition [proposition-milnor-sequence].
