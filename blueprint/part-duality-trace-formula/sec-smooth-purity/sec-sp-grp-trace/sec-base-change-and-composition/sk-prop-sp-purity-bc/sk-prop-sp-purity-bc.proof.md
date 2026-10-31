+++
kind = "proof"
of = "sk-prop-sp-purity-bc"
uses = ["sk-prop-cohsm", "sk-prop-sp-tower-geometric", "sk-lem-lem-sp-dnc-naturality"]
+++
We compare the orientations and the maps (10.9). For a finite ring $A$ we do this
directly with coefficients in $A$, and for $\mathcal O_E$ we do it for the
map on towers $\gamma_{f,\bullet}$ of (10.18) and
then apply $R\varprojlim$. The cases $E$ and $\overline{\mathbf Q}_\ell$ follow, since
$\gamma_{f,E}$ and $\gamma_{f,\overline{\mathbf Q}_\ell}$ are obtained from
$\gamma_{f,\mathcal O_E}$ by inverting $\ell$ and by extension of scalars from
a finite extension of $\Ql$.
We write out the calculation for towers. Dropping the index $\bullet$
gives the calculation at finite level. The map $\gamma_{f,\bullet}$ is the composite of
the orientation
$(\mathcal O_{E,X}/\ell^\bullet)(d)[2d]\xrightarrow{\sim}\omega_{f,\bullet}$
and the map
$f_\bullet^*K_\bullet\otimes\omega_{f,\bullet}\to f_\bullet^!K_\bullet$
for $K_\bullet=\operatorname{red}_YK$,
and we treat the two factors separately.

*Orientation.* After removing the shift $[2d]$, the two orientations
to be compared are maps between sheaves of towers of rank one in degree
zero, so equality may be tested locally on $X'$ and at each level $n$.
At a fixed level, the diagonal, its normal bundle, the deformation to
the normal bundle and the trace map of vector bundles all commute
with base change (Lemma [sk-lem-lem-sp-dnc-naturality](1)), and therefore
so does the orientation built from them. Hence the orientations agree.

*The map $f^*K\otimes\omega_f\to f^!K$.* We transpose both maps
(10.9) under the adjunction on towers
for $f'$. By the definition of $e_{f,\bullet}$, the transpose of the
pulled-back map for $f$ is the pulled-back counit for $f$, preceded by
the map of the projection formula. Since the projection formula is natural
under pullback, the transpose of the map for $f'$ is the same
composite. This is the counit calculation in the proof of
Proposition [sk-prop-cohsm](3), carried out with towers. Hence
the transposes are equal, and so are the two maps.
