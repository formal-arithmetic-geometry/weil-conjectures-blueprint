+++
id = "det-cor-affine-space-rational-line"
kind = "lemma"
title = "The affine line"
order = 2443
uses = ["sk-prop-p1-adjunction-rational", "sk-prop-sf-existence", "cor-amb-affine-space-adjunction"]
+++
Let $\Lambda=E$ or $\Qlb$, let $p:\mathbf A^1_V\to V$ be the projection,
$j:\mathbf A^1_V\hookrightarrow\mathbf P^1_V$ the standard open immersion and
$q:\mathbf P^1_V\to V$ the projection. On the categories
$\Loc(\Dbc(-,\Lambda))$:

1. $j_!$ and $j^*$ preserve these categories and $j_!\dashv j^*$;
2. $Rp_!\simeq Rq_*\circ j_!$;
3. $Rp_!$ is left adjoint to $p^*(1)[2]$, and $p^!\simeq p^*(1)[2]$ as functors
   $\Loc(\Dbc(V,\Lambda))\to\Loc(\Dbc(\mathbf A^1_V,\Lambda))$.
