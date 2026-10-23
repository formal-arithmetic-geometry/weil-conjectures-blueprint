+++
kind  = "proof"
of    = "sk-p-lie"
+++
Put $\mathfrak r=\rad\mathfrak l$, and write the faithful module as a
direct sum of simple modules. Let $M$ be one of them. By
[sk-lem-walg-lie-eigenvector], there is a nonzero simultaneous
$\lambda$-eigenspace $M_\lambda$ for $\mathfrak r$. We claim that
$M_\lambda$ is $\mathfrak l$-stable. Fix $x\in\mathfrak l$ and
$0\ne v\in M_\lambda$, and consider
$U=\operatorname{span}\{v,xv,x^2v,\ldots\}$. Since
$[\mathfrak r,x]\subseteq\mathfrak r$, the calculation in the cyclic basis
from the proof of [sk-lem-walg-lie-eigenvector] applies: each
$a\in\mathfrak r$ preserves $U$ and acts on it by a triangular matrix with
constant diagonal $\lambda(a)$. Therefore

$$
0=\operatorname{tr}_U[x,a]=\dim(U)\lambda([x,a]),
\qquad \lambda([x,a])=0.
$$

It follows that $a(xv)=\lambda(a)xv+\lambda([a,x])v=\lambda(a)xv$, which
proves the claim. Since $M$ is simple, we get $M_\lambda=M$, and in
particular $[\mathfrak l,\mathfrak r]$ acts as zero on $M$. As this holds
for every simple summand and the module is faithful, we conclude that
$[\mathfrak l,\mathfrak r]=0$, that is, $\mathfrak r\subseteq
Z(\mathfrak l)$. The reverse inclusion holds because the center is an
abelian ideal.

Next, the quotient $\overline{\mathfrak l}=\mathfrak l/Z(\mathfrak l)$ has
zero radical. Indeed, the inverse image of a solvable ideal of the quotient
is a central extension of a solvable Lie algebra, hence solvable, and
therefore contained in $\mathfrak r=Z(\mathfrak l)$. By
[sk-lem-walg-killing], we have
$[\overline{\mathfrak l},\overline{\mathfrak l}]=\overline{\mathfrak l}$.
Thus every element of $\mathfrak l$ is congruent modulo $Z(\mathfrak l)$
to a sum of brackets, which proves that
$\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l]$.
