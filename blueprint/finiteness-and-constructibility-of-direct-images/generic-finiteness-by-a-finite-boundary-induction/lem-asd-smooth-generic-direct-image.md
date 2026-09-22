+++
id = "lem-asd-smooth-generic-direct-image"
kind = "lemma"
title = "A smooth source with locally constant coefficients"
order = 5806
lean = ["AlgebraicGeometry.Etale.IsSmooth.exists_open_isLisse_derivedPushforward"]
uses = ["lem-fin-compact-bounded-and-base-change", "lem-fin-lisse-field-dual"]
+++
Let $S$ be integral and of finite type over a field $k$, let
$\ell\ne\operatorname{char}(k)$, let $f:X\to S$ be a separated smooth
morphism of finite type, and let $L$ be a finite locally constant
$\mathbf F_\ell$-sheaf. There is a nonempty open $U\subset S$ such that
$Rf_{U,*}L|_{X_U}$ is bounded with finite locally constant cohomology, and
for every $v:T\to U$ with Noetherian $T$ the ordinary base-change morphism
$$
v^*Rf_{U,*}L|_{X_U}\longrightarrow Rf_{T,*}L|_{X_T}
$$
is an isomorphism.

## Proof

Write $\lambda=\mathbf F_\ell$. The relative dimension is locally constant;
the finitely many occurring dimensions give a finite disjoint open
decomposition, so we may treat one dimension at a time.

Put $\omega_f=f^\times\lambda_S$. The ambient smooth theorem says that
$\omega_f$ is locally an invertible sheaf in degree $-2d$, and that
$f^\times M=\omega_f\otimes f^*M$; its compatibility with Noetherian base
change is the ambient base-change proposition. In particular
$N=L^\vee\otimes\omega_f$ is bounded constructible and the
finite-dimensional evaluation isomorphism gives
$R\mathcal Hom_X(N,\omega_f)=L$.

The internal adjunction proved on the ambient categories therefore
identifies
$$
Rf_*L=R\mathcal Hom_S(Rf_!N,\lambda_S).\tag{$\ast$}
$$
This invokes neither preservation of a constructible subcategory by $f^!$
nor ordinary direct-image finiteness.

By [lem-fin-compact-bounded-and-base-change], $C=Rf_!N$ is bounded
constructible. Each of its finitely many nonzero cohomology sheaves is
finite locally constant on some nonempty open of the integral scheme $S$:
take the stratum containing the generic point in the constructible
stratification, and then its open neighborhood. Intersect these finitely
many opens to obtain $U$. Apply [lem-fin-lisse-field-dual] to $C|_U$;
equation $(\ast)$ gives the claimed bounded locally constant cohomology.

For $v:T\to U$ with Noetherian $T$, the ambient smooth theorem identifies
$v_X^*N$ with the coefficient complex used for $f_T$. Compact-support base
change identifies $v^*C$ with $Rf_{T,!}v_X^*N$, and
[lem-fin-lisse-field-dual] permits pullback through its internal dual. Thus
the pullback of $(\ast)$ is the same isomorphism $(\ast)$ for $f_T$.
Naturality of internal adjunction with respect to its unit and counit
identifies this composite with the ordinary base-change morphism. Hence the
specified morphism, and not merely two abstract objects, is an isomorphism.
Intersect the opens obtained for the finitely many relative dimensions to
finish.

Unresolved dependencies: def:sbc-smooth-morphisms, def:weil-pbc-derived-categories, def:weil-pbc-constructible-complexes, sbc-def-base-change-map, thm:asd-smooth-tensor, prop:asd-smooth-base-change, prop:asd-internal-adjunction, sbc-lem-smooth-relative-dimension-locally-constant
