+++
id = "sk-thm-sf-kunneth-verdier"
kind = "theorem"
title = "Künneth–Verdier isomorphism"
order = 2512
uses = ["sk-def-sf-kv-maps", "sk-def-sf-operations", "sk-lem-sf-flat-model", "sk-lem-sf-kunneth-star", "sk-lem-sf-mate", "sk-prop-sf-biduality-general", "sk-prop-sf-closed-unit", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-localization", "sk-prop-sf-open-closed-triangle", "sk-thm-regular", "sk-thm-sf-ctf-stability", "sk-thm-sf-tensor-hom", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.hasKunnethComparisons"]
tags = ["sketch"]
+++
The three maps of [sk-def-sf-kv-maps] are isomorphisms, natural in their
variables, under the hypotheses of that definition (the $Rf_i^!$ are the
constructible exceptional adjoints of [sk-def-sf-operations] (vi); no
admissibility datum of [sk-def-sf-admissible] is assumed): the
exceptional Künneth map $\alpha$, the external Hom map $\beta$, and the
Künneth–Verdier map $\kappa$. In particular, for $X,Y$ separated of finite
type over $k$, with the structure
morphism $a_Y$ and the product projection $p_X=\operatorname{id}_X\times a_Y$
as in [sk-def-sf-kv-maps] (iv), and
$M\in\Dctf(X,\Lambda)$, $N\in\Dctf(Y,\Lambda)$,

$$
\kappa_{M,N}:M\boxtimes\mathbb D_YN\ \xrightarrow{\ \sim\ }\
\RHom\bigl(p_Y^*N,Rp_X^!M\bigr).
$$
