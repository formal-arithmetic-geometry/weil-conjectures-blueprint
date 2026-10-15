+++
kind = "proof"
of = "sk-lem-geo-affine-local"
uses = ["sk-prop-geo-p1-adjunction", "sk-prop-pe-unbounded-classical"]
+++
By the classical comparison ([sk-prop-pe-unbounded-classical]), the following
étale computations calculate the pro-étale adjoints together with their units
and counits.

(1) Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the open immersion, so
that $Ra_!=Rp_*j_!$ for $d=1$. Since $j_!\dashv j^*$, (G4) of
[sk-prop-geo-p1-adjunction] gives $a^!=j^*p^*(1)[2]=a^*(1)[2]$. For general
$d$, write $a$ as a composite of $d$ affine-line projections and use Stacks,
Tag [0F7J](https://stacks.math.columbia.edu/tag/0F7J). The counit is the
successive composite of the $d$ projective-line traces and the open-immersion
counits. Associativity (Stacks, Tag
[0F7K](https://stacks.math.columbia.edu/tag/0F7K)) and compatibility with base
change (Stacks, Tag [0F7L](https://stacks.math.columbia.edu/tag/0F7L)) show
that this is the counit for the canonical composition isomorphism, and that it
commutes with base change.

(2) Extension by zero
$u_!\colon\Mod(U_{\mathrm{ét}},\Lambda)\to\Mod(X_{\mathrm{ét}},\Lambda)$ is exact
and left adjoint to $u^*$ by its elementary sheaf-theoretic construction
(Stacks, Tag [03S2](https://stacks.math.columbia.edu/tag/03S2)), and the
adjunction extends to derived categories because both functors are exact. For
every $A\in D(U_{\mathrm{ét}},\Lambda)$,

$$
\Hom(A,u^*f^!N)=\Hom(u_!A,f^!N)=\Hom(Rf_!u_!A,N)=\Hom(R(fu)_!A,N),
$$

with the Hom groups taken in $D(U_{\mathrm{ét}},\Lambda)$,
$D(X_{\mathrm{ét}},\Lambda)$ and $D(S_{\mathrm{ét}},\Lambda)$, the last step by
the composition isomorphism of Stacks, Tag
[0F7J](https://stacks.math.columbia.edu/tag/0F7J). The Yoneda lemma gives
(G10), and since these bijections use exactly that composition isomorphism,
the counit of $R(fu)_!\dashv(fu)^!$ is the composite of the two counits.
Repeating the argument for a further étale map gives the compatibilities with
composition and localization.
