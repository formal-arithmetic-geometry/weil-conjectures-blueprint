+++
kind = "proof"
of = "proposition-compactness-proper-direct-image"
order = 498
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "proposition-left-completeness", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "proposition-locally-constant-sheaves-finite-presentation", "definition-lisse-sheaves", "lemma-flat-models-generators", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "lemma-uniform-ext-bound", "definition-ind-constructible-sheaves", "proposition-ind-constructible-sheaves", "corollary-ind-heart-b", "corollary-ambient-ind-derived", "lemma-proper-direct-image-unbounded-complexes", "lemma-structure-integral-constructible-complexes", "proposition-forgetting-supports-composition", "proposition-six-operations-change-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
The rational proofs (Theorem [theorem-compactness-rational-coefficients],
Lemmas [lemma-reduction-finitely-many-degrees] and [lemma-proper-direct-image-unbounded-complexes])
go through once we supply for $\mathcal O_E$ the four inputs they use:
the abelian structure of Lemma [lemma-structure-integral-constructible-complexes](1),
continuity of $\Ext^i(C,-)$ for
bounded below systems, a bound $d_C$ with $\Ext^i(C,N)=0$ for $i>d_C$ and
$N$ constructible, and a bound on the amplitude of $Rp_*$.

For continuity, take $C=a_!L$ on a stratum. By
Lemma [lemma-sections-support-closed-subscheme](2), $R\!\operatorname{Hom}(a_!L,-)$ is
$R\Gamma(S,-)$ of the dual of $L$ tensored with
$u^*R\underline\Gamma_Z$. The proof of that formula uses only that $L$ is
dualizable, which holds by
Lemma [lemma-structure-integral-constructible-complexes](3), and so continuity follows from
Corollary [corollary-continuity-cohomology].

The bound $d_C$ comes from counting degrees as in
Lemma [lemma-uniform-ext-bound]. Namely, the reductions of $N$ lie in $[-1,0]$, and the dual of $L$ adds one degree. Next, the functors $R\Gamma$ and $R\underline\Gamma_Z$ add the cohomological dimensions of
Definition [definition-cohomological-dimension]. Finally, the derived limit over the reductions adds one more [Stacks, [08TB](https://stacks.math.columbia.edu/tag/08TB)].

The same count bounds $Rp_*$. For fibres of
dimension $\le d$, the torsion bound [Stacks, [095U](https://stacks.math.columbia.edu/tag/095U)] gives $2d$, and the
derived limit adds one. Hence $Rp_*$ of a constructible sheaf lies in
$[0,2d+1]$.
