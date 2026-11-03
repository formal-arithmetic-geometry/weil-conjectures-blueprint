+++
kind = "proof"
of = "lem-weil-pbc-finite-product-integral-closure"
+++
If a tuple $(s_i)\in S$ is integral over $R$, applying the coordinate projections $R\to R_i$, $S\to S_i$ to a monic equation shows that each $s_i$ is integral over $R_i$.

Conversely, suppose each $s_i$ is a root of a monic polynomial $P_i\in R_i[X]$. Let $N$ be the maximum of the degrees and replace $P_i$ by $X^{N-\deg P_i}P_i$, which is monic of degree $N$ and still annihilates $s_i$. Assembling the coefficients coordinatewise gives a monic polynomial of degree $N$ over $R=\prod_iR_i$ which annihilates $(s_i)$. (For the empty product everything is zero.) This proves that the integral closure of $R$ in $S$ is $\prod_iS_i'$.

If every $R_i\to S_i$ is injective, then $R$ is integrally closed in $S$ iff $\prod_iS_i'=\prod_iR_i$, iff $S_i'=R_i$ for every $i$ (test with tuples supported in a single coordinate), i.e. iff each $R_i$ is integrally closed in $S_i$.
