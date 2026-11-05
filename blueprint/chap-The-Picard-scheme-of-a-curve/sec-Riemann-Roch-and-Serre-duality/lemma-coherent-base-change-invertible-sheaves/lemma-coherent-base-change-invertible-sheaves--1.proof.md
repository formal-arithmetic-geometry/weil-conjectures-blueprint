+++
kind = "proof"
of = "lemma-coherent-base-change-invertible-sheaves--1"
order = 1530004
uses = ["definition-constructible-sheaves", "lemma-acyclic-resolutions", "lemma-perfect-complexes-geometric-point", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form"]
+++
The construction first descends the proper morphism and the finitely
presented relatively flat module to a Noetherian affine base. A finite
affine cover gives a bounded flat Čech complex $C^\bullet$ computing
the higher direct images after every base change. Proper cohomology
finiteness, proved by an integral-ideal filtration and a Chow modification,
makes its cohomology finite over the Noetherian base. The algebraic
finite-Tor-amplitude criterion
`DerivedCategory.isPerfect_of_finiteTorAmplitude` then gives a
bounded-above finite free resolution $Q^\bullet\to C^\bullet$.
Pulling this model and its resolution back gives
`AlgebraicGeometry.Scheme.Modules.exists_proper_flat_cech_model`.

Now apply
`AlgebraicGeometry.Scheme.Modules.exists_local_finiteFree_shortening`.
The module $\operatorname{coker}(Q^{-1}\to Q^0)$ is finitely presented
and flat, since the resolution has no negative cohomology after tensoring.
It is therefore finite projective and becomes free near $t$. Replace
the negative tail of $Q^\bullet$ by this module in degree zero to obtain
$P^\bullet$, bounded in $[0,d]$. The comparison with $C^\bullet$
remains a quasi-isomorphism after pullback because the complexes are
K-flat. Composing the resulting cohomology isomorphisms with the Čech
comparisons proves the assertion. The specialization to an invertible
module uses `AlgebraicGeometry.Scheme.Modules.isFlatOver_of_isInvertible`.
