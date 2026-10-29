+++
kind  = "proof"
of    = "sk-lem-formal-closed-support"
+++
Since a sheaf vanishing on $V$ is pushed forward from $Z$, the functor $\underline\Gamma_Z$ is
right adjoint to the exact functor $i_*$. To compare its derived functor with the fibre, we
show that the map $M\to j_*j^*M$ is surjective for injective $M$, so that on injective sheaves
the kernel of this map is also its fibre.

Recall that $i^*$ and $i_*$ are exact, that $i^*i_*=\mathrm{id}$, and that every sheaf $M$ sits
in the localization sequence $0\to j_!j^*M\to M\to i_*i^*M\to0$
([Stacks, Tag 09AA](https://stacks.math.columbia.edu/tag/09AA),
[Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH),
[Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM)). By the last fact, a sheaf whose
restriction to $V$ vanishes is of the form $i_*$ of a sheaf on $Z$. In particular this holds
for $\ker(M\to j_*j^*M)$.

*Adjunction.* A map $i_*N\to M$ composes to zero with $M\to j_*j^*M$, because $j^*i_*N=0$.
Hence it factors through $\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$, and by full
faithfulness of $i_*$ it corresponds to a map $N\to\underline\Gamma_Z(M)$. In other words,
$\underline\Gamma_Z$ is right adjoint to
$i_*\colon\Mod(Z_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$. Since $i_*$ is
exact, its right adjoint $\underline\Gamma_Z$ preserves K-injective complexes. Represent $K$ by
a K-injective complex $I^\bullet$ ([Stacks, Tag 079P](https://stacks.math.columbia.edu/tag/079P)).
Then $\underline\Gamma_Z(I^\bullet)$ is K-injective and computes the right derived functor of
$\underline\Gamma_Z$ at $K$, and the adjunction on complexes gives
$$
R\operatorname{Hom}_X(i_*N,K)=\Hom^\bullet(i_*N,I^\bullet)=\Hom^\bullet(N,\underline\Gamma_Z(I^\bullet)).
$$
The right-hand side is $R\operatorname{Hom}_Z(N,R\underline\Gamma_ZK)$ by the comparison with
the fibre, which we prove next. Details: [det-lem-formal-closed-support-sheaves].

*Comparison with the fibre.* It remains to identify the right derived functor of
$\underline\Gamma_Z$ with $i^*\fib(K\to Rj_*j^*K)$. We first show that for an injective sheaf
$I$ the unit $I\to j_*j^*I$ of the adjunction $j^*\dashv j_*$ on
$\Mod(X_{\mathrm{proét}},\Lambda)$ is surjective. Indeed, by injectivity the inclusion
$j_!j^*I\to I$ extends along $j_!j^*I\hookrightarrow j_*j^*I$ to a map
$s\colon j_*j^*I\to I$. The composite of $s$ and the unit, $j_*j^*I\xrightarrow{s}I\to j_*j^*I$,
restricts to the identity on $V$. Since $j_*$ is fully faithful, an endomorphism of
$j_*j^*I$ is determined by its restriction to $V$, so this composite is the identity, and
hence the unit $I\to j_*j^*I$ is surjective. Now represent $K$ by a K-injective complex
$I^\bullet$ with injective terms ([Stacks, Tag 079P](https://stacks.math.columbia.edu/tag/079P)).
Then $j^*I^\bullet$ is K-injective, since the left adjoint $j_!$ of $j^*$ is exact, and hence
$j_*j^*I^\bullet$ represents $Rj_*j^*K$. The termwise exact sequences
$$
0\to i_*\underline\Gamma_Z(I^n)\to I^n\to j_*j^*I^n\to0
$$
define a distinguished triangle
$i_*\underline\Gamma_Z(I^\bullet)\to K\to Rj_*j^*K\to i_*\underline\Gamma_Z(I^\bullet)[1]$.
Applying $i^*$ and using $i^*i_*=\mathrm{id}$, we identify $\underline\Gamma_Z(I^\bullet)$, which
computes the right derived functor of $\underline\Gamma_Z$ at $K$, with
$i^*\fib(K\to Rj_*j^*K)$. Details: [det-lem-formal-closed-support-derived].

*The stratum formula.* Recall that $a_!=i_*u_!$. Using part (1), the adjunction
$u_!\dashv u^*$ and the identity $\cHom(L,-)=L^\vee\otimes-$ for the finite locally projective
sheaf $L$, we find that
$R\operatorname{Hom}_X(i_*u_!L,K)=R\operatorname{Hom}_Z(u_!L,R\underline\Gamma_ZK)=R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$.
Details: [det-lem-formal-closed-support-stratum].
