+++
kind = "proof"
of = "lemma-simple-objects"
order = 1250
uses = ["lemma-largest-punctual-subsheaf"]
+++
Since a middle extension has no punctual subobject or
quotient and $M$ is irreducible on the open, the
middle extension is simple. Conversely, ordinary truncation splits an arbitrary perverse
sheaf into a punctual part and a part of the form $F[1]$, and
simplicity forces one of them to vanish.

We first show that $P=(j_*M)[1]$ has no punctual subobject or quotient.
The adjunction calculations below are geometric, and they apply equally
to compatible Weil morphisms. Let $i$ be the inclusion of a finite set
of closed points and $A$ a sheaf on it. A map $P\to i_*A$ is zero, because by
adjunction it corresponds to a map from $i^*P=(i^*j_*M)[1]$ to the
sheaf $A$, that is, to a negative Ext. A map in the other direction is
also zero. Since $M$ is lisse, $j_*M$ does not change when we replace $U$
by a smaller dense open and $M$ by its restriction. Hence we may assume that the support of $A$ lies in
$Z=C\setminus U$, and we let $i$ now denote the inclusion of $Z$. The
adjunction $j^*\dashv Rj_*$ shows that $i^!Rj_*M=0$. In the triangle

$$
j_*M\longrightarrow Rj_*M\longrightarrow
\tau^{\ge1}Rj_*M\longrightarrow
$$

the last term is supported on $Z$, so that $i^!$ agrees with $i^*$ on
it. Applying $i^!$ and using $i^!Rj_*M=0$, we find
$i^!j_*M\simeq(i^*\tau^{\ge1}Rj_*M)[-1]$, which has ordinary
cohomology only in degrees at least two. Hence $i^!P$ has ordinary
cohomology only in degrees at least one.
Therefore $\Hom(i_*A,P)=\Hom(A,i^!P)=0$.

To see that $P$ is simple, note that on a dense open a
perverse subobject of $P$ is a shifted lisse subsheaf of $M$. By
irreducibility it is $0$ or everything there, and the difference is
then punctual. In detail, consider a perverse exact sequence
$0\to Q\to P\to R\to0$, restrict it to a smaller dense open on which
all ordinary cohomology sheaves are lisse. There $P=M[1]$, and the
sequence is a shifted exact sequence of lisse sheaves. Restriction to
a dense open preserves irreducibility, because the fundamental group
of a dense open of a normal connected curve surjects onto that of the
curve, as in the proof of Theorem [theorem-purity-real-sheaves-curves], and the same
holds for the Weil groups. So $Q$ or $R$ has zero generic
restriction. A perverse object with zero generic restriction is
punctual. Indeed, its $\mathcal H^{-1}$ is then supported on a finite
set, and a sheaf without punctual subsheaves with this property is
zero. Its $\mathcal H^0$ is punctual by definition. So $Q$ or $R$
is a punctual subobject or quotient of $P$. By the vanishing just
proved it is zero, and $P$ is simple.

Conversely, let $P$ be simple. We show that $P$ is punctual or a middle
extension of an irreducible lisse sheaf. Ordinary truncation gives a
perverse exact sequence

$$
0\longrightarrow(\mathcal H^{-1}P)[1]
\longrightarrow P\longrightarrow\mathcal H^0P\longrightarrow0.
$$

Hence a simple $P$ is either punctual or of the form $F[1]$, where $F$
has no punctual subsheaf. In the second case, choose a dense open $U$
on which $F$ is lisse and put $M=F|_U$.
The map $F\to j_*M$ is injective, since its kernel is $F_{\rm p}=0$
(Lemma [lemma-largest-punctual-subsheaf]),
and its cokernel $B$ is punctual. Rotating the corresponding triangle of sheaves we obtain the perverse
exact sequence $0\to B\to F[1]\to(j_*M)[1]\to0$. Its last term is
nonzero, so $B=0$ by simplicity. Suppose that $M$ had a proper nonzero
lisse subsheaf $M_1$. The object $j_!M_1[1]$ is perverse, because
$j_!M_1\subset j_*M_1$ has no punctual subsheaf, and the image of
$j_!M_1[1]\to P$ in the abelian heart is proper and nonzero, as one
sees on $U$. This contradicts simplicity. Finally, if $P$ is punctual, then by the
long exact cohomology sequence its subobjects in the heart are
punctual sheaves in degree zero, so $P$ is simple exactly when it is
irreducible as a punctual sheaf.
