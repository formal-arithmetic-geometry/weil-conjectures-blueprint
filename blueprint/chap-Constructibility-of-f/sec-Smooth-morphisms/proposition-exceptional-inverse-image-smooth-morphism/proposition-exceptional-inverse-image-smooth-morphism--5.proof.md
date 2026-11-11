+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--5"
order = 562011
uses = ["proposition-forgetting-supports-composition", "definition-exceptional-base-change-finite", "lemma-cohomology-projective-line-trace", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "proposition-comparison-morphism-inverse-image--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-identity-pasting--1", "lemma-identity-pasting--2", "theorem-comparison-over-henselian-pair-degree--1", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--1", "proposition-forgetting-supports-composition--3", "proposition-adjunction-projective-line--1", "theorem-smooth-base-change-classical-torsion--1", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "lemma-finite-direct-images--1"]
+++
Use the chart descriptions and counits established in clauses [proposition-exceptional-inverse-image-smooth-morphism--1]–[proposition-exceptional-inverse-image-smooth-morphism--3].

We write
$\varepsilon_N:Rf_!f^!N\to N$ for the counit of
$Rf_!\dashv f^!$ (for $f=p$ this is (6.8)). The map (6.13) is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)
\xrightarrow{\ \sim\ }
N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{1\otimes\varepsilon_{\Lambda_S}}N ,
$$

where the first arrow is the projection formula. The map (6.1) is the
transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N
\xrightarrow{\ \sim\ }g^*Rf_!f^!N
\xrightarrow{g^*\varepsilon_N}g^*N,
$$

where the first arrow is the inverse of the base change isomorphism
for $Rf_!$ [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)].

*(6.13) is an isomorphism.* On each such $U$, under
(6.14), the source and the target of (6.13)
are both $e^*p_d^*v^*N(d)[2d]$. We claim that the map is the
identification obtained by reassociating tensor product and twist. It
suffices to compare the transposes. Both are the projection formula
followed by the counit for $v$, the $d$ counits for the affine lines, and
the étale counit for $e$. They agree by the formula for the counit of a
composite in Lemma [lemma-affine-space-etale-localization]. Hence
(6.13) is an isomorphism on $X$.

*Source:* the proof of Proposition [proposition-exceptional-inverse-image-smooth-morphism].
