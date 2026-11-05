+++
kind = "proof"
of = "lemma-reciprocal-roots-zeta"
order = 1390
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "lemma-hankel-rank-rationality", "lemma-reduced-fractions-integer-coefficients", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
The identity (19.2) holds because both sides
are reduced fractions for $Z(X_0,T)$ over $\mathbf Q_\ell$. By
Corollary [corollary-purity-cohomology-smooth-proper-variety], the
reciprocal roots of $P_{i,\ell}$ have absolute value $q^{i/2}$ under
every embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. Since $q>1$,
distinct degrees give distinct absolute values, and so the polynomials
$P_{i,\ell}$ are pairwise coprime. Their products over odd and over
even degrees are therefore coprime, and they have constant coefficients
one. By (19.1) their quotient is
$Z(X_0,T)$. On the other hand, $A$ and $B$ remain coprime in
$\mathbf Q_\ell[T]$, since a Bézout relation over $\mathbf Q$ remains
valid over $\mathbf Q_\ell$. The two reduced fractions agree by the
uniqueness argument in the proof of
Lemma [lemma-reduced-fractions-integer-coefficients], which works
over any field.

Write $A(T)=\prod_a(1-aT)$ and $B(T)=\prod_b(1-bT)$ over
$\overline{\mathbf Q}$. The reciprocal roots $a$ and $b$ are roots of the
monic integral polynomials $U^{\deg A}A(U^{-1})$ and $U^{\deg B}B(U^{-1})$.
Hence they are nonzero algebraic integers. Let
$\theta:\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_\ell$ be an embedding, and
let $a$ be a reciprocal root of $A$ or $B$. By
(19.2) and the pairwise coprimality of the
$P_{i,\ell}$, there is exactly one $i$ such that $\theta(a)$ is a
Frobenius eigenvalue on $H^i_\ell$. It is odd for $A$ and even for $B$.

Corollary [corollary-purity-cohomology-smooth-proper-variety] bounds
$|\iota(\theta(a))|$ for embeddings $\iota$ of $\overline{\mathbf Q}_\ell$. The lemma,
however, concerns the embeddings of the number field $\mathbf Q(a)$. We
pass from one to the other by extending field embeddings. Let
$\tau:\mathbf Q(a)\hookrightarrow\mathbf C$ be any embedding. The map
$\tau\circ\theta^{-1}$, defined on $\theta(\mathbf Q(a))$, extends to a
field isomorphism $\iota':\overline{\mathbf Q}_\ell\xrightarrow{\sim}\mathbf C$, because both
are algebraically closed fields of characteristic zero with
transcendence degree $2^{\aleph_0}$ over $\mathbf Q$. We have
$\iota'(\theta(a))=\tau(a)$. Applying
Corollary [corollary-purity-cohomology-smooth-proper-variety] with this $\iota'$ to the
eigenvalue $\theta(a)$ on $H^i_\ell$, we find

$$
|\tau(a)|=q^{i/2}.
$$

Since $q>1$, this absolute value determines $i$, and so $i$ does not
depend on $\theta$.
