+++
kind = "proof"
of = "proposition-compatibility-purity-base-change"
order = 799
uses = ["definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "theorem-existence-contractible-covers", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-descent-finite-coefficient-field", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-comparison-etale-derived-category", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-compact-support", "lemma-change-coefficients-exceptional-inverse-image", "proposition-six-operations-change-coefficients", "proposition-isomorphisms-reduce-finite-coefficients", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
The map $\gamma_f$ has two factors, the orientation of $\omega_f$ and the
map $\mu_{f,K}$, and we show that each commutes with base
change. For the orientation this is a local statement about rank one
sheaves, and it follows from the naturality of the deformation to the
normal bundle. For $\mu_{f,K}$ we compare transposes under the
adjunction for $f'$.

For a finite ring $A$ we compare the orientations and the maps
$\mu_{f,K}$ directly with coefficients in $A$, and for
$\mathcal O_E$ we compare the maps on towers $\gamma_{f,\bullet}$ of
(9.19) and apply $R\varprojlim$. The cases $E$ and
$\overline{\mathbf Q}_\ell$ follow, since
$\gamma_{f,E}$ and $\gamma_{f,\overline{\mathbf Q}_\ell}$ are obtained from
$\gamma_{f,\mathcal O_E}$ by inverting $\ell$ and by extension of scalars from
a finite extension of $\mathbf Q_\ell$.
We write out the calculation for towers; dropping the index $\bullet$
gives the calculation at finite level. There the map $\gamma_{f,\bullet}$ is the composite of
the orientation
$(\mathcal O_{E,X}/\ell^\bullet)(d)[2d]\xrightarrow{\sim}\omega_{f,\bullet}$
and the map
$f_\bullet^*K_\bullet\otimes\omega_{f,\bullet}\to f_\bullet^!K_\bullet$
for $K_\bullet=\operatorname{red}_YK$.

*Orientation.* After removing the shift $[2d]$, the two orientations
to be compared are maps between sheaves of towers of rank one in degree
zero. Since maps between sheaves form a sheaf, and a map of sheaves of towers is
a compatible family of maps of sheaves, equality may be tested
locally on $X'$ and at each level $n$. At a fixed level, the diagonal, its
normal bundle, the deformation to the normal bundle and the trace map of
vector bundles all commute with base change
(Lemma [lemma-naturality-under-base-change-etale](1)), and therefore so
does the orientation built from them.

*The map $f^*K\otimes\omega_f\to f^!K$.* This factor is not a map of
sheaves, so we cannot compare the two maps locally. However, a map into
$f'^!_\bullet g^*K_\bullet$ is determined by its transpose under the adjunction
on towers for $f'$. By the definition of $e_{f,\bullet}$, the transpose of the
pulled-back map $\mu_{f,K}$ for $f$ is the pulled-back counit
for $f$, preceded by
the map of the projection formula. Since the projection formula is natural
under pullback, the transpose of the map for $f'$ is the same
composite, as in the counit calculation in the proof of
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3), carried out with towers.
