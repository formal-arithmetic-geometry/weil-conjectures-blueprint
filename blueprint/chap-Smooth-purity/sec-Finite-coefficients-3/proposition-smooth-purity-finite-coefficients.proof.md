+++
kind = "proof"
of = "proposition-smooth-purity-finite-coefficients"
order = 760
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-change-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
The calculation so far was made with coefficients $\mathbf Z/\ell^n\mathbf Z$,
and every ingredient in it extends along $\mathbf Z/\ell^n\mathbf Z\to A$,
where we choose $n$ with $\ell^nA=0$. Once the Kummer and diagonal classes are
extended, the calculation works with $A$ throughout. In particular, the splitting for the
projective line has two free summands, and its integration and triangle
identities keep the same normalization, since
(9.9) is an identity of endomorphisms of a
constant sheaf and is preserved by extension of scalars. So the local
adjunctions compute $f_A^!$, and the arguments for vector bundles and
deformations then show that $\omega_{f,A}\simeq A_X(d)[2d]$. We define $\gamma_{f,A}(K)$
as the composite

$$
f_A^{*}K\otimes^{\mathbf L}A_X(d)[2d]
\xrightarrow{\sim}f_A^{*}K\otimes^{\mathbf L}\omega_{f,A}
\xrightarrow{\sim}f_A^{!}K.
$$

These are the isomorphisms given by the orientation and by $\mu_{f,K}$,
and both are natural in $K$.
By (9.17) below, $\gamma_{f,A}$ does not depend
on the choice of $n$ and is compatible with maps of finite rings.
