+++
kind = "proof"
of = "def-weil-pbc-constant-group-scheme"
+++
*The data are well formed.* $E$ is a set, so the coproduct $\coprod_{e\in E}T$ exists with coprojections $\iota_e$, which are open immersions with pairwise disjoint images covering $T_E$; its universal property applied to the family $(\mathrm{id}_T)_{e\in E}$ gives the unique $\pi$ with $\pi\circ\iota_e=\mathrm{id}_T$. The fibre product $P$ of $\pi$ with itself exists and $\pi\circ p=\pi\circ q$ by its commutative square, so $\rho$ is well defined.

*The multiplication exists.* Pulling the cover $(V_e)_e$ back along $p$ and along $q$ covers $P$ by the opens $W_{e,e'}$, and $W_{e,e'}\cong T\times_TT$. The morphisms $\iota_{e+e'}\circ\rho|_{W_{e,e'}}$ agree on overlaps, since overlaps of distinct pieces are empty, so they glue to a morphism $m:P\to T_E$. Comparing $\pi\circ m$ and $\rho$ on each $W_{e,e'}$ gives $\pi\circ m=\rho$.

*Points.* For $T$-morphisms $f,g:U\to T_E$ we have $\pi\circ f=s=\pi\circ g$, so the universal property of $P$ gives the unique $(f,g)$ with $p\circ(f,g)=f$, $q\circ(f,g)=g$, and $\pi\circ m\circ(f,g)=\rho\circ(f,g)=s$, so $f+g$ is a $T$-morphism. $c_e=\iota_e\circ s$ is a $T$-morphism: $\pi\circ\iota_e\circ s=s$.
