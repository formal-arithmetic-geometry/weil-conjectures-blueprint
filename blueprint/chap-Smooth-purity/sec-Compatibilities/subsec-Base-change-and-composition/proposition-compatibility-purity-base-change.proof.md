+++
kind = "proof"
of = "proposition-compatibility-purity-base-change"
order = 792
+++
The map $\gamma_f$ has two factors, the orientation of $\omega_f$ and the
map (9.4). We show that each commutes with base
change. For the orientation this is a local statement about rank one
sheaves, and it follows from the naturality of the deformation to the
normal bundle. For (9.4) we compare transposes under the
adjunction for $f'$.

For a finite ring $A$ we compare the orientations and the maps
(9.4) directly with coefficients in $A$, and for
$\mathcal O_E$ we compare the maps on towers $\gamma_{f,\bullet}$ of
(9.19) and apply $R\varprojlim$. The cases $E$ and
$\overline{\mathbf Q}_\ell$ follow, since
$\gamma_{f,E}$ and $\gamma_{f,\overline{\mathbf Q}_\ell}$ are obtained from
$\gamma_{f,\mathcal O_E}$ by inverting $\ell$ and by extension of scalars from
a finite extension of $\mathbf Q_\ell$.
We write out the calculation for towers; dropping the index $\bullet$
gives the calculation at finite level. The map $\gamma_{f,\bullet}$ is the composite of
the orientation
$(\mathcal O_{E,X}/\ell^\bullet)(d)[2d]\xrightarrow{\sim}\omega_{f,\bullet}$
and the map
$f_\bullet^*K_\bullet\otimes\omega_{f,\bullet}\to f_\bullet^!K_\bullet$
for $K_\bullet=\operatorname{red}_YK$.

*Orientation.* After removing the shift $[2d]$, the two orientations
to be compared are maps between sheaves of towers of rank one in degree
zero. Maps between sheaves form a sheaf, and a map of sheaves of towers is
a compatible family of maps of sheaves. Hence equality may be tested
locally on $X'$ and at each level $n$. At a fixed level, the diagonal, its
normal bundle, the deformation to the normal bundle and the trace map of
vector bundles all commute with base change
(Lemma [lemma-naturality-under-base-change-etale](1)). Therefore so
does the orientation built from them.

*The map $f^*K\otimes\omega_f\to f^!K$.* This factor is not a map of
sheaves, so we cannot compare the two maps locally. However, a map into
$f'^!_\bullet g^*K_\bullet$ is determined by its transpose under the adjunction
on towers for $f'$. By the definition of $e_{f,\bullet}$, the transpose of the
pulled-back map (9.4) for $f$ is the pulled-back counit
for $f$, preceded by
the map of the projection formula. Since the projection formula is natural
under pullback, the transpose of the map for $f'$ is the same
composite, as in the counit calculation in the proof of
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3), carried out with towers.
