+++
kind = "proof"
of = "lemma-sections-support-closed-subscheme"
order = 278
uses = ["proposition-etale-implications", "proposition-pro-etale-affines-form-basis", "definition-local-cohomology", "lemma-local-cohomology-right-adjoint"]
+++
Lemma [lemma-local-cohomology-right-adjoint] gives the adjunction
between $i_*$ and $R\underline\Gamma_Z$ on derived categories. What is new
here is that $R\underline\Gamma_Z$ is the right derived functor of
$\underline\Gamma_Z$, and this upgrades the adjunction to $R\!\operatorname{Hom}$ complexes
and yields formula (3.1). For this we show two things:
$\underline\Gamma_Z$ is right adjoint to the exact functor $i_*$ on
sheaves, and $M\to j_*j^*M$ is surjective for injective $M$. The second means
that on injective sheaves the kernel of this map is also its fibre.

We use that $i^*$ and $i_*$ are exact, that $i^*i_*=\mathrm{id}$, and
that every sheaf $M$ sits in the localization sequence
$0\to j_!j^*M\to M\to i_*i^*M\to0$ [Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA), [09AH](https://stacks.math.columbia.edu/tag/09AH), [09BM](https://stacks.math.columbia.edu/tag/09BM)].
The last fact shows that a sheaf whose restriction to $V$ vanishes is of
the form $i_*$ of a sheaf on $Z$. In particular
$\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$.

*Adjunction on sheaves.* The functor $\underline\Gamma_Z$ is right
adjoint to $i_*:\operatorname{Mod}(Z_{\mathrm{pro}\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
Indeed, a map $i_*N\to M$ composes to zero with $M\to j_*j^*M$, because
$j^*i_*N=0$, so it factors through
$\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$. Since $i_*$ is fully
faithful, such factorizations are the maps $N\to\underline\Gamma_Z(M)$.
Moreover, as $i_*$ is exact, its right adjoint $\underline\Gamma_Z$ preserves
K-injective complexes.

*Surjectivity on injectives.* For an injective sheaf $I$ the unit
$I\to j_*j^*I$ of the adjunction $j^*\dashv j_*$ on
$\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is surjective, because it has a right inverse.
To construct it, extend the inclusion $j_!j^*I\to I$ along
$j_!j^*I\hookrightarrow j_*j^*I$ to a map $s:j_*j^*I\to I$, which is
possible because $I$ is injective. Then the composite
$j_*j^*I\xrightarrow{s}I\to j_*j^*I$ restricts to the identity on $V$.
Since $j_*$ is fully faithful, an endomorphism of $j_*j^*I$ is determined by
its restriction to $V$, and so this composite is the identity.

*Comparison with the fibre.* The right derived functor of
$\underline\Gamma_Z$ agrees with $i^*\fib(K\to Rj_*j^*K)$. To see this,
represent $K$ by a K-injective complex $I^\bullet$ with injective terms
[Stacks, [079P](https://stacks.math.columbia.edu/tag/079P)]. Then $\underline\Gamma_Z(I^\bullet)$ computes the right
derived functor of $\underline\Gamma_Z$ at $K$. On the other side, the complex
$j^*I^\bullet$ is K-injective, because the left adjoint $j_!$ of $j^*$ is
exact. Hence $j_*j^*I^\bullet$ represents $Rj_*j^*K$. By the surjectivity just
proved, the sequences

$$
0\to i_*\underline\Gamma_Z(I^n)\to I^n\to j_*j^*I^n\to0
$$

are exact termwise, and they define a distinguished triangle
$i_*\underline\Gamma_Z(I^\bullet)\to K\to Rj_*j^*K\to i_*\underline\Gamma_Z(I^\bullet)[1]$.
Applying $i^*$ and using $i^*i_*=\mathrm{id}$ identifies
$\underline\Gamma_Z(I^\bullet)$ with $i^*\fib(K\to Rj_*j^*K)$.

*Part (1).* With $I^\bullet$ as above, the complex
$\underline\Gamma_Z(I^\bullet)$ is K-injective by the adjunction on
sheaves, and it represents $R\underline\Gamma_ZK$ by the comparison with
the fibre. The adjunction on complexes therefore gives

$$
R\!\operatorname{Hom}_X(i_*N,K)=\Hom^\bullet(i_*N,I^\bullet)
=\Hom^\bullet(N,\underline\Gamma_Z(I^\bullet)),
$$

whose right-hand side is $R\!\operatorname{Hom}_Z(N,R\underline\Gamma_ZK)$.

*Formula (3.1).* Since $a_!=i_*u_!$, part (1),
the adjunction $u_!\dashv u^*$ and the identity
$\cHom(L,-)=L^\vee\otimes-$ for the finite locally projective sheaf $L$
give
$R\!\operatorname{Hom}_X(i_*u_!L,K)=R\!\operatorname{Hom}_Z(u_!L,R\underline\Gamma_ZK)
=R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$.
