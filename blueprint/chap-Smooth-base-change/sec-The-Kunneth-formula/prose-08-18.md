+++
id = "prose-08-18"
kind = "hidden"
title = "The Künneth formula (1)"
order = 705
+++
The trace formula needs the Künneth formula for ordinary direct images
(Proposition [proposition-ordinary-external-kunneth]), which is a base change
statement for $Rf_*$. Base change for $Rf_*$ fails in general, as the open
immersion $j:\mathbf G_m\hookrightarrow\mathbf A^1$ of the beginning of the
section shows. Along a product
projection $Y\times T\to Y$, however, base change holds
(Lemma [lemma-base-change-along-product-projection]). To prove this we
compactify, after which only an open immersion remains, and for an open
immersion the statement comes down to two results: base change along
extensions of the ground field, a consequence of smooth base change, and the
Künneth formula with one proper factor, a consequence of proper base
change. In this subsection $A$ is a finite
admissible ring, and we write $M\boxtimes N=p_1^*M\otimes^{\mathbf L}p_2^*N$
for the external tensor product.

We start with the base change statement, which is the case of the
Künneth formula in which the second coefficient is constant.
