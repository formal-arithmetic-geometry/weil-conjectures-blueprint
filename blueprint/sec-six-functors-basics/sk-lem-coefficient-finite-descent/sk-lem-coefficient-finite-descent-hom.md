+++
id = "det-lem-coefficient-finite-descent-hom"
kind = "lemma"
title = "Morphisms in $D^b_c(X,\\overline{\\mathbf Q}_\\ell)$ descend to a finite extension"
uses = ["sk-lem-constructible-ext-continuity", "lem-sfb-subfield-flat", "lem-sfb-qlbar-flat", "sk-prop-sfb-qlbar-colimit-x"]
+++
Let $X$ be a standing scheme, $E/\mathbf Q_\ell$ finite and $C,D\in\Dbc(X,E)$. For finite
$F\supseteq E$ and every $r\in\mathbf Z$:

1. $\Hom_{D(X,F)}(C_F,D_F[r])\cong\Hom_{D(X,E)}(C,\operatorname{Res}D_F[r])$, and likewise over $\Qlb$,
   naturally in $F$;
2. if $D^\bullet$ is a bounded complex representing $D$, then $(D^\bullet\otimes_{E_X}F_X)_F$ is a
   filtered system of complexes of $E_X$-modules vanishing below the lower bound of $D^\bullet$,
   with colimit $D^\bullet\otimes_{E_X}\QbarX$;
3. the map $\varinjlim_F\Hom(C_F,D_F[r])\to\Hom(C_{\Qlb},D_{\Qlb}[r])$ is bijective.
