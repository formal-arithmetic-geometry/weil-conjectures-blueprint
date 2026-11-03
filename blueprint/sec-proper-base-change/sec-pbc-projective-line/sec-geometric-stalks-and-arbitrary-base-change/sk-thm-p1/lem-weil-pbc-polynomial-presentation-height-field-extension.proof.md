+++
kind = "proof"
of = "lem-weil-pbc-polynomial-presentation-height-field-extension"
+++
*Construction of $g$.* Let $g$ be the composite of the canonical isomorphism $K[x_1,\dots,x_n]\cong k[x_1,\dots,x_n]\otimes_kK$ with $f\otimes\mathrm{id}_K:k[x_1,\dots,x_n]\otimes_kK\to S\otimes_kK$. By right exactness of $-\otimes_kK$, $g$ is surjective and its kernel is the extension $(\ker f)K[x_1,\dots,x_n]$ of the kernel of $f$. The square formed by $f$, $g$ and the maps $k[x]\to K[x]$, $S\to S\otimes_kK$ commutes, as one checks on coefficients and variables.

*Heights.* Let $Q$ be a prime of $S\otimes_kK$ with contraction $q$ to $S$, and put $\mathfrak P=f^{-1}(q)$ and $\mathfrak P'=g^{-1}(Q)$; by commutativity of the square, $\mathfrak P'$ lies over $\mathfrak P$. Since $\ker f\subseteq\mathfrak P$, $f$ induces $k[x]/\mathfrak P\cong S/q$, and therefore the fibre rings $K[x]/\mathfrak PK[x]\cong(k[x]/\mathfrak P)\otimes_kK$ and $(S\otimes_kK)/q(S\otimes_kK)\cong(S/q)\otimes_kK$ are isomorphic, the isomorphism carrying the prime induced by $\mathfrak P'$ to the prime induced by $Q$. Hence these two primes of the fibre rings have the same height $h$.

Both maps $k[x]\to K[x]$ and $S\to S\otimes_kK$ are flat (base change of the flat extension $k\to K$ of fields), so they satisfy going down, and all four rings are Noetherian ($k[x]$ and $K[x]$ by the Hilbert basis theorem, $S$ and $S\otimes_kK$ as their quotients). For a flat map of Noetherian rings, the height of a prime equals the height of its contraction plus its height in the fibre ring. Thus $\operatorname{ht}(\mathfrak P')=\operatorname{ht}(\mathfrak P)+h$ and $\operatorname{ht}(Q)=\operatorname{ht}(q)+h$, and hence $\operatorname{ht}(f^{-1}(q))+\operatorname{ht}(Q)=\operatorname{ht}(g^{-1}(Q))+\operatorname{ht}(q)$.
