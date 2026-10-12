+++
id = "lem-sf-hom-triangulated"
kind = "lemma"
title = "Exactness of the internal Hom in each variable"
order = 2385
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-pbc-etale-site", "def-weil-pbc-kinjective-resolutions", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $A$ be a commutative ring, let $X$ be a scheme and let
$K',K,K'',M,M',M''$ be complexes of $A$-modules on $X_{\Et}$. If
$K'\to K\to K''\to K'[1]$ and $M'\to M\to M''\to M'[1]$ are
distinguished triangles of $D(X_{\Et},A)$, then the sequences

$$
R\mathcal Hom_A(K'',M)\to R\mathcal Hom_A(K,M)\to R\mathcal Hom_A(K',M)
\to R\mathcal Hom_A(K'',M)[1],
$$

$$
R\mathcal Hom_A(K,M')\to R\mathcal Hom_A(K,M)\to R\mathcal Hom_A(K,M'')
\to R\mathcal Hom_A(K,M')[1]
$$

are distinguished triangles, the internal Hom being that of
[def-weil-derived-pullback-tensor-hom], computed by a K-injective
resolution of the second variable.
