+++
kind = "proof"
of = "lemma-case-z-v-x-m"
order = 1639
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "proposition-inverting-ell", "definition-pro-etale-base-change-map", "lemma-completed-ordinary-base-change", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-all-admissible", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-nearby-cycles-constant-family"]
+++
We give a homotopy argument. The contraction $x\mapsto ax$ joins the identity
($a=1$) to a map that factors through $Z$ ($a=0$), and the endomorphisms of
$z^*\operatorname{Sp}_{X,Z}(M_X)$ that these maps induce form a family
over $\mathbf A^1$. Since $\mathbf A^1$ has the
cohomology of a point, the family is constant, and comparing its two
ends shows that $\tau_{X,Z}(M_X)$ has an inverse.

Consider the contraction $h:X\times\mathbf A^1\to X$, $h(x,a)=ax$,
and write $h_a=h(-,a):X\to X$ for $a\in k$.  It maps
$Z\times\mathbf A^1$ schematically into $Z$, since
$h^*(x^m)=a^m x^m\in(x^m)$, and by Lemma [lemma-functoriality-deformation],
whose hypothesis is this inclusion of ideals, all $h_a$ lift to the
deformations.  Moreover, $h_1=\operatorname{id}$, and $h_0$ factors
through $Z$ and restricts to the identity on $Z_{\mathrm{red}}$.  Set $N=z^*\operatorname{Sp}_{X,Z}(M_X)$.
The base change maps for pullback along these lifts induce endomorphisms
$\phi_a:N\to N$, with $\phi_1=\operatorname{id}_N$.

There is one endomorphism $\phi$ of the pullback of $N$ to
$Z\times\mathbf A^1$ whose fibre at $a$ is $\phi_a$.  To construct it,
we apply the base change map for pullback along $h:X\times\mathbf A^1\to X$
and then invert the base change map for the projection to $X$, which is
smooth; by flat base change, the deformation of
$X\times\mathbf A^1$ is $\mathcal D_ZX\times\mathbf A^1$.  The restrictions of $h$ and
of the projection to $Z\times\mathbf A^1$ induce the same map to $Z$ on
reduced schemes, so invariance under nilpotent thickenings identifies
$h_Z^*N$ with $\operatorname{pr}_Z^*N$, naturally in $N$, and we may
view the family as an endomorphism of a
single pullback.  By compatibility with composition, its fibres are the
endomorphisms $\phi_a$ constructed above.

The family $\phi$ is constant; this is the
algebraic form of homotopy invariance.
Since $Z_{\mathrm{red}}$ is a point, invariance under nilpotent
thickenings identifies $D^b_c(Z_{\acute et},A)$ with the bounded derived
category of finite $A$-modules.  Pullback along the projection
$p:Z\times\mathbf A^1\to Z$ is fully faithful on this category.
Indeed, the calculation for the affine line and the hypercohomology
spectral sequence show that $R\Gamma(\mathbf A^1,p^*B)=B$ for every such
bounded complex $B$, and full faithfulness follows by adjunction.
Thus $\phi$ is the pullback of a single endomorphism of $N$. Its two
restrictions $\phi_0$ and $\phi_1$ therefore coincide, and
$\phi_0=\operatorname{id}_N$.

Because $h_0$ factors through $Z$, we can also express $\phi_0$ in
terms of $\tau_{X,Z}(M_X)$.  Let
$\alpha:M_Z\to N$ be the restriction of the unit of nearby cycles for
the constant sheaf on $\mathcal D_ZX$.  By naturality, and since $h_0$
factors as $X\to Z\hookrightarrow X$, we get

$$
\phi_0=\alpha\tau_{X,Z}(M_X),\qquad
\tau_{X,Z}(M_X)\alpha=\operatorname{id}_{M_Z}.
$$

The second equality holds because the composite is the specialization
map for the constant family $Z\times S$, followed by its fixed inverse.  Since
$\phi_0=\phi_1=\operatorname{id}_N$, the maps $\alpha$ and
$\tau_{X,Z}(M_X)$ are inverse isomorphisms.
