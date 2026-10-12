+++
kind  = "proof"
of    = "sk-prop-sfb-module-category"
+++
Faithfulness is [lem-sfb-modobj-forget-faithful].

Part 1. Kernels and cokernels are computed in $\mathcal C$ by
[lem-sfb-modobj-kernels] and [lem-sfb-modobj-cokernels]. The category is abelian by
[lem-sfb-modobj-abelian]. The forgetful functor is left exact by
[lem-sfb-modobj-forget-left-exact] and right exact by
[lem-sfb-modobj-forget-right-exact].

Part 2. Module objects are the symmetric bimodules by
[lem-sfb-modobj-symmetric-bimodules] and [def-sfb-symmetric-bimod-module-iso]. Symmetric bimodules are stable under the tensor
product of bimodules by [lem-sfb-symmetric-bimod-tensor]. The monoidal structure is
[def-sfb-modobj-relative-tensor], and the symmetric structure is
[def-sfb-modobj-symmetric-tensor].

Part 3. Since $\mathcal C$ is closed, $X\otimes-$ is a left adjoint. By the symmetry, so is
$-\otimes X$. Hence both preserve colimits, and in particular $\mathcal R\otimes-$ is right
exact. An abelian category has coequalizers. So parts 1 and 2 apply. Closedness is
[def-sfb-modobj-internal-hom]. The Grothendieck property is
[lem-sfb-modobj-grothendieck], and the flat resolutions are
[lem-sfb-modobj-flat-resolutions].

Part 4. Take $\mathcal C=\Sh(X_{\mathrm{proét}},\Ab)$ with the tensor product of
[sk-def-sfb-sheaf-tensor]. It is closed symmetric monoidal. Its tensor product preserves
colimits in each variable, so in particular it is additive. It is a Grothendieck abelian
category:
- filtered colimits are exact, because sheafification is exact and filtered colimits of
  presheaves of abelian groups are exact;
- the sheafified free abelian sheaves $\mathbf Z_U$ on the objects $U$ form a generating
  family, and $X_{\mathrm{proét}}$ is essentially small.

It has functorial flat resolutions. $\mathbf Z_U\otimes F$ is the sheafification of
$V\mapsto\bigoplus_{\Hom(V,U)}F(V)$, which is exact in $F$. Hence $\mathbf Z_U$ is flat,
and so are direct sums of such sheaves. The canonical map
$\bigoplus_{U,\ s\in M(U)}\mathbf Z_U\to M$ is a functorial epimorphism. Finally,
$\Lambda_X=p_X^*\Lambda$ is a commutative monoid object because $p_X^*$ is braided
([sk-def-sfb-pulled-back-coefficients]). Now apply parts 3 and 1.
