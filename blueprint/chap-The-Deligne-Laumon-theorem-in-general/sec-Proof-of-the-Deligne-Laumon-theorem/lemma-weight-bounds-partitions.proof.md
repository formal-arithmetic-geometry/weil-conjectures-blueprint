+++
kind = "proof"
of = "lemma-weight-bounds-partitions"
order = 1356
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
In both cases the restrictions of $K$ are again mixed of weights at
most $w$ (Proposition [proposition-weights-under-usual-operations]),
and we place $R^qf_!K$ in the middle of an exact sequence of Weil
sheaves whose outer terms are bounded.

For (1), applying $Rf_!$ and the composition isomorphism to the
triangle $j_!j^*K\to K\to i_*i^*K\to$ gives an exact sequence

$$
R^q(fj)_!j^*K\longrightarrow R^qf_!K\longrightarrow R^q(fi)_!i^*K,
$$

which is Frobenius-equivariant by naturality, and
Lemma [lemma-weights-exact-sequence] gives the bound for
$R^qf_!K$.

For (2), let $j':V_0\to Y_0$ and $i':W_0\to Y_0$ be the inclusions.
Base change for direct images with compact support
(Proposition [proposition-composition-base-change-rf-shriek])
identifies $j'^*R^qf_!K$ with $R^qf_{V!}(K|_{f^{-1}V_0})$ and
$i'^*R^qf_!K$ with $R^qf_{W!}(K|_{f^{-1}W_0})$. By
Lemma [lemma-finite-quasi-finite-direct-images], the outer terms of

$$
0\longrightarrow j'_!j'^*R^qf_!K\longrightarrow R^qf_!K
\longrightarrow i'_*i'^*R^qf_!K\longrightarrow0
$$

are mixed of weights at most $w+q$, and
Lemma [lemma-weights-exact-sequence] gives the bound for the
middle term.
