+++
kind = "proof"
of = "lemma-affine-space-etale-localization"
order = 560
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-adjunction-projective-line", "proposition-six-operations-change-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Both parts follow formally from uniqueness of right adjoints. Part (1)
comes from (6.9) and $j_!\dashv j^*$ for $\mathbf A^1\subset\mathbf P^1$, and
part (2) from $u_!\dashv u^*$ for étale $u$.

(1) Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the open
immersion, so that $Rp_{1!}=Rp_*j_!$ for $d=1$.
Since $j_!\dashv j^*$ and $Rp_*\dashv p^*(1)[2]$ by (6.9),
composing right adjoints gives $p_1^!=j^*p^*(1)[2]$. This equals
$p_1^*(1)[2]$ because $p\circ j=p_1$. For general $d$, write $p_d$ as a
composite of $d$ projections $r_1,\dots,r_d$ of affine lines. By the composition isomorphism for $Rf_!$ (Proposition [proposition-composition-base-change-rf-shriek](1)) we have
$Rp_{d!}\simeq Rr_{1!}\circ\dots\circ Rr_{d!}$.
Hence $p_d^!$ is the composite of the right adjoints of the $Rr_{i!}$,
which is $p_d^*(d)[2d]$ by the case $d=1$. Under this isomorphism, the
counit of $Rp_{d!}\dashv p_d^*(d)[2d]$ is the composite of the $d$ counits
for the affine lines. Each of these is a trace (6.5)
composed with the counit of $j_!\dashv j^*$. By the associativity in Proposition [proposition-composition-base-change-rf-shriek](1), the composite does not depend
on how the $d$ factors are grouped. Each factor and the composition
isomorphism commute with base change (Proposition [proposition-composition-base-change-rf-shriek](2)), and therefore so does the counit. The unit is determined
by the counit through the triangle identities, and it commutes with base
change as well.

(2) For an étale $u$, the functor $Ru_!$ is extension by zero. By its
elementary construction [Stacks, [03S2](https://stacks.math.columbia.edu/tag/03S2)], it is an exact functor
$u_!:\operatorname{Mod}(U_{\acute{e}t},A)\to\operatorname{Mod}(X_{\acute{e}t},A)$ left adjoint to $u^*$.
As both functors are exact, they need not be derived, and the adjunction
extends to derived categories. For every $M\in D(U_{\acute{e}t},A)$,

$$
\Hom(M,u^*f^!N)
=\Hom(u_!M,f^!N)
=\Hom(Rf_!u_!M,N)
=\Hom(R(fu)_!M,N),
$$

where the last step is the composition isomorphism of
Proposition [proposition-composition-base-change-rf-shriek](1). The Yoneda lemma therefore gives (6.12). Taking $M=u^*f^!N$ and the
identity on the left, we see that the counit of $R(fu)_!\dashv(fu)^!$ is the composite of the counits as stated. For the cocycle condition, the isomorphism for $uu'$ and the
composite of those for $u$ and $u'$ both correspond under the Yoneda lemma
to the bijections obtained from the composition isomorphism for
$f\circ u\circ u'$. These bijections agree by associativity of the
composition isomorphisms (Proposition [proposition-composition-base-change-rf-shriek](1)).
