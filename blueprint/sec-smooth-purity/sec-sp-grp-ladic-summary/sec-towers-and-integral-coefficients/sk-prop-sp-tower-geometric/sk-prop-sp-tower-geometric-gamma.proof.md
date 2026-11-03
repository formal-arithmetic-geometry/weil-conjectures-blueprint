+++
kind = "proof"
of = "det-sp-tower-gamma"
+++
(1) By the chart form in [det-sp-tower-gluing],
$\omega_{f,\bullet}[-2d]$ is locally $(\mathcal O_{E,U}/\ell^\bullet)(d)$, a rank-one
tower sheaf in degree zero. Vector-bundle integration does not depend on
frames, by the universal $\GL_d$ calculation of vector-bundle purity: the
possible discrepancy between two frames is a map of tower sheaves in degree
zero, so it can be checked level by level, where it is the identity. For the
deformation family, the coordinate construction of the deformation lemma gives
comparisons of tower sheaves normalized at $t=1$; at each level these are the
finite comparisons, and the uniqueness (a map of rank-one tower sheaves is
determined by its levels, each of which is determined by normalization at
$t=1$) glues them and determines them at $t=0$. The resulting diagonal
orientation, a map of tower sheaves after removing the shift, has as levels the
finite orientations of [thm-pur-diagonal-dualizing-object].

(2) The tensor map
$f^*_\bullet K_\bullet\otimes^{\mathbf L}\omega_{f,\bullet}\to f^!_\bullet K_\bullet$ is the
transpose of
$Rf_{!,\bullet}(f^*_\bullet K_\bullet\otimes\omega_{f,\bullet})\simeq K_\bullet\otimes Rf_{!,\bullet}\omega_{f,\bullet}
\xrightarrow{\mathrm{id}\otimes\varepsilon_\bullet}K_\bullet$. At level $n$, by
[det-sp-tower-gluing] (levels of units and counits are the finite ones) and the
levelwise projection formula, it is the finite tensor map, an isomorphism.
Composing with the inverse orientation of (1) and the twist reassociation
gives $\gamma_{f,\bullet}(K_\bullet)$; its levels are the finite
$\gamma_{f,\mathcal O_E/\ell^n}(K_n)$, which are isomorphisms, so it is an
isomorphism. Naturality holds factorwise.

(3) If $C_\bullet$ is normalized, the reduction maps of $Rf_{!,\bullet}C_\bullet$ are
the composites of the comparisons $b$ of [det-sp-reduction-direct-image] with
$Rf_!$ of the reduction maps of $C_\bullet$, all isomorphisms. If $K_\bullet$ is
normalized, $f^*_\bullet K_\bullet(d)[2d]$ is normalized (pullback and twist commute
with extension of scalars), and by the purity compatibility
$c_{n,m}\circ(\gamma_{f,n})_m=\gamma_{f,m}$ of [det-sp-reduction-compatibilities]
together with (2), the isomorphism $\gamma_{f,\bullet}$ carries its reduction maps to
those of $f^!_\bullet K_\bullet$; so the latter are isomorphisms.
