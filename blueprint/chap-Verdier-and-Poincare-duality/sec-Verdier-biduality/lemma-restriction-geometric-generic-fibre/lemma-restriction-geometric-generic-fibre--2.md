+++
id = "lemma-restriction-geometric-generic-fibre--2"
kind = "lemma"
title = "Comparison for the exceptional inverse image"
order = 839003
aliases = ["bp-r251-2"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_generic"]
uses = ["definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "proposition-proper-base-change-degree-zero--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "definition-torsion-pbc-property--1", "definition-injective-acyclicity--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "proposition-proper-base-change-projective-line--1", "proposition-proper-base-change-etale-site--1", "proposition-comparison-etale-derived-category--3", "proposition-composition-base-change-rf-shriek--4", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
In the setting above, let $X$ be a $B$-scheme of finite type, let
$i:Z\hookrightarrow X$ be a closed immersion with open complement
$j:U\hookrightarrow X$, and let $i_{\bar\eta}:Z_{\bar\eta}\hookrightarrow X_{\bar\eta}$
be its base change. For every $M\in\Dbc(X,A)$ the map

$$
g_Z^*i^!M\longrightarrow i_{\bar\eta}^!g_X^*M
$$

defined above is an isomorphism. Here $i^!$ is the derived exceptional
inverse image, and the map corresponds under
$i_{\bar\eta,*}\dashv i_{\bar\eta}^!$ to the pullback
$i_{\bar\eta,*}g_Z^*i^!M=g_X^*i_*i^!M\to g_X^*M$ of the counit.
