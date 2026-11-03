+++
kind = "proof"
of = "thm-weil-pbc-qbar"
uses = ["det-thm-sfb-proper-base-change-rational", "det-def-sfb-dc-restricted-functors"]
+++
*Forgetting the Weil structure.* Let $\operatorname{For}$ denote the forgetful
functor from Weil modules to modules, and also the induced functor on derived
categories ([def-weil-weil-sheaf-complex]). The unit and counit of the module
adjunction $f^*\dashv f_*$ commute with the Weil structures defined in the
statement (they are natural and compatible with the composition isomorphisms
for $fg_X=g_Yf$), so $f^*\dashv f_*$ lifts to Weil modules, and likewise for
$f'$; $\operatorname{For}$ carries these adjunctions, and the pullback
comparison, to the module ones. On Weil modules over $T$, $\operatorname{For}$
has the exact left adjoint $M\mapsto\bigoplus_{n\in\mathbf Z}(g_T^n)^*M$, with
the Weil structure permuting the summands, so $\operatorname{For}$ preserves
K-injective complexes. As it commutes with the underived $f_*$, it follows that
$\operatorname{For}\circ Rf_*\cong Rf_*\circ\operatorname{For}$, compatibly
with units and counits, and trivially $\operatorname{For}\circ h^*=
h^*\circ\operatorname{For}$. Hence
$\operatorname{For}(\mathrm{BC}_K)$ is the base change morphism
$\mathrm{BC}_{\operatorname{For}K}$ of [det-def-sfb-base-change-morphism] for
the square $X',X,Y',Y$ over $k$ and $\operatorname{For}K\in\Dbc(X,\Qlb)$.

*Constructibility and the isomorphism.* The schemes $X,X',Y,Y'$ are of finite
type over $k$, and $Y,Y'$ are quasi-compact. Both assertions below are local on
$Y$, resp. $Y'$: restriction to an open subscheme commutes with derived direct
images ([Tag 0D6G](https://stacks.math.columbia.edu/tag/0D6G)), with inverse
images, units and counits, hence carries $\mathrm{BC}$ to the base change
morphism of the restricted square. Cover $Y$ by finitely many affine opens
$V$, and $Y'$ by finitely many affine opens $V'$ each mapping into some
affine open $V$ of $Y$; then $V,V'$, and $f^{-1}V$,
$f'^{-1}V'$ (proper over them), are separated and of finite type over $k$.
Inverse images and, for $\Lambda=\Qlb$, direct images preserve bounded
constructible complexes between such schemes ([det-def-sfb-dc-restricted-functors];
for the proper direct images also [det-thm-sfb-proper-base-change-rational]
(2)). Applying this on the finitely many affine opens involved,
$Rf_*\operatorname{For}K$, $h^*Rf_*\operatorname{For}K$ and
$Rf'_*h'^*\operatorname{For}K$ are bounded with constructible cohomology; since
$\operatorname{For}$ commutes with $Rf_*$, $Rf'_*$, $h^*$, $h'^*$ and with
cohomology objects, $h^*Rf_*K$ and $Rf'_*h'^*K$ are Weil complexes. By
[det-thm-sfb-proper-base-change-rational] (3) for $\Lambda=\Qlb$ and the
restricted squares, $\mathrm{BC}_{\operatorname{For}K}=
\operatorname{For}(\mathrm{BC}_K)$ is an isomorphism. A morphism of complexes
of Weil modules is a quasi-isomorphism if and only if the underlying morphism
of complexes of modules is one, since cohomology of Weil modules is computed
on the underlying modules; so $\mathrm{BC}_K$ is an isomorphism, and it is an
isomorphism of Weil complexes because these form a full subcategory of the
derived category of Weil modules. This proves (1).

*Weil sheaves.* Apply (1) to $K=\mathcal F[0]$. The pullbacks $h^*$, $h'^*$ are
induced by exact functors of Weil modules, so they commute with
$\mathcal H^i$ and $h'^*(\mathcal F[0])=(h'^*\mathcal F)[0]$. Taking
$\mathcal H^i$ of $\mathrm{BC}_{\mathcal F[0]}$ gives
$h^*R^if_*\mathcal F\cong R^if'_*h'^*\mathcal F$ as Weil sheaves, which is (2).
