+++
kind = "proof"
of = "lemma-extreme-degrees-affine-curve--2"
order = 1186005
uses = ["proposition-extension-zero-restriction-closed-subscheme", "lemma-finite-quasi-finite-direct-images", "lemma-degree-zero-top-cohomology"]
+++
Give $C_0-U_0$ its reduced closed subscheme structure and write
$i:Z_0\hookrightarrow C_0$ for its inclusion. This is a finite
$\Fq$-scheme. The open--closed sequence
([proposition-extension-zero-restriction-closed-subscheme]), after
applying compactly supported cohomology and using $j^*j_*F\simeq F$,
gives the distinguished triangle

$$
\RGammac(U,F)\longrightarrow\RGammac(C,j_*F)
\longrightarrow\RGammac(Z,i^*j_*F)\longrightarrow.
$$

The third term has cohomology only in degree zero, by exactness for
finite direct images ([lemma-finite-quasi-finite-direct-images]).
For $r\ge2$, its cohomology in both degrees $r-1$ and $r$ vanishes,
so the long exact sequence gives a Frobenius-equivariant isomorphism
$H_c^r(U,F)\simeq H_c^r(C,j_*F)$. This is
`AlgebraicGeometry.nonempty_equiv_compactlySupportedCohomology_directImage_of_two_le`.

The nonempty open $U_0$ is again a smooth geometrically connected
affine curve. Apply the degree-two identification in
[lemma-degree-zero-top-cohomology], obtained from the perfect
Poincaré pairing with $H^0(U,F^\vee)$, to get
$H_c^2(U,F)\simeq W(-1)$. Compose it with the inverse of the
localization isomorphism in degree two.
