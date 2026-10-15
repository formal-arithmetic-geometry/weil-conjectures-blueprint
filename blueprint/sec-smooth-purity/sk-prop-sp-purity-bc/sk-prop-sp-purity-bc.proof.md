+++
kind = "proof"
of = "sk-prop-sp-purity-bc"
uses = ["sk-prop-sp-exceptional-bc", "sk-prop-sp-tower-geometric"]
+++
For a finite ring $A$ the following orientation and counit calculation is made
directly with $A$-coefficients. For $\mathcal O_E$ we make it for the tower
purity map $\gamma_{f,\bullet}$ of the tower model [sk-prop-sp-tower-geometric]
and apply $R\varprojlim$; the tower exceptional base change
$e_{f,\bullet}:u_\bullet^*f_\bullet^!\to(f')_\bullet^!v_\bullet^*$ (the transpose of
$v_\bullet^*(\varepsilon_{f,\bullet})\circ\beta_{f,\bullet}^{-1}$, with $\beta_{f,\bullet}$
the tower compact-support base change) has as levels the finite exceptional
base changes, is compatible with the reduction maps by the mixed base-change
identities, and its $R\varprojlim$ is the integral exceptional base change.
Inverting $\ell$ and descending to a common finite extension then give $E$ and
$\Qlb$. We write out the tower calculation; dropping the index $\bullet$ gives the
finite one. The map $\gamma_{f,\bullet}$ is the composite of the orientation
$(\mathcal O_{E,X}/\ell^\bullet)(d)[2d]\xrightarrow{\sim}\omega_{f,\bullet}$ and the tensor
map $f_\bullet^*K_\bullet\otimes\omega_{f,\bullet}\to f_\bullet^!K_\bullet$, both morphisms
in $\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$, and we treat the two factors
separately.

*Orientation.* The diagonal, its normal bundle, the deformation to the normal
bundle and the integration on vector bundles all commute with base change; on
each coordinate chart this is the finite-level geometric calculation, at every
level $n$. After removing the shift $[2d]$, the two orientations to be compared
are maps between rank-one tower sheaves in degree zero. Equality of maps of
sheaves can be tested at each level, so the orientations agree in
$\Dctf(X'_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$.

*Tensor map.* Transpose both tensor maps under the tower adjunction for $f'$,
between $\Dctf(X'_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$ and
$\Dctf(Y'_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$. By the definition of
$e_{f,\bullet}$, the transpose of the pulled-back tensor map is the pulled-back
counit for $f$, preceded by the projection-formula map in
$\Dctf(Y'_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$; by naturality of the projection
formula under pullback, the transpose of the tensor map for $f'$ is the same
composite. This is the counit calculation of [sk-prop-sp-exceptional-bc],
carried out with towers. So the transposes, and hence the tensor maps, are
equal.
