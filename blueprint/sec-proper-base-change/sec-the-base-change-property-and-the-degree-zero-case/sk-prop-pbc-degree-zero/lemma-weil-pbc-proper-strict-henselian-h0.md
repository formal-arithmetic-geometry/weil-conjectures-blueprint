+++
id = "lemma-weil-pbc-proper-strict-henselian-h0"
kind = "lemma"
title = "Degree-zero comparison over a strictly henselian base"
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_geometricFibre", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_addCommGrpCat_geometricFibre"]
order = 1654
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-finite-section-pullback", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-universal-homeomorphism-base-change", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-finite-pullback-composition", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $A$ be strictly henselian local
[def-weil-pbc-henselian-terminology], let $S=\operatorname{Spec}A$, write
$k=A/\mathfrak m$, and let $s:\Spec k^{\mathrm{alg}}\to S$ be the closed
geometric point given by an algebraic closure $k^{\mathrm{alg}}$ of $k$. Let
$p:Z\to S$ be proper [def-weil-pbc-scheme-conventions], with closed geometric
fibre $Z_s=Z\times_S\Spec k^{\mathrm{alg}}$ and projection $a:Z_s\to Z$. Let
$\Lambda$ be a commutative ring. For every etale sheaf $F$ of $\Lambda$-modules
on the small etale site [def-weil-pbc-etale-site] of $Z$, in particular for every
etale abelian sheaf [def-weil-pbc-etale-sheaves], the pullback of global
sections [def-weil-pbc-finite-section-pullback] along $a$

$$
 a^\sharp:\Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_s,a^{-1}F)
$$

is an isomorphism.
