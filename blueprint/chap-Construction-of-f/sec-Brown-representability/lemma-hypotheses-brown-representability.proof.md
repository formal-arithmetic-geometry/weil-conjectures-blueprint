+++
kind = "proof"
of = "lemma-hypotheses-brown-representability"
order = 524
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-left-completeness", "corollary-continuity-cohomology", "definition-classical-pro-etale-sheaves", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-uniform-bounds-pro-etale-affines", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-local-cohomology", "lemma-local-cohomology-right-adjoint", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "corollary-coefficient-heart-b", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "lemma-cohomology-modules-underlying-abelian", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-uniform-ext-bound", "definition-ind-constructible-sheaves", "proposition-ind-constructible-sheaves", "corollary-ind-heart-b", "corollary-ambient-ind-derived", "theorem-compactness-rational-coefficients", "proposition-compactness-finite-coefficients", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "proposition-compactness-proper-direct-image", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
The set-theoretic conditions are general facts about derived categories
of Grothendieck abelian categories. Compactness, on the other hand, was proved separately for each kind of coefficients, and generation follows from the
definition of the localizing category.

As the derived category of a Grothendieck abelian category of module
sheaves, the ambient category is locally small, and so is its
full subcategory $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$. Moreover, the latter has direct sums by definition, so its idempotents split [Stacks, [05QW](https://stacks.math.columbia.edu/tag/05QW)]. Finally, the subcategory $D^b_{\mathrm{ctf}}(X,\Lambda)$ is thick, since constructibility and finite Tor
amplitude are preserved by shifts, cones and direct summands.

To see that $D^b_{\mathrm{ctf}}(X,\Lambda)$ is essentially small, note first that the
constructible sheaves in the heart have a set of representatives for each
admissible $\Lambda$. A bounded complex with such cohomology is built from its
cohomology sheaves by finitely many extensions, formed with truncations
in the ambient category. Each extension step is classified by an
element of a Hom set of the ambient category, and these Hom sets are
sets because the ambient category is locally small. Hence these
complexes form an essentially small category, of which
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is a full subcategory.

Compactness for finite $A$ is Proposition [proposition-compactness-finite-coefficients].
For $E$ and $\overline{\mathbf Q}_\ell$ it is
Theorem [theorem-compactness-rational-coefficients], and for $\mathcal O_E$
it is Proposition [proposition-compactness-proper-direct-image]; in the integral and rational cases,
$D^b_{\mathrm{ctf}}=\Dbc$.

For generation, suppose that $K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ receives no
nonzero maps from shifts of objects of a small skeleton. The objects
$M$ with $\Hom(M[n],K)=0$ for all $n$ form a localizing subcategory
containing $D^b_{\mathrm{ctf}}$. Hence this subcategory contains $K$. Then $\mathrm{id}_K=0$, and so $K=0$.
