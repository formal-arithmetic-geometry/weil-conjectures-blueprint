+++
kind  = "proof"
of    = "sk-lem-wft-curve-simples"
+++
We first show that $P=(j_*M)[1]$ has no punctual subobject or quotient.
The adjunction calculations below are geometric, and they apply equally
to compatible Weil morphisms. A map $P\to i_*A$ is zero, because by
adjunction it corresponds to a map from $i^*P=(i^*j_*M)[1]$ to the
sheaf $A$, that is, to a negative Ext. A map in the other direction is
also zero. To see this, shrink $U$ so that the support of $A$ lies in
$Z=C\setminus U$. The adjunction $j^*\dashv Rj_*$ shows that
$i^!Rj_*M=0$. In the triangle

$$
 j_*M\longrightarrow Rj_*M\longrightarrow
                         \tau^{\ge1}Rj_*M\longrightarrow
$$

the last term is supported on $Z$. Applying $i^!$, we see that
$i^!(j_*M)[1]$ has ordinary cohomology only in degrees at least one.
Therefore $\operatorname{Hom}(i_*A,P)=\operatorname{Hom}(A,i^!P)=0$.

Next we show that $P$ is simple. Given a perverse exact sequence
$0\to Q\to P\to R\to0$, restrict it to a smaller dense open on which
all ordinary cohomology sheaves are lisse. There $P=M[1]$, and the
sequence is a shifted exact sequence of lisse sheaves. Restriction to
a dense open preserves irreducibility, because the fundamental group
of a dense open of a normal connected curve surjects onto that of the
curve; indeed, the inverse image of the open in a connected finite
étale cover remains connected. The same surjectivity holds for the
degree-preserving Weil groups. Hence $Q$ or $R$ has zero generic
restriction. A perverse object with zero generic restriction is
punctual, and so the vanishing just proved shows that $P$ is simple.

Conversely, let $P$ be simple. Ordinary truncation gives a perverse
exact sequence

$$
 0\longrightarrow(\mathcal H^{-1}P)[1]
 \longrightarrow P\longrightarrow\mathcal H^0P\longrightarrow0.
$$

Hence a simple $P$ is either punctual or of the form $F[1]$, where $F$
has no punctual subsheaf. In the second case, choose a dense open $U$
on which $F$ is lisse and put $M=F|_U$.
The map $F\to j_*M$ is injective with punctual cokernel $B$, and
rotating the corresponding triangle of sheaves we obtain the perverse
exact sequence $0\to B\to F[1]\to(j_*M)[1]\to0$. Its last term is
nonzero, so $B=0$ by simplicity. Suppose that $M$ had a proper nonzero
lisse subsheaf $M_1$. The object $j_!M_1[1]$ is perverse, because
$j_!M_1\subset j_*M_1$ has no punctual subsheaf, and the image of
$j_!M_1[1]\to P$ in the abelian heart is proper and nonzero, as one
sees on $U$. This contradicts simplicity. Finally, the punctual simple
objects are classified by the submodules of their finite-dimensional
stalks.
