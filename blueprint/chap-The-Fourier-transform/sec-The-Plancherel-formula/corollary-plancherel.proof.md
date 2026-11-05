+++
kind = "proof"
of = "corollary-plancherel"
order = 1239
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
As for the classical transform, the proof is by orthogonality of
characters. We expand the square of the sum in (16.3),
using that the complex conjugate of a character value is its inverse.
This writes the left side as a double sum over $x,z\in\mathbf F_{q^n}^r$
of $\iota t_{K,n}(x)\overline{\iota t_{K,n}(z)}$ times a character sum
over $y$, which we now compute.
For $x,z\in\mathbf F_{q^n}^r$, the orthogonality of characters gives

$$
\sum_y\iota\psi\bigl(\operatorname{Tr}\langle x-z,y\rangle\bigr)
=\begin{cases}q^{nr},&x=z,\\0,&x\ne z.\end{cases}
$$

Indeed, for $x\ne z$ the linear form
$y\mapsto\operatorname{Tr}_{\mathbf F_{q^n}/k_0}\langle x-z,y\rangle$ is
nonzero, since the trace pairing is nondegenerate, and hence
surjective onto $k_0$. As $\psi$ is nontrivial, there is $y_0$ with
$c=\psi(\operatorname{Tr}\langle x-z,y_0\rangle)\ne1$, and
substituting $y+y_0$ for $y$ multiplies the sum by $\iota(c)$, so the sum is zero.
Therefore only the diagonal terms remain, and they
give the asserted identity. On a line, finally, the factor $q^n$ raises
$\nu$ by one.
