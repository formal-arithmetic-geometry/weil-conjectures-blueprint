+++
id = "lemma-weil-pbc-adic-milnor-sequence"
kind = "lemma"
title = "Milnor sequence on pro-etale test objects"
order = 1932
uses = ["def-weil-pbc-adic-derived-inverse-limit"]
+++
Let $U$ be a weakly contractible quasi-compact object of the pro-etale site.
For every tower $M_\bullet$ and every $i$ there is a functorial exact
sequence

$$
0\longrightarrow\varprojlim
{}^{1}_nH^{i-1}(U,M_n)\longrightarrow
H^i\left(U,R\varprojlim_nM_n\right)\longrightarrow
\varprojlim_nH^i(U,M_n)\longrightarrow0.
$$

## Proof

Weak contractibility makes $\Gamma(U,-)$ exact, and evaluation on $U$
commutes with products. Apply it to the product-cone triangle. The long
exact cohomology sequence identifies the kernel of $1-s$ on
$\prod_nH^i(U,M_n)$ with $\varprojlim H^i(U,M_n)$ and its cokernel in
degree $i-1$ with $\varprojlim{}^1H^{i-1}(U,M_n)$. Kernel–cokernel
exactness gives the displayed sequence, and every construction is natural
in a map of towers.
