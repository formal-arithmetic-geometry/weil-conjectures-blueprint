+++
kind = "proof"
of = "lemma-nearby-duality-slice"
order = 1685
uses = ["lemma-comparison-completed-coefficients", "definition-tate-twists", "definition-constructible-sheaves", "lemma-identity-pasting", "lemma-naturality-pasting-comparison", "definition-projection-formula-map", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-f-shriek-ell-adic-coefficients", "lemma-change-coefficients-compact-support", "lemma-change-coefficients-exceptional-inverse-image", "proposition-isomorphisms-reduce-finite-coefficients", "theorem-smooth-base-change-classical-torsion", "theorem-smooth-base-change-all-admissible", "lemma-kunneth-one-identity-factor", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "proposition-relative-dualizing-complex", "theorem-sp-qbar", "proposition-compatibility-purity-base-change", "definition-trace-map", "lemma-perfect-complexes-geometric-point", "lemma-internal-adjunction-two-exchange-formulas", "lemma-kunneth-formula-compact-supports", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "lemma-nearby-cycles-constant-family", "lemma-finite-support-global-sections", "lemma-kunneth-map-slice", "lemma-composition-exceptional-base-change-maps", "lemma-nearby-duality-proper-direct-image"]
+++
The map $\delta$ is the adjoint of the pairing
(E.12). By
Lemma [lemma-duality-invariants-pro-p] it therefore suffices to compare the
three arrows of this pairing with the corresponding arrows on the slice,
restricted to $P$-invariants.  Since the slicing formula comes from
factoring the inclusion of the geometric generic point and composing
the adjunctions for the direct images, the
lax monoidal map and the evaluation correspond under it to the maps on the
slice, restricted to $P$-invariants.

For the last arrow $\theta_X$, we claim
that under (E.2) and
(E.16), the map $g_s^*\theta_X$
corresponds to $(\theta_{X'})^P\otimes A(1)[2]$. We check
this on a smooth ambient space, where $\theta$ is the identity by smooth
purity, and descend along the closed immersion
$i:X\hookrightarrow\mathbf A^r_{\mathbf A^1_S}$ of the statement, which we abbreviate
to $i:X\hookrightarrow\mathbf A^r$. First, on $\mathbf A^r$ and on its slice, smooth
purity and the base change isomorphism of nearby cycles for smooth
pullback identify $\theta$ with the identity of the dualizing complex of
a smooth scheme, and these identifications differ by $A(1)[2]$. To descend to $X$, we use
the identity (E.9) for $i$, which gives
$\theta_X=i_s^!\theta_{\mathbf A^r}\circ\beta_i(\omega_{\mathbf A^r_\eta})$.
By (E.6), $\theta_X$ is then the adjoint,
for $Ri_{s*}\dashv i_s^!$, of $\nu_i$, followed by $\Psi$ of the
exceptional counit $Ri_{\eta*}i_\eta^!\to1$ and by
$\theta_{\mathbf A^r}$. Now the base change map $\nu_i$ for the proper map
$i$ and the factorization used for slicing commute with this counit,
because their ordinary adjoints are the same composite of the counit
for the open immersion of the generic fibre and the counit for $i$.
Since generic restriction is compatible with $i^!$ and with evaluation,
the claim for $\mathbf A^r$ gives it for $X$ before taking invariants.

It remains to pass to $P$-invariants. For a finite quotient $G$ of $P$,
the additive functor $i_{s'}^!$ commutes with the action of $G$, and so
it preserves the image of the averaging idempotent. Thus $i_{s'}^!$
commutes with $(-)^P$, and the same descent works after taking
$P$-invariants. Since the shift $[2]$ is even, no additional Koszul
sign appears.
