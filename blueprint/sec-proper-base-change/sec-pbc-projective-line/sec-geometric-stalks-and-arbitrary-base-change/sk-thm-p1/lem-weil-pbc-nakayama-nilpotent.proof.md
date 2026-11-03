+++
kind = "proof"
of = "lem-weil-pbc-nakayama-nilpotent"
+++
First prove part (9) of the source. Let $Q$ be any $R$-module with $Q=IQ$. By induction on $n\geq 0$, $Q=I^nQ$: the case $n=0$ is immediate, and if $Q=I^nQ$, then $Q=IQ=I(I^nQ)=I^{n+1}Q$. Choose $k\geq1$ with $I^k=0$. Then $Q=I^kQ=0$.

Now let $L,L'\subseteq M$ be submodules with $M=L+IL'$. In the quotient $Q=M/L$, every class is represented by an element $l+\sum_j i_jx_j$ with $l\in L$, $i_j\in I$, and $x_j\in L'$, hence lies in $IQ$; conversely $IQ\subseteq Q$, so $Q=IQ$. Step 1 gives $Q=0$, and therefore $M=L$. This is part (10) of the source.

Apply Step 2 with $L=u(N)$ and $L'=M$. Surjectivity of $N/IN\to M/IM$ is equivalent to $M=u(N)+IM$, so Step 2 yields $M=u(N)$. Thus $u$ is surjective, proving part (11) and the stated result.
