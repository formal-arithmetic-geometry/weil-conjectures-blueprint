+++
kind = "proof"
of = "lem-weil-pbc-finite-free-resolution-noetherian"
+++
Base step. Since $M$ is finitely generated, choose generators $m_1,\ldots,m_{n_0}\in M$ and let $\varepsilon:R^{\oplus n_0}\to M$ be the $R$-linear map sending the $j$-th standard basis vector $e_j$ to $m_j$. Every element of $M$ is an $R$-linear combination $\sum_j a_jm_j=\varepsilon(\sum_j a_je_j)$, so $\varepsilon$ is surjective. (Put $F_{-1}=M$, $d_0=\varepsilon$.)

Inductive step. Suppose for some $e\ge0$ an $R$-linear map $d_e:R^{\oplus n_e}\to F_{e-1}$ has been constructed (with $F_{e-1}=R^{\oplus n_{e-1}}$ for $e\ge1$ and $F_{-1}=M$). Let $K_e=\ker d_e\subseteq R^{\oplus n_e}$. The module $R^{\oplus n_e}$ is finitely generated (by $e_1,\ldots,e_{n_e}$) and $R$ is Noetherian, so its submodule $K_e$ is finitely generated. As in the base step choose generators $k_1,\ldots,k_{n_{e+1}}$ of $K_e$ and let $d_{e+1}:R^{\oplus n_{e+1}}\to R^{\oplus n_e}$ send $e_j\mapsto k_j$; then $\operatorname{im}d_{e+1}=K_e=\ker d_e$.

Iteration. Applying the inductive step for $e=0,1,2,\ldots$ (definition by recursion on $e$, choosing at each stage generators of $K_e$) gives integers $n_0,n_1,n_2,\ldots\ge0$ and maps $\varepsilon=d_0$, $d_1,d_2,\ldots$ with $\operatorname{im}d_{e+1}=\ker d_e$ for every $e\ge0$.

Exactness. By the base step $\varepsilon$ is surjective, i.e. the sequence is exact at $M$; by the iteration $\operatorname{im}d_1=\ker\varepsilon$ and $\operatorname{im}d_{i+1}=\ker d_i$ for all $i\ge1$. In particular $d_i\circ d_{i+1}=0$ and $\varepsilon\circ d_1=0$, so $\cdots\to R^{\oplus n_1}\to R^{\oplus n_0}\to M\to0$ is an exact complex of finite free $R$-modules, as claimed.
