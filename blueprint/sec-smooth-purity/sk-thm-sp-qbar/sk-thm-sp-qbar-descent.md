+++
id = "det-sp-qbar-finite-descent"
kind = "lemma"
title = "Finite diagrams of $\\overline{\\mathbf Q}_\\ell$-complexes descend to a finite extension"
order = 3035
uses = ["sk-thm-sfb-qlbar-two-colimit", "sk-prop-scalar-six"]
+++
Let $T$ be a scheme and $E/\Ql$ finite. By [sk-thm-sfb-qlbar-two-colimit] the
condensed category $\Dbc(T,\Qlb)$ is the $2$-colimit of the categories
$\Dbc(T,F)$ over finite extensions $F\supset E$ inside $\Qlb$, along the
extension-of-scalars functors; this is a theorem, not a definition. Then:

1. for $K,L\in\Dbc(T,E)$ and $q\in\mathbf Z$,
   $\varinjlim_{F\supset E}\Hom_{\Dbc(T,F)}(K_F,L_F[q])\xrightarrow{\sim}\Hom_{\Dbc(T,\Qlb)}(K_{\Qlb},L_{\Qlb}[q])$;
2. every finite diagram in $\Dbc(T,\Qlb)$ (finitely many objects and
   morphisms) satisfying finitely many relations (equalities of composites) is
   isomorphic to the extension of scalars of a diagram over some finite
   $F\supset E$ satisfying the same relations;
3. for $f:X\to Y$ separated of finite type, the functors $Rf_{!,\Qlb}$ and
   $f^*_{\Qlb}$ commute with extension of scalars from each finite $F$.
