+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--5"
order = 562011
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--6", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-cohomology-modules-underlying-abelian--1", "lemma-identity-pasting--1", "lemma-identity-pasting--2", "theorem-comparison-over-henselian-pair-degree--1", "lemma-finite-morphisms--2", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--5", "proposition-exceptional-inverse-image-smooth-morphism--8", "definition-change-of-coefficients-maps--6", "proposition-six-operations-change-coefficients--23", "theorem-smooth-base-change-classical-torsion--1", "theorem-smooth-base-change-classical-torsion-2--1", "lemma-kunneth-one-identity-factor--1", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1", "lemma-finite-direct-images--1"]
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
