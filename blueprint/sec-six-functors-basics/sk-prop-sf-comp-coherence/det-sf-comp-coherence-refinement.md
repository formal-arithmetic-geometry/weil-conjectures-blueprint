+++
id = "det-sf-comp-coherence-refinement"
kind = "lemma"
title = "The refinement map on the localizing category"
order = 2285
uses = ["lem-weil-pbc-proper-open-comparison-iso", "det-sf-comp-coherence-single", "det-sf-determination-localizing"]
+++
Let $\Lambda$ be admissible, $f:X\to Y$ separated of finite type, and let
$j:X\to Z$, $j':X\to Z'$ be dense compactifications of $f$ over $Y$ together
with a refinement $h:Z'\to Z$, i.e. a proper $Y$-morphism with $h\circ j'=j$
and $h^{-1}(X)=X$. Let

$$
e_{h,K}:j_!K\longrightarrow Rh_*j'_!K\quad\text{in }D(Z_{\mathrm{proét}},\Lambda)
$$

be the adjoint, under $j_!\dashv j^*$, of the isomorphism
$K\simeq j^*Rh_*j'_!K$. Then:

1. $e_{h,K}$ is the unique map $j_!K\to Rh_*j'_!K$ whose restriction to $X$ is
the identity of $K$;
2. $e_{h,K}$ is an isomorphism for every $K\in\Loc(\Dctf(X,\Lambda))$;
3. $e_{\mathrm{id},K}=\mathrm{id}$, and for successive refinements
$Z''\xrightarrow{k}Z'\xrightarrow{h}Z$ one has
$e_{hk,K}=Rh_*(e_{k,K})\circ e_{h,K}$ under $R(hk)_*=Rh_*Rk_*$.
