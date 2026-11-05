+++
kind = "proof"
of = "lemma-fourier-transform-boundary-sequence"
order = 1274
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "theorem-trace-formula-euler-product", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-finite-quasi-finite-direct-images", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The three assertions are of different kinds. That the transform
of $j_!M$ is a single sheaf is a vanishing statement for the
cohomology of the twisted sheaves $M\otimes\mathcal L_{\psi(yx)}$ on
$U$, whereas the exact sequence comes from transforming the boundary sequence
$0\to j_!M\to j_*M\to B\to0$ term by term. Finally, the
bound on $B'$ comes from the stalks of $B$, which are known from
Proposition [proposition-weights-j-boundary-points].

For $G$, the stalk formula
of Proposition [proposition-base-change-fourier-inversion] says that
the stalk of $\operatorname{FT}_\psi(j_!M)$ at $y$ is
$R\Gamma_c(U,M\otimes\mathcal L_{\psi(yx)})[1]$, so we must show that
only $H^1_c$ is nonzero. We apply
Lemma [lemma-extreme-degrees-affine-curve] to the lisse
sheaf $M\otimes\mathcal L_{\psi(yx)}$ on the affine curve $U$, with $j$
the identity. It shows that the group in degree zero vanishes and that
the group in degree two is a twist of
the coinvariants of geometric monodromy on
$M\otimes\mathcal L_{\psi(yx)}$. But a nonzero coinvariant would be a
geometric quotient of $M$ isomorphic to $\mathcal L_{\psi(-yx)}$, and
our assumption on $M$ excludes such a constituent, so
the group in degree two vanishes as well. The shift then places the
remaining group $H^1_c$ in degree zero, and the transform is a sheaf
$G$.

The transform of $B$ is computed point by point. After geometric base
change, the punctual sheaf
$B$ is a finite sum of skyscrapers with coefficient modules, and the
transform of each skyscraper is a linear character sheaf tensored with
that module and shifted by one. Since a linear character sheaf is lisse
on the whole dual line, $\operatorname{FT}_\psi(B)=B'[1]$ with $B'$ lisse.

Applying the Fourier transform to the triangle obtained from
$0\to j_!M\to j_*M\to B\to0$, and using
Proposition [proposition-fourier-transform-middle-extension] for the
middle term, we obtain a triangle
$G\to j'_*M'\to B'[1]\to$. Here $G$ and $j'_*M'$ are sheaves in degree
zero, and $B'[1]$ is a sheaf in degree $-1$. Hence the long exact
sequence of cohomology sheaves has only three nonzero terms, and it is
the stated exact sequence.

The weights of $B'$ come from those of $B$, because a character sheaf has
weight zero, and the weights of $B$ are at most $w$ by
Proposition [proposition-weights-j-boundary-points]. Only at boundary
points that are not rational does this need an argument. So let $s$ be a
boundary point of
degree $d$ and $y$ a rational point of the dual line. The geometric
points over $s$ contribute $d$ summands to $B'_{\bar y}$, which
$\operatorname{Frob}_y$ permutes cyclically, and its $d$th power acts
on one summand as $\operatorname{Frob}_s$ on $B_{\bar s}$ times a root
of unity coming from the character sheaf. Every eigenvalue
$\beta$ of $\operatorname{Frob}_y$ on these summands therefore satisfies
$\beta^d=\zeta\alpha$, with $\zeta$ a root of unity and $\alpha$ an
eigenvalue of $\operatorname{Frob}_s$. Since
$|\iota\alpha|\le q^{dw/2}$, we get $|\iota\beta|\le q^{w/2}$.
At a point $y$ of higher degree we replace $q$ by the cardinality of
$\kappa(y)$.

For a filtration of $B'$ with pure quotients, choose for each boundary
point, over its
residue field, a Frobenius-stable full flag of the coefficient module,
which exists because $\overline{\mathbf Q}_\ell$ is algebraically closed. Each successive
quotient is then a line, on which Frobenius acts by one of its eigenvalues.
Tensoring with the linear character sheaves and summing over the
Frobenius orbit, we
obtain a finite Weil filtration of $B'$ whose quotients are pure of
the weights of the coefficient eigenvalues, and these weights are at
most $w$.
