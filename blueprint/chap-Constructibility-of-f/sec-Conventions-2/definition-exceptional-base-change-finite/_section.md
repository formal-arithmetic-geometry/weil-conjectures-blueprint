+++
id = "definition-exceptional-base-change-finite"
kind = "definition"
title = "The base change map for $f^!$, finite coefficients"
order = 539
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap", "AlgebraicGeometry.Etale.upperShriekBaseChangeMap"]
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to S$ be separated and of finite type, let $g:S'\to S$ be a
morphism, let $X'=X\times_SS'$, and let $f':X'\to S'$, $g':X'\to X$ be the
projections. For $N\in D(S_{\acute{e}t},A)$, let
$\varepsilon_N:\href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!N}\to N$ be the counit of $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$. The
*base change map*

$$
\beta_N:g'^*\href{@theorem-existence-exceptional-inverse-image}{f^!N}\longrightarrow \href{@theorem-existence-exceptional-inverse-image}{f'^!}g^*N
\tag{6.1}
$$

is the transpose, for $f'$, of the morphism

$$
\href{@proposition-construction-independence-rf-shriek}{Rf'_!}g'^*\href{@theorem-existence-exceptional-inverse-image}{f^!N}
\xrightarrow{\ \sim\ }g^*\href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!N}
\xrightarrow{g^*\varepsilon_N}g^*N,
\tag{6.2}
$$

where the first arrow is the inverse of the base change isomorphism
for [$Rf_!$](@proposition-construction-independence-rf-shriek) (Proposition [proposition-composition-base-change-rf-shriek](2)).
