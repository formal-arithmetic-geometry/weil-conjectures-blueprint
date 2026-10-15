+++
kind = "proof"
of = "det-ind-heart-ii-sums"
+++
For a finite subset $T\subset S$, the map $\bigoplus_{s\in T}\Ext^q(C,B_s)\to\Ext^q(C,\bigoplus_{s\in T}B_s)$
is an isomorphism because $\Ext^q(C,-)=\Hom(C,-[q])$ is additive and finite direct sums are biproducts.
The sum $\bigoplus_{s\in S}B_s$ is the filtered colimit, over the finite subsets $T$ ordered by
inclusion, of the sheaves $\bigoplus_{s\in T}B_s$ in degree $0$. By part (1) of
[sk-lem-constructible-ext-continuity],

$$
\Ext^q\Bigl(C,\bigoplus_SB_s\Bigr)=\varinjlim_T\Ext^q\Bigl(C,\bigoplus_TB_s\Bigr)
=\varinjlim_T\bigoplus_T\Ext^q(C,B_s)=\bigoplus_S\Ext^q(C,B_s),
$$

and the composite is the natural map.
