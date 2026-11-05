+++
id = "definition-exceptional-base-change-finite"
kind = "definition"
title = "The base change map for $f^!$, finite coefficients"
order = 539
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $f:X\to S$ be separated and of finite type, let $g:S'\to S$ be a
morphism, let $X'=X\times_SS'$, and let $f':X'\to S'$, $g':X'\to X$ be the
projections. For $N\in D(S_{\acute{e}t},A)$, let
$\varepsilon_N:Rf_!f^!N\to N$ be the counit of $Rf_!\dashv f^!$. The
*base change map*

$$
\beta_N:g'^*f^!N\longrightarrow f'^!g^*N
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
for $Rf_!$ (Proposition [proposition-composition-base-change-rf-shriek](2)).
