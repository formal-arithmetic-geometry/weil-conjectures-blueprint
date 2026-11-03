+++
kind  = "proof"
of    = "sk-lem-walg-lie-eigenvector"
+++
We argue by induction on the dimension of the Lie algebra $\mathfrak r$.
For $\mathfrak r=0$ there is nothing to prove. Otherwise, choose an ideal
$\mathfrak a\supseteq[\mathfrak r,\mathfrak r]$ of codimension one and
write $\mathfrak r=\mathfrak a+LX$. By induction, $\mathfrak a$ has a
common eigenvector $v$, with character $\lambda$. Put
$U=\operatorname{span}\{v,Xv,X^2v,\ldots\}$. For $a\in\mathfrak a$, the
identity

$$
aX^j=X^ja+\sum_{i=0}^{j-1}X^i[a,X]X^{j-1-i}
$$

shows by induction that $U$ is $\mathfrak a$-stable and that $a$ acts
upper triangularly in the cyclic basis with constant diagonal
$\lambda(a)$. Since both $X$ and $a$ preserve $U$, we get

$$
0=\operatorname{tr}_U[X,a]=\dim(U)\lambda([X,a]).
$$

As $L$ has characteristic zero, it follows that $\lambda([X,a])=0$. Hence
the simultaneous $\lambda$-eigenspace $U_\lambda$ of $\mathfrak a$, which
contains $v$, is $X$-stable. An eigenvector of $X$ in $U_\lambda$ is then a
common eigenvector for $\mathfrak r$. A character obtained in this way
vanishes on $[\mathfrak r,\mathfrak r]$, since brackets act as zero on a
line.
