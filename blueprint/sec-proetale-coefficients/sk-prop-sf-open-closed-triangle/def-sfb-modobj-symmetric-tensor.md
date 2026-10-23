+++
id = "def-sfb-modobj-symmetric-tensor"
kind = "definition"
title = "The symmetric monoidal structure on $\\Mod_{\\mathcal R}(\\mathcal C)$"
order = 1140
uses = ["def-sfb-modobj-relative-tensor"]
lean = ["CategoryTheory.Mod.symmetricCategory", "CategoryTheory.Mod.braidedCategory"]
+++
Let $\mathcal C$ be a symmetric monoidal category with coequalizers such that $X\otimes-$
and $-\otimes X$ preserve colimits for every $X$, and let $\mathcal R$ be a commutative
monoid object. The braiding $\beta_{M,N}\colon M\otimes N\to N\otimes M$ of $\mathcal C$
descends to an isomorphism of $\mathcal R$-module objects
$$
M\otimes_{\mathcal R}N\xrightarrow{\ \sim\ }N\otimes_{\mathcal R}M
$$
for the relative tensor product of [def-sfb-modobj-relative-tensor]. These isomorphisms
make $(\Mod_{\mathcal R}(\mathcal C),\otimes_{\mathcal R},\mathcal R)$ a symmetric
monoidal category.
