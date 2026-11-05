+++
id = "theorem-comparison-over-henselian-pair-degree"
kind = "theorem"
title = "Henselian comparison in degree zero"
order = 328
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_of_henselianRing", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_addCommGrpCat_of_henselianRing", "AlgebraicGeometry.Etale.globalSectionsUpperStarMap_naturality"]
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form"]
+++
Let $(R,J)$ be a henselian pair, let $Z\to\operatorname{Spec}R$ be
proper, and let $i:Z_0=Z\times_R\operatorname{Spec}(R/J)\hookrightarrow Z$.
For every sheaf of sets $F$ on $Z_{\acute{e}t}$, restriction is a bijection

$$
\Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_0,i^*F).
$$

The comparison is natural in $F$.
