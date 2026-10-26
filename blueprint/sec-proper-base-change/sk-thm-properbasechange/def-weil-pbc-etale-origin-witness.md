+++
id = "def-weil-pbc-etale-origin-witness"
kind = "definition"
title = "Explicit etale-origin witness"
order = 1961
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.plusEtaleOrigin"]
uses = ["def-weil-pbc-site-comparison-morphism"]
+++
An object $K\in D(T_{\Proet},\Lambda)$ is *bounded below of étale origin*
(it *comes from the etale site*) if there exist

$$
 L\in\Dplus(T_{\Et},\Lambda)\quad\text{and an isomorphism}\quad
 \alpha:\nu_T^*L\xrightarrow{\sim}K,
$$

where $\nu_T^*$ is the inverse image of the comparison morphism of sites
[def-weil-pbc-site-comparison-morphism]. Such a pair $(L,\alpha)$ is called an
*etale-origin witness* for $K$. The objects of étale origin form a full
subcategory of $D(T_{\Proet},\Lambda)$ closed under isomorphisms.
