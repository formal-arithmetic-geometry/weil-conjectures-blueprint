+++
kind = "proof"
of = "lemma-external-duality-trace-morphism--1"
order = 910001
uses = ["lemma-constructible-sheaves", "theorem-sp-qbar", "definition-exceptional-base-change-map", "proposition-composition-base-change-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "proposition-construction-independence-rf-shriek", "proposition-projection-formula-rational-coefficients"]
+++
Fix $M$. We use dévissage in $N$: invertibility of
$\kappa_{M,N[n]}$ for all $n\in\mathbf Z$ is stable under distinguished
triangles. The constructible generation theorem
`AlgebraicGeometry.ProEtale.CondensedRing.triangEnvelope_lisseGenerator`
reduces the assertion to $N=Rg_!Rj_!L$, where $g:Z\hookrightarrow Y$
is closed, $j:U\hookrightarrow Z$ is open, $U$ is affine and $L$ is
dualizable. This is the derived form of the stratification used in
[lemma-constructible-sheaves].

Compatibility of $\kappa$ with closed pushforward and extension by zero
reduces to $L$ on $U$. For a dualizable object, the external Hom map is
an isomorphism, so it suffices that
$\alpha:M\boxtimes\omega_U\to p_X^!M$ be an isomorphism. These are
the steps `isIso_kunnethVerdierMap_lowerShriek_iff_of_isClosedImmersion`,
`isIso_kunnethVerdierMap_lowerShriek` and
`isIso_kunnethVerdierMap_of_exactPairing` in the namespace
`AlgebraicGeometry.ProEtale.CondensedRing`.

To prove this last assertion, embed $U$ as a closed subscheme
$i:U\hookrightarrow\mathbf A^n_k$, with open complement $j':W\hookrightarrow
\mathbf A^n_k$. Both $\mathbf A^n_k$ and $W$ are smooth, so smooth purity
[theorem-sp-qbar] and exceptional base change make their maps $\alpha$
invertible. Apply the open–closed triangle

$$
Rj'_!\Qbarl_W\longrightarrow\Qbarl_{\mathbf A^n_k}
\longrightarrow Ri_*\Qbarl_U\longrightarrow
$$

and the two-out-of-three property for $\kappa$, including all shifts.
Closed pushforward then gives invertibility of $\kappa_{M,\Qbarl_U}$.
The unit comparison `isIso_kunnethVerdierMap_unit_iff` identifies this
with invertibility of $\alpha$ on $U$. Thus
`isIso_exceptionalKunnethMap_of_isAffine` supplies the affine case,
and dévissage proves the assertion for every $N$.
