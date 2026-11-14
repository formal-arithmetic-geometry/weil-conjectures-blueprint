+++
id = "definition-exceptional-base-change-finite--1"
kind = "definition"
title = "The base change map for $f^!$"
order = 539001
aliases = ["bp-r542-1"]
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap"]
uses = ["definition-derived-base-change-map", "proposition-composition-open-restriction-compactifications-f", "definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Let $f:X\to S$ be separated and of finite type, let $g:S'\to S$ be a
morphism, let $X'=X\times_SS'$, and let $f':X'\to S'$, $g':X'\to X$ be the
projections. For $N\in D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$, let
$\varepsilon_N:Rf_!f^!N\to N$ be the counit of $Rf_!\dashv f^!$. The
*base change map*

$$
g'^*_\Lambda f^!_\Lambda N\longrightarrow f'^!_\Lambda g^*_\Lambda N
\tag{6.1}
$$

is the transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N
\xrightarrow{\ \sim\ }g^*Rf_!f^!N
\xrightarrow{g^*\varepsilon_N}g^*N,
\tag{6.2}
$$

where the first arrow is the inverse of the base change isomorphism
for $Rf_!$ [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)].
