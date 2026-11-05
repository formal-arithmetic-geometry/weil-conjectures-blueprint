+++
kind = "proof"
of = "lemma-base-change-cone-x-z"
order = 1636
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "corollary-evaluation-weakly-contractible-objects", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-all-admissible", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian", "lemma-sheaves-finite-support-finite-morphisms"]
+++
Both the source and the target of $\tau$ are compatible with proper
direct image and smooth pullback, so the cone is as well. To prove the
vanishing on $i_*M$, we reduce to the pair $(Z,Z)$, where the
deformation is a constant family.

By Lemma [lemma-functoriality-deformation], $f$ induces a morphism
$\widetilde f$ of deformations, which is proper if $f$ is proper and
smooth if $f$ is smooth. To this morphism we apply the base change maps of
nearby cycles, together with proper or smooth base change for the
restriction to the zero section.  The resulting squares for
$\tau$ then commute because the base change map for pullback is compatible
with composition, and their cofibres give the two isomorphisms.
In the special case $f=i$, the source pair is $(Z,Z)$ and
$\mathcal D_ZZ=Z\times S$, so $\tau_{Z,Z}$ is the
inverse of the isomorphism of Lemma [lemma-nearby-cycles-constant-family].
Hence $C_{Z,Z}=0$, and since $i$ is proper, the first isomorphism gives
$C_{X,Z}(i_*M)=0$.
The last assertion then follows by applying the exact functor $C_{X,Z}$
to $j_!j^*L\to L\to i_*i^*L$.
