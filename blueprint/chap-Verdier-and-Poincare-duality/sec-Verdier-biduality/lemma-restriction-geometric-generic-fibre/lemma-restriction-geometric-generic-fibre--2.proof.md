+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--2"
order = 838005
uses = ["lemma-restriction-geometric-generic-fibre--1", "lemma-sections-support-closed-subscheme", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition"]
+++
The restriction $j^*M$ is bounded constructible, so
[lemma-restriction-geometric-generic-fibre--1] applies to it. Pull back
the localization triangle with closed support
([lemma-sections-support-closed-subscheme])

$$
i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M\longrightarrow.
$$

Since $i_*=Ri_!$ for a closed immersion
([proposition-forgetting-supports-composition]), compact-support base change
([proposition-composition-base-change-rf-shriek]) identifies the first
term with $i_{S,*}g_Z^*i^!M$. The open comparison identifies the third
term with $Rj_{S,*}g_U^*j^*M$.

There are no nonzero maps from $i_{S,*}Q[n]$ to the third term, for any
$Q$ and any integer $n$: by adjunction such maps are computed after
$j_S^*$, which kills objects supported on $Z_S$. The long exact Hom
sequence therefore shows that the transpose of the first arrow is an
isomorphism, because $i_{S,*}$ is fully faithful. The mate identity
identifies this transpose with the canonical exceptional base change map.
This is
`AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_isIso`,
applied to the open comparison.
