+++
kind  = "proof"
of    = "thm-coef-integral-verdier"
+++
The dualizing object and its reductions are
[prop-coef-integral-dualizing]. Apply
[lem-coef-integral-hom-reduction]; it proves both displayed
identifications and completeness of the ambient internal Hom.
By [lem-coef-integral-residue-tor], all input reductions are
finite-Tor constructible. The finite bound
[lem-weil-verdier-preservation-strata] and the comparison
[lem-weil-finite-duality-site-comparison] prove constructibility
and the uniform interval stated for every reduction of the output.
This establishes preservation in the actual integral category.

Apply the internal-Hom comparison twice. Its evaluation
compatibility identifies the reduction of $\delta_K$, defined by
the tensor–Hom evaluation as in [lem-weil-duality-pairing],
with the canonical finite double-dual map. Those maps are
isomorphisms by [thm-fix-general-biduality].
The cone of $\delta_K$ is derived complete
([sk-def-pe-derived-completion]) and all its reductions are zero, so it is zero
by derived Nakayama ([sk-lem-pe-derived-nakayama]).
Thus $\delta_K$ is an isomorphism. The evaluation identity
$D_{X,R}(\delta_K)\circ\delta_{D_{X,R}K}=\operatorname{id}$
shows that these natural isomorphisms exhibit the stated
anti-equivalence. The argument proves a property of ambient
internal Hom, not a replacement definition of that functor.
