+++
kind = "proof"
of = "det-sp-orientation-charts"
+++
*Step 1: Cartesian square of centres.* The étale map
$e\times e:U\times_YU\to\mathbf A^d_Y\times_Y\mathbf A^d_Y$ carries the
diagonal of $U$ into the diagonal of $\mathbf A^d_Y$. The inverse image of the
latter is $U\times_{\mathbf A^d_Y}U$, in which the diagonal of $U$ is open and
closed because $e$ is separated and étale. Removing the other components (an
open subscheme of $U\times_YU$ containing the diagonal) gives a Cartesian
square of centres: the diagonal of $U$ is the inverse image of the diagonal of
$\mathbf A^d_Y$ under an étale map.

*Step 2: normal bundles.* The induced map of normal bundles is the
differential $T_{U/Y}\xrightarrow{\sim}e^*T_{\mathbf A^d_Y/Y}$, an isomorphism of
vector bundles (pullback of vector bundles), since $e$ is étale.

*Step 3: the ingredients are pulled back.* For the dualizing complex: by
composing adjunctions, $\omega_{f|_U}=(p_d\circ e)^!\simeq e^!p_d^!$, and the
exceptional inverse image along an étale map is its ordinary inverse image, so
$\omega_{f|_U}\simeq e^*\omega_{p_d}$. For the deformation comparison: the
deformation space of the centre in Step 1 maps étale to that of the diagonal of
$\mathbf A^d_Y$, the pulled-back comparison is the identity at $t=1$, and the
uniqueness in the deformation lemma identifies it with the comparison for $U$.

*Step 4.* Vector-bundle integration is preserved by the linear isomorphism of
Step 2. By [det-sp-orientation-vector-bundle] the diagonal orientation of the
trivial bundle $T_{\mathbf A^d_Y/Y}$ is the vector-bundle orientation, i.e.
integration on $\mathbf A^d_Y$. Combining Steps 1–3, the diagonal orientation
on $U$ is the pullback along $e$ of the affine-space orientation, which is the
affine-space orientation of $U$ given by its coordinate adjunction.
