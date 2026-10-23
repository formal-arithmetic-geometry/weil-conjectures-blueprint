+++
kind = "proof"
of = "lem-weil-pbc-finite-module-localization-zero-annihilator"
+++
Since $M$ is finitely generated, choose $m_1,\dots,m_n\in M$ ($n\ge 0$) such that every $m\in M$ can be written $m=\sum_{i=1}^n a_im_i$ with $a_i\in A$.

For each $i$, $m_i/1=0$ in $S^{-1}M=0$; by the description of the kernel of the localization map ($m/1=0$ iff $um=0$ for some $u\in S$; this is the hypothesis as phrased in the statement) there is $t_i\in S$ with $t_im_i=0$.

Put $s=t_1t_2\cdots t_n$ ($s=1$ if $n=0$); $s\in S$ since $S$ is multiplicative and contains $1$. For $m=\sum_i a_im_i\in M$, commutativity of $A$ gives $sm=\sum_i a_i\big(\prod_{j\ne i}t_j\big)(t_im_i)=0$. Hence $sM=0$.
