+++
kind = "proof"
of = "det-sf-open-closed-sequence-ring-sheaf"
uses = ["lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-fully-faithful", "lem-exc-proetale-open-unit", "lem-weil-extension-by-zero-exact", "lem-weil-extension-by-zero-adjunction", "lem-exc-closed-localization", "lem-exc-closed-cover-extension", "det-sf-open-closed-pullback-limits", "lem-exc-open-closed-detection"]
+++
All functors involved send a module over the relevant sheaf of rings to a
module over its inverse or direct image, and on underlying abelian sheaves
they are the functors of abelian sheaves; exactness, the unit and counit
maps and the vanishing statements can therefore be checked on underlying
abelian sheaves. The proofs of the finite-coefficient lemmas cited below
never use the coefficients: they only manipulate sections on the affine
ind-étale bases, so they apply verbatim to abelian sheaves.

*(1)* $j^*$ is restriction to the open $U_{\mathrm{proét}}=X_{\mathrm{proét}}/U$,
which is exact. $j_!$ is the sheafification of extension by zero; it is left
adjoint to $j^*$ ([lem-weil-extension-by-zero-adjunction]), exact
([lem-weil-extension-by-zero-exact]), and its unit is an isomorphism
([lem-exc-proetale-open-unit]): for $W\to X$ factoring through $U$ the
presheaf extension by zero already has value $N(W)$.

*(2)* Exactness of $i_*$ is [lem-exc-proetale-closed-exact]: a section of
$i_*H$ on a basis object $W$ is a section of $H$ on $Z_W=W\times_XZ$; it lifts
to $G$ on a finite affine ind-étale covering of $Z_W$, which extends, by the
henselian lifts of [lem-exc-closed-cover-extension], to a covering of $W$
whose remaining members lie over $U$, where the section is zero. This uses
that $W\setminus Z_W$ is quasi-compact, i.e. that $j$ is quasi-compact. The
counit $i^*i_*G\to G$ is an isomorphism by
[lem-exc-proetale-closed-fully-faithful]; evaluating on a weakly
contractible $V$ with (1) of [det-sf-open-closed-pullback-limits] gives
$(i^*i_*G)(V)=G(v(V)\times_XZ)=G(V)$. Finally $j^*i_*G=0$ because for $W$
over $U$ the fibre product $W\times_XZ$ is empty and $G(\emptyset)=0$.

*(3)* The composite $j_!j^*M\to M\to i_*i^*M$ is zero, since by adjunction it
corresponds to a map $j^*M\to j^*i_*i^*M=0$. The pair $(j^*,i^*)$ is
jointly conservative on abelian sheaves: if $j^*F=0$ and $i^*F=0$, a section
$s\in F(W)$ on a basis object becomes zero on a covering of $Z_W$ by henselian
lifts and is zero on the open members over $U$, so $s=0$ by the sheaf axiom
([lem-exc-open-closed-detection]). Since $j^*$ and $i^*$ are
exact, the sequence is exact as soon as its images under $j^*$ and $i^*$ are.
Under $j^*$ it becomes $0\to j^*M\xrightarrow{\sim}j^*M\to0\to0$ by (1),(2)
and the triangle identity for $j_!\dashv j^*$. Under $i^*$ its first term is
$i^*j_!j^*M=0$ (sections of $j_!N$ on a henselian lift $v(V)$ vanish, because
$v(V)$ does not factor through $U$ unless $V=\emptyset$, and these values
compute $i^*$ by [det-sf-open-closed-pullback-limits]), and the map
$i^*M\to i^*i_*i^*M$ is inverse to the counit isomorphism of (2) by the
triangle identity. So both restricted sequences are exact.

*(4)* For $g:X'\to X$, both $g^*j_!$ and $j'_!g_U^*$ are left adjoint to
$g_{U*}j'^*=j^*g_*$, so they agree canonically. For the closed part,
$g^*i_*G\to i'_*g_Z^*G$ is the base-change map; it is an isomorphism after
$j'^*$ (both sides vanish by (2)) and after $i'^*$, where both sides become
$g_Z^*G$ by the counit isomorphism of (2) and
[lem-exc-closed-localization]; by joint conservativity it is an isomorphism.
The functor $g^*$ is exact and commutes with the counit and unit maps of (3)
under these identifications, so it carries the sequence for $M$ to that for
$g^*M$.
