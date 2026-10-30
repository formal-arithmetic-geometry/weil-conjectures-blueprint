+++
kind  = "proof"
of    = "lem-asd-smooth-generic-direct-image"
+++
Write $\lambda=\mathbf F_\ell$. The relative dimension is
locally constant by
[sbc-lem-smooth-relative-dimension-locally-constant]; the
finitely many occurring dimensions give a finite disjoint open
decomposition, so we may treat one dimension at a time.
Put $\omega_f=f^\times\lambda_S$. The ambient smooth theorem
[thm-asd-smooth-tensor] says that $\omega_f$ is locally an
invertible sheaf in degree $-2d$, that
$f^\times M=\omega_f\otimes f^*M$. Its compatibility with
Noetherian base change is [prop-asd-smooth-base-change]. In particular
$N=L^\vee\otimes\omega_f$ is bounded constructible and the
finite-dimensional evaluation isomorphism gives

$$
R\mathcal Hom_X(N,\omega_f)=L.
$$

The internal adjunction proved on the ambient categories in
[prop-asd-internal-adjunction] therefore identifies

$$
Rf_*L
=R\mathcal Hom_S(Rf_!N,\lambda_S).
\tag{\(\ast\)}
$$

This invokes neither preservation of a constructible subcategory
by $f^!$ nor ordinary direct-image finiteness.

By [lem-fin-compact-bounded-and-base-change], $C=Rf_!N$
is bounded constructible. Each of its finitely many nonzero
cohomology sheaves is finite locally constant on some nonempty
open of the integral scheme $S$: take the stratum containing
the generic point in the constructible stratification of
[def-weil-pbc-constructible-complexes], and then its open
neighborhood. Intersect these finitely many opens to obtain $U$.
Apply [lem-fin-lisse-field-dual] to $C|_U$; equation
$(\ast)$ gives the claimed bounded locally constant cohomology.

For $v:T\to U$ with Noetherian $T$, the ambient smooth theorem identifies
$v_X^*N$ with the coefficient complex used for $f_T$.
Compact-support base change identifies
$v^*C$ with $Rf_{T,!}v_X^*N$, and
[lem-fin-lisse-field-dual] permits pullback through its
internal dual. Thus the pullback of $(\ast)$ is the same
isomorphism $(\ast)$ for $f_T$. Naturality of internal
adjunction with respect to its unit and counit identifies this
composite with the ordinary base-change morphism. Hence the
specified morphism, and not merely two abstract objects, is an
isomorphism. Intersect the opens obtained for the finitely many
relative dimensions to finish.
