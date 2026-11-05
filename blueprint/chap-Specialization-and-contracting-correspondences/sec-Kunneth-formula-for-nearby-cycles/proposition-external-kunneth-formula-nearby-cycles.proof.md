+++
kind = "proof"
of = "proposition-external-kunneth-formula-nearby-cycles"
order = 1659
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "definition-derived-adic-completeness", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "corollary-open-direct-image-over-field", "proposition-open-direct-image-preserves-finite", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-degree-zero-calculation", "lemma-injectivity-base-change-map-degree", "lemma-reduction-field", "lemma-integral-changes-source-base", "lemma-change-coefficients", "lemma-base-change-along-product-projection", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms", "lemma-kunneth-map-proper-direct-image", "lemma-finite-support-global-sections", "lemma-kunneth-map-slice"]
+++
We argue by induction on
$n=\dim(X_{\bar\eta}\times_{\bar\eta}Y_{\bar\eta})$, simultaneously for
all such traits.  Before slicing we need two reductions: global sections require proper families, and
bounding fibre dimensions after slicing requires flatness, so we
arrange both.  For properness, note first that the assertion is local on $X_s\times_kY_s$.  We may therefore pass to
affine neighbourhoods of the two factors, take projective closures
over $S$ and extend the coefficients by zero on their generic fibres.
By the base change isomorphism for nearby cycles along open immersions,
the restriction of the new map is the original map, so we may assume
that $X$ and $Y$ are projective.  For flatness, the base change isomorphism for
the closed immersions of the closures of their generic fibres, together with
invariance under nilpotent thickenings, lets us also assume that they are
reduced with dense generic fibres, hence flat
over the trait.  Moreover, none of these reductions increases $n$.

Let $Q$ be the cone of (E.4). For proper
families, global sections of nearby cycles on the special fibre are
cohomology of the geometric generic fibre, so by the base change
isomorphism for the proper structure maps and
Lemma [lemma-kunneth-map-proper-direct-image], the map of global
complexes induced by $\Pi_{L,M}$ is the ordinary Künneth isomorphism

$$
R\Gamma(X_{\bar\eta},L)\otimes_A^{\mathbf L}
R\Gamma(Y_{\bar\eta},M)
\xrightarrow{\sim}
R\Gamma(X_{\bar\eta}\times Y_{\bar\eta},L\boxtimes M),
$$

and therefore

$$
R\Gamma(X_s\times_kY_s,Q)=0.
\tag{E.5}
$$

By Lemma [lemma-finite-support-global-sections], $Q=0$ as soon as
$Q$ has finite support.  When $n=0$, the special fibres are
zero-dimensional by flatness, so the support is finite. Let $n>0$.
By Lemma [lemma-quasi-finite-coordinates], $X_s\times_kY_s$ is
covered by finitely many products $V_s\times W_s$ of open subschemes
with quasi-finite maps $b:V\to\mathbf A^q_S$ and $c:W\to\mathbf A^r_S$,
where $q+r\leq n$ and $\dim V_{\bar\eta}\leq q$,
$\dim W_{\bar\eta}\leq r$. The restriction of $Q$ to $V_s\times W_s$ is
the cone of $\Pi_{L|_V,M|_W}$. If $q+r<n$, it vanishes by the induction
hypothesis. By symmetry we may therefore
assume $q+r=n$ and $q>0$, and compose $b$ with one of
the coordinate projections $\mathbf A^q_S\to\mathbf A^1_S$. In the
notation of Lemma [lemma-kunneth-map-slice] for $V$, $W$ and this
map, the map $V'\to\mathbf A^q_S\times_{\mathbf A^1_S}S'=\mathbf
A^{q-1}_{S'}$ is a base change of $b$, hence quasi-finite, and
therefore

$$
\dim V'_{\bar\eta'}\leq q-1,\qquad
\dim W'_{\bar\eta'}\leq r.
$$

By the induction hypothesis $\Pi_{L',M'}$ is an isomorphism. By
Lemma [lemma-kunneth-map-slice], the restriction of $Q$ over $s'$
is therefore zero. In other words, the support of $Q$ has no point over
the generic point of this coordinate line in the special fibre. Its
image in that line is constructible and does not contain the generic
point, so it is a finite set of closed points.

We repeat this argument for each of the $q$ coordinates of $b$. After
interchanging the factors, we do the same for each of the $r$
coordinates of $c$; the analogue of Lemma [lemma-kunneth-map-slice]
with the roles of $X$ and $Y$ exchanged holds by symmetry of
$\boxtimes$. The support of $Q$ on $V_s\times W_s$ is then contained in
the inverse image under $b_s\times c_s$ of a finite set. This inverse
image is finite, because $b_s\times c_s$ is quasi-finite. With finite
support, (E.5) and
Lemma [lemma-finite-support-global-sections] show that $Q=0$.
