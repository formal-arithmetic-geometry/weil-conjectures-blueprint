+++
kind  = "proof"
of = "det-def-sfb-derived-tensor-hom"
uses = ["det-def-sfb-derived-categories", "det-prop-sfb-module-category", "lem-sfb-derived-monoidal", "lem-sfb-derived-monoidal-closed", "def-weil-derived-tensor", "lem-sfb-derived-tensor-sheaves-derived", "def-sfb-derived-hom-sheaves", "def-sfb-derived-tensor-hom-adjunction-sheaves", "def-sfb-derived-tensor-modules", "lem-sfb-derived-tensor-modules-derived", "def-sfb-derived-hom-modules", "def-sfb-derived-tensor-hom-adjunction-modules"]
+++
A closed symmetric monoidal Grothendieck abelian category with functorial flat
resolutions has a monoidal derived category for the K-flat derived tensor product
[lem-sfb-derived-monoidal], and this derived category is closed
[lem-sfb-derived-monoidal-closed]. Both categories of coefficients are of this kind. For
$\Sh(X_{\mathrm{proét}},\mathcal A)$ this is the last paragraph of the proof of
[det-def-sfb-derived-categories]. For $\Mod_{\Lambda_X}$ it is
[det-prop-sfb-module-category]; $\Lambda_X$ is commutative because $\Lambda$ is.

For layer A, the derived tensor product is [def-weil-derived-tensor]. It is the
two-variable left derived functor of the tensor product by
[lem-sfb-derived-tensor-sheaves-derived]. The derived hom is [def-sfb-derived-hom-sheaves],
with its adjunction [def-sfb-derived-tensor-hom-adjunction-sheaves].

For layer B, these are [def-sfb-derived-tensor-modules],
[lem-sfb-derived-tensor-modules-derived], [def-sfb-derived-hom-modules] and
[def-sfb-derived-tensor-hom-adjunction-modules].
