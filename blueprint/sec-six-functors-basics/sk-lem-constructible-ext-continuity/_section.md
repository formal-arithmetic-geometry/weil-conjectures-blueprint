+++
id = "sk-lem-constructible-ext-continuity"
kind = "lemma"
title = "Continuity of Ext out of a constructible complex"
order = 1561
uses = ["sk-lem-bounded-continuity", "sk-lem-formal-closed-support", "sk-cor-coefficient-heart-ii"]
tags = ["sketch"]
+++
Let $\Lambda=E$, $\Qlb$ or $\cO_E$. Let $C\in D(X_{\mathrm{proét}},\Lambda)$ be obtained by finitely
many extensions and shifts from sheaves $a_!L$, with $a\colon S\hookrightarrow X$ a locally
closed immersion and $L$ a finite locally free $\Lambda_S$-module. Let $(K_i^\bullet)$ be a
filtered diagram of complexes of $\Lambda_X$-modules that all vanish below a fixed degree.
Then for every integer $q$ the natural map of $\Hom$ groups in $D(X_{\mathrm{proét}},\Lambda)$
$$
\varinjlim_i\Hom(C,K_i^\bullet[q])\longrightarrow\Hom\bigl(C,(\varinjlim_iK_i^\bullet)[q]\bigr)
$$
is an isomorphism. The hypothesis on $C$ holds:

1. for every $C\in\Dbc(X,\Lambda)$ if $\Lambda=E$ or $\Qlb$, by [sk-cor-coefficient-heart-ii];
   in particular, for $C\in\Cons(X,\Lambda)$ the functors $\Ext^q_\Lambda(C,-)$ commute with
   filtered colimits of $\Lambda_X$-modules;
2. for every finite extension of sheaves $a_!L_0$ with $L_0$ a finite locally free
   $\cO_{E,S}$-module, if $\Lambda=\cO_E$.
