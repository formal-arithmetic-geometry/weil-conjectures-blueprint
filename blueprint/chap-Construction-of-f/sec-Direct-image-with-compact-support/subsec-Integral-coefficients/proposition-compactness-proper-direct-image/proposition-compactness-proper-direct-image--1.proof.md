+++
kind = "proof"
of = "proposition-compactness-proper-direct-image--1"
order = 497002
uses = ["proposition-pro-etale-affines-form-basis", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-uniform-ext-bound", "proposition-ind-constructible-sheaves", "corollary-ind-heart-b", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "definition-weak-contractibility--1", "proposition-left-completeness--1", "corollary-continuity-cohomology--1", "corollary-continuity-cohomology--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-flat-models-generators--1", "definition-underived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--3", "definition-ind-constructible-sheaves--1", "proposition-ind-constructible-sheaves--4", "proposition-ind-constructible-sheaves--5", "proposition-ind-constructible-sheaves--6", "corollary-ambient-ind-derived--1", "corollary-ambient-ind-derived--2", "proposition-comparison-etale-derived-category--5", "lemma-structure-integral-constructible-complexes--1", "lemma-structure-integral-constructible-complexes--3", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
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
Lemma [lemma-uniform-ext-bound]. The reductions of $N$ lie
in $[-1,0]$, and the dual of $L$ adds one degree. The functors $R\Gamma$ and
$R\underline\Gamma_Z$ add the cohomological dimensions of
Definition [definition-cohomological-dimension]. The derived limit over the reductions adds
one more [Stacks, [08TB](https://stacks.math.columbia.edu/tag/08TB)].

*Source:* the proof of Proposition [proposition-compactness-proper-direct-image].
