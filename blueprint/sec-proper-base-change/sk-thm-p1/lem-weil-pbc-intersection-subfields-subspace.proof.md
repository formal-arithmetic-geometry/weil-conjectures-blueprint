+++
kind = "proof"
of = "lem-weil-pbc-intersection-subfields-subspace"
+++
The forward implication is immediate: if $0\ne v\in V\cap k^{\oplus n}$, then $v\in V\cap K_\alpha^{\oplus n}$ for each $\alpha$, since $k\subseteq K_\alpha$.

For the converse, induct on $n$. If $n=1$, a $K$-subspace $V\subseteq K$ is either $0$ or $K$: a nonzero $x\in V$ gives $1=x^{-1}x\in V$. Since $\mathcal A$ is nonempty and $V\cap K_\alpha\ne0$ for every $\alpha$, $V=K$, whence $1\in V\cap k$. Now suppose $n\ge2$ and the converse holds in dimension $n-1$.

Identify the tail subspace $W=\{(x_2,\ldots,x_n)\in K^{\oplus(n-1)}:(0,x_2,\ldots,x_n)\in V\}$. It is $K$-linear. If $W\cap k^{\oplus(n-1)}\ne0$, adjoining a leading zero proves $V\cap k^{\oplus n}\ne0$. Otherwise the induction hypothesis, applied to $W$ and contraposed, gives an $\alpha\in\mathcal A$ for which $W\cap K_\alpha^{\oplus(n-1)}=0$.

Choose $0\ne w=(w_1,\ldots,w_n)\in V\cap K_\alpha^{\oplus n}$. Then $w_1\ne0$, since otherwise its tail would be a nonzero element of $W\cap K_\alpha^{\oplus(n-1)}$. Dividing by $w_1\in K_\alpha$ gives $v=(1,x_2,\ldots,x_n)\in V\cap K_\alpha^{\oplus n}$. Every $z=(z_1,\ldots,z_n)\in V\cap K_\alpha^{\oplus n}$ satisfies $z-z_1v\in V\cap(0\oplus K_\alpha^{\oplus(n-1)})=0$; thus $V\cap K_\alpha^{\oplus n}=K_\alpha v$. If $K_\beta\subseteq K_\alpha$, choose $0\ne z\in V\cap K_\beta^{\oplus n}$. The preceding equality gives $z=z_1v$ with $z_1\ne0$; hence $v=z_1^{-1}z\in K_\beta^{\oplus n}$.

Each coordinate $x_i$ of $v$ therefore belongs to every $K_\beta$ contained in $K_\alpha$. Given any $\gamma\in\mathcal A$, condition (3) supplies $\delta$ with $K_\delta\subseteq K_\alpha\cap K_\gamma$; hence $x_i\in K_\delta\subseteq K_\gamma$. Condition (2) yields $x_i\in\bigcap_\gamma K_\gamma=k$. The leading coordinate $1$ lies in $k$ too, so $0\ne v\in V\cap k^{\oplus n}$, completing the induction.
