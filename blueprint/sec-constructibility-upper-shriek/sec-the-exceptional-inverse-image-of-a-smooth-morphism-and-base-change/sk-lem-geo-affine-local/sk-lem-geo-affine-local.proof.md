+++
kind = "proof"
of = "sk-lem-geo-affine-local"
uses = ["sk-prop-geo-p1-adjunction", "sk-lem-geo-p1-cohomology"]
+++
Both parts are formal consequences of uniqueness of right adjoints: (1)
from (7.4) and $j_!\dashv j^*$ for $\mathbf A^1\subset\mathbf P^1$, and
(2) from $u_!\dashv u^*$ for étale $u$.

(1) Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the open
immersion, so that $Rp_{1!}=Rp_*j_!$ for $d=1$. Since $j_!\dashv j^*$,
it follows from (7.4) that $p_1^!=j^*p^*(1)[2]=p_1^*(1)[2]$. For general $d$, we write
$p_d$ as a composite of $d$ projections of affine lines. By
[Stacks, Tag 0F7J](https://stacks.math.columbia.edu/tag/0F7J), $Rp_{d!}$ is the composite of their functors $R(-)_!$, and
hence $p_d^!$ is the composite of their right adjoints, which is
$p_d^*(d)[2d]$ by the case $d=1$. Under the isomorphism
$Rp_{d!}\simeq Rr_{1!}\circ\dots\circ Rr_{d!}$ of [Stacks, Tag 0F7J](https://stacks.math.columbia.edu/tag/0F7J), where
$r_1,\dots,r_d$ are these projections, the counit of
$Rp_{d!}\dashv p_d^*(d)[2d]$ is the composite of the $d$ counits for the
affine lines. Each of these is a trace (7.3) composed with the counit of
$j_!\dashv j^*$, and the composite does not depend on how the
$d$ factors are grouped, by associativity [Stacks, Tag 0F7K](https://stacks.math.columbia.edu/tag/0F7K). Each factor
commutes with base change, and so does the composition isomorphism
[Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L). Hence the counit commutes with base change, and so does
the unit, since it is determined by the counit through the triangle
identities.

(2) By its elementary construction [Stacks, Tag 03S2](https://stacks.math.columbia.edu/tag/03S2), extension by zero
$u_!:\operatorname{Mod}(U_{\acute{e}t},\Lambda)\to \operatorname{Mod}(X_{\acute{e}t},\Lambda)$ is exact and
left adjoint to $u^*$. Since both functors are exact, the adjunction
extends to derived categories. For every $M\in D(U_{\acute{e}t},\Lambda)$,

$$
\Hom(M,u^*f^!N)
=\Hom(u_!M,f^!N)
=\Hom(Rf_!u_!M,N)
=\Hom(R(fu)_!M,N),
$$

where the last step is the composition isomorphism of [Stacks, Tag 0F7J](https://stacks.math.columbia.edu/tag/0F7J). By the
Yoneda lemma, we obtain (7.10). Since these bijections use exactly that
composition isomorphism, the counit of $R(fu)_!\dashv(fu)^!$ is the
composite of the two counits. Repeating the argument for a further
étale map, we obtain the compatibilities with composition and
localization.
