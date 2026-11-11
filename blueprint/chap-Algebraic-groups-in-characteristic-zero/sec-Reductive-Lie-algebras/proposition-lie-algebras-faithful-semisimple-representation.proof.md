+++
kind = "proof"
of = "proposition-lie-algebras-faithful-semisimple-representation"
order = 1746
uses = ["lemma-lie-s-theorem", "lemma-killing"]
+++
We follow the two halves described at the start of this section:
first the radical is central, and then the quotient by the center
equals its derived algebra.

Put $\mathfrak r=\operatorname{rad}\mathfrak l$, and write the
faithful module as a direct sum of simple modules. Let $M$ be one of
them. By Lemma [lemma-lie-s-theorem], there is a nonzero
simultaneous $\lambda$-eigenspace $M_\lambda$ for $\mathfrak r$. We
claim that $M_\lambda$ is $\mathfrak l$-stable. To prove this, fix $x\in\mathfrak l$ and
$0\ne v\in M_\lambda$, and consider
$U=\operatorname{span}\{v,xv,x^2v,\ldots\}$. For
every $a\in\mathfrak r$ we have $[a,x]\in\mathfrak r$, and the identity

$$
ax^j=x^ja+\sum_{i=0}^{j-1}x^i[a,x]x^{j-1-i}
$$

shows, by induction on $j$, that $a$ preserves $U$ and acts on it by a
triangular matrix with constant diagonal $\lambda(a)$ in the basis
$v,xv,x^2v,\ldots$ of $U$. Indeed, the identity gives
$ax^jv=\lambda(a)x^jv$ plus terms $x^i[a,x]x^{j-1-i}v$, and by induction
applied to $[a,x]\in\mathfrak r$ these lie in the span of
$v,\ldots,x^{j-1}v$. With this, the trace of $[x,a]$ on $U$ can be computed in two
ways. Since $x$ and $a$ preserve $U$, the restriction of $[x,a]$ to $U$
is a commutator, whose trace is zero. On the other hand,
$[x,a]\in\mathfrak r$ acts on $U$ with constant diagonal
$\lambda([x,a])$. Comparing,

$$
0=\operatorname{tr}_U[x,a]=\dim(U)\lambda([x,a]),
$$

and $\lambda([x,a])=0$ because $\Omega$ has characteristic zero. It
follows that
$a(xv)=\lambda(a)xv+\lambda([a,x])v=\lambda(a)xv$, which proves the
claim.

Since $M$ is simple, the claim gives $M_\lambda=M$. Thus $\mathfrak r$
acts on $M$ by scalars, and in particular $[\mathfrak l,\mathfrak r]$
acts as zero on $M$. This holds for every simple summand, and the module
is faithful, so $[\mathfrak l,\mathfrak r]=0$, that is,
$\mathfrak r\subseteq Z(\mathfrak l)$. The reverse inclusion holds
because the center is an abelian ideal.

For the second equality, we show that the quotient
$\overline{\mathfrak l}=\mathfrak l/Z(\mathfrak l)$ has zero radical and
apply Lemma [lemma-killing]. The inverse image of a solvable ideal of the
quotient is a central extension of a solvable Lie algebra, hence
solvable. So it is contained in $\mathfrak r=Z(\mathfrak l)$. The
lemma now gives $[\overline{\mathfrak l},\overline{\mathfrak l}]
 =\overline{\mathfrak l}$. In other words, every element of $\mathfrak l$ is
congruent modulo $Z(\mathfrak l)$ to a sum of brackets, and
$\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l]$.
