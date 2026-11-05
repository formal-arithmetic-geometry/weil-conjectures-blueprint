+++
id = "corollary-torsion-jacobian-field-extension--5"
kind = "corollary"
title = "Picard group modulo $n$"
order = 1561010
aliases = ["bp-r487-5"]
lean = ["AlgebraicGeometry.Scheme.ker_picDegreeMod", "AlgebraicGeometry.Scheme.nonempty_addEquiv_torsionBy_pic_and_quotient"]
uses = ["corollary-degree-jacobian--1"]
+++
There is an isomorphism

$$
\operatorname{Pic}(C)/n\operatorname{Pic}(C)
\simeq\mathbf Z/n\mathbf Z.
$$

The kernel statement identifying this quotient by degree holds
without an invertibility assumption: for every integer $m>0$,

$$
\ker\bigl(\deg\bmod m:\operatorname{Pic}(C)
\longrightarrow\mathbf Z/m\mathbf Z\bigr)
=m\operatorname{Pic}(C).
$$

Together with the surjectivity of degree, this identifies the
quotient isomorphism with the one induced by degree.
