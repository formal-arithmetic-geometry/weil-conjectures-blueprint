+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--6"
order = 562013
uses = ["definition-derived-base-change-map", "proposition-forgetting-supports-composition", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--1", "lemma-identity-pasting--2", "theorem-comparison-over-henselian-pair-degree--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--1", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--4", "proposition-adjunction-projective-line--3", "theorem-smooth-base-change-classical-torsion--1", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
The comparisons are the adjoint transposes specified below.

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

*(6.1) is an isomorphism.* For each type of chart,
under the explicit description of $f^!$ as a
twisted inverse image, (6.1) is the evident identification of
inverse images. For the projective line, the transpose of
(6.2) is the usual identification
$g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of pullbacks. This holds because the unit
(6.7) and counit (6.8) commute with base change.
By restriction to the affine line and composition, the same holds for
affine space. For a separated étale map $u$, the transpose is again the
usual identification of inverse images. Indeed, the stalk of $u_!M$ at a
geometric point is the direct sum of the stalks of $M$ at the geometric
points over it. This description is compatible with base change, and under
it the counit $u_!u^*N\to N$ is the sum of the identity maps of the stalks
of $N$.

The cases combine, because base change for $Rf_!$ is compatible with
composition [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)] and the counit of a composite is the composite of
the counits. The open immersions $u$ and $v$ are étale. Substituting
these facts into (6.2), we see that the restriction of
(6.1) to $U\times_XX'$ is the composite of the étale and
affine-space cases just treated. Hence (6.1) is an
isomorphism on a cover of $X'$, and therefore it is an isomorphism.

*Source:* the proof of Proposition [proposition-exceptional-inverse-image-smooth-morphism].
