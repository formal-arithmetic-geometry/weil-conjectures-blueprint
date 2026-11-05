+++
kind = "proof"
of = "proposition-function-sheaf-dictionary"
order = 1030
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "lemma-flat-models-generators", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "proposition-ordinary-external-kunneth", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-frobenius-operator", "definition-correspondence", "lemma-local-terms-point", "theorem-proper-pushforward-lefschetz-verdier", "proposition-additivity-trace-classes", "lemma-scheme-frobenius-geometric-frobenius", "lemma-local-term-restriction-map", "lemma-vanishing-restrictions-after-blowing-up", "lemma-covers-degree-prime-to-ell", "lemma-tangent-cones-on-cover", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Part (5) is Theorem [theorem-grothendieck-lefschetz-trace-formula] and part (3)
is Corollary [corollary-trace-functions-direct-image-compact].

For (1), the stalk of $g^*K$ at $\bar w$ is $K_{\bar x}$ with $x=g_0(w)$, and
the Weil structure of $g^*K$ is $g^*\phi$ composed with the base change
isomorphism. Under this identification of stalks the $m$-th iterate of the
Weil structure of $g^*K$ at $\bar w$ is the $m$-th iterate of $\phi$ at
$\bar x$, so the two Frobenius endomorphisms agree.

For (2), the stalk of $K\otimes^{\mathbf L}_\Lambda L$ at $\bar x$ is
$K_{\bar x}\otimes^{\mathbf L}_\Lambda L_{\bar x}$, since pullback to
$\bar x$ commutes with derived tensor products, and its Frobenius is the
tensor product of the two Frobenius endomorphisms. These stalks are perfect (Lemma [lemma-perfect-complexes-geometric-point]), so we may represent them by
bounded complexes $P$, $Q$ of finite projective modules and the endomorphisms by
chain maps $v$, $w$. Now the term of degree $n$ of $P\otimes Q$ is
$\bigoplus_{i+j=n}P^i\otimes Q^j$, the trace of $v^i\otimes w^j$ on
$P^i\otimes Q^j$ is $\operatorname{Tr}(v^i)\operatorname{Tr}(w^j)$, and
$(-1)^n=(-1)^i(-1)^j$. By the chain formula of
Proposition [proposition-properties-trace] the trace on $P\otimes Q$ is
therefore the product of the traces on $P$ and on $Q$.

For (4), note that $j_!=Rj_!$ and $i_*=Ri_!$, with the same Weil structures.
By (3), $t_{j_!j^*K,m}(x)$ is the sum of $t_{j^*K,m}$ over the fibre of $j_0$
at $x$. This fibre is the point $x$ if $x\in U_0$, and it is empty otherwise.
By (1), $t_{j^*K,m}(x)=t_{K,m}(x)$ for $x\in U_0(\mathbf F_{q^m})$. The same
argument applies to $i_*i^*K$, and the two functions add up to $t_{K,m}$.
