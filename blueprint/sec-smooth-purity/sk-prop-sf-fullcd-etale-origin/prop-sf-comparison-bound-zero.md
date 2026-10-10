+++
id = "prop-sf-comparison-bound-zero"
kind = "theorem"
title = "The comparison bound on coefficients of étale origin is $M=0$"
order = 1797
tags = ["latex:proposition"]
uses = ["def-sf-fullcd-used-class", "def-weil-full-cohomological-dimension", "def-weil-pbc-etale-sheaves", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "lem-sf-proetale-constructible-origin", "thm-sf-fullcd-etale-origin", "thm-sp-grothendieck"]
+++
Let $X$ be a scheme and let $\nu_X:X_{\Proet}\to X_{\Et}$ be the comparison
morphism of [def-weil-pbc-site-comparison-morphism], the coefficient ring
being $A$. Let $G$ be a sheaf of $A$-modules on the small étale site
$X_{\Et}$, in the sense of [def-weil-pbc-etale-sheaves]; *no*
constructibility hypothesis is imposed on $G$. Then the adjunction map

$$
G\longrightarrow\nu_{X,*}\nu_X^*G
$$

is an isomorphism, and consequently

$$
R^q\nu_{X,*}\bigl(\nu_X^*G\bigr)=0\qquad(q>0).
$$

Thus on the sheaves of étale origin – equivalently, by
[lem-sf-proetale-constructible-origin], on the coefficient sheaves of the
blueprint's class [def-sf-fullcd-used-class] – the vanishing degree of
the comparison direct image is bounded by $M=0$, independently of the
dimension of $X$ and of any constructibility of $G$.
