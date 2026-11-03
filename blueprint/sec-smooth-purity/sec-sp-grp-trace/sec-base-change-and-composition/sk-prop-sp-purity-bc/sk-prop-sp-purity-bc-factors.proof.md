+++
kind = "proof"
of = "det-sp-purity-bc-factors"
+++
(1) The diagonal of $f'$ is the base change of the diagonal of $f$, the normal
bundle of the base-changed diagonal is the pullback $u^*T_{X/Y}=T_{X'/Y'}$, the
deformation to the normal bundle commutes with base change, and vector-bundle
integration is compatible with pullback. On each coordinate chart
([det-sp-orientation-charts]) the orientation is the affine-space orientation,
whose pullback is the affine-space orientation of the pulled-back chart; this is
the finite-level geometric calculation, valid at every level $n$. After removing
the shift $[2d]$, the two orientations to be compared are maps between rank-one
(tower) sheaves in degree zero; equality of such maps is local and can be
tested at each level, so the orientations agree.

(2) Transpose both maps under the adjunction $R(f')_{!,\bullet}\dashv(f')^!_\bullet$.
The tensor map for $f$ is the transpose of
$Rf_{!,\bullet}(f^*K\otimes\omega_f)\simeq K\otimes Rf_{!,\bullet}\omega_f\xrightarrow{\mathrm{id}\otimes\varepsilon_f}K$
(projection formula, then counit at the unit object). By the definition of
$e_{f,\bullet}$ as the transpose of $v^*\varepsilon_f\circ\beta_f^{-1}$, the transpose
of the pulled-back tensor map is: compact-support base change, then the
pulled-back projection formula, then the pulled-back counit. By naturality of
the projection formula under pullback (compatibility of the projection formula
with base change), this equals the projection formula for $f'$ followed by
$\mathrm{id}\otimes\varepsilon_{f'}$ at $v^*K$ — the transpose of the tensor map for
$f'$ (with $\omega_{f'}$ identified via $e_f$ at the unit object, consistently
with (1)). Equal transposes give equal maps.

Since $\gamma$ is the inverse orientation followed by the tensor map
([det-sp-tower-gamma]), (1) and (2) give the final identity.
