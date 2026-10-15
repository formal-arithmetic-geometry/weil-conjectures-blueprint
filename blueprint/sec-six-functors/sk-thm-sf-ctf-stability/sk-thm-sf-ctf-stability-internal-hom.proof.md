+++
kind = "proof"
of = "det-thm-sf-ctf-stability-internal-hom"
+++
*Dévissage of the first argument.* For finite $A$, take a bounded flat
constructible model of $K$ ([sk-lem-sf-flat-model]) and a finite
stratification on whose strata all its terms are locally constant; on a
stratum $S$, the restriction of the model is a bounded complex of finite flat,
hence finite projective, locally constant sheaves, i.e. a locally constant
perfect complex. The open–closed localization triangles along the
stratification express $K$ as a finite iterated cone of the $a_!(K|_S)$
(equivalently, one may filter the flat model by its stupid truncations). For $\mathcal O_E$, $E$ and
$\Qlb$, the constructible local models on strata (lisse sheaves, locally
completions of finite free complexes, [sk-def-sfb-dc-restricted-functors])
give the same description. So it suffices to treat $K=a_!P$, since
$\cHom(-,L)$ is exact and $\Dctf$ is triangulated.

*The formula.* For a locally closed immersion $a$ the trivial
compactification of its closed part gives $Ra_!=a_!$, and $a_!\dashv a^!$ on
the localizing categories; tensor–Hom adjunction together with the
projection formula $a_!(P\otimes^{\mathbf L}a^*M)\simeq a_!P\otimes^{\mathbf L}M$
gives, for every $M$,
$\Hom(M,\cHom_X(a_!P,L))=\Hom(a_!(a^*M\otimes^{\mathbf L}P),L)=\Hom(a^*M,\cHom_S(P,a^!L))=\Hom(M,Ra_*\cHom_S(P,a^!L))$,
naturally in $M$, whence the first isomorphism by Yoneda. Since $P$ is a
locally constant perfect complex it is dualizable with dual $P^\vee$, and
$\cHom_S(P,-)\simeq P^\vee\otimes^{\mathbf L}-$.

*Membership.* $a^!L\in\Dctf(S,\Lambda)$, $P^\vee\otimes^{\mathbf L}a^!L\in\Dctf$
(tensor product with a perfect complex, which lies in $\Dctf$), and $Ra_*$
preserves $\Dctf$, all by [det-thm-sf-ctf-stability-direct-images]. Hence
$\cHom_X(a_!P,L)\in\Dctf(X,\Lambda)$, and finite cones and shifts give the
assertion for every $K$.
