+++
id = "sk-lem-constructible-ext-continuity"
kind = "lemma"
title = "Continuity of Ext out of a constructible complex"
order = 246
uses = ["sk-lem-coefficient-heart", "sk-def-sfb-constructible", "sk-cor-coefficient-heart-ii"]
tags = ["sketch"]
+++
Let $\Lambda=E$, $\overline{\mathbf Q}_\ell$ or $\mathcal O_E$. Let $M\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$
be obtained by finitely many extensions and shifts from sheaves $a_!L$,
with $a:S\hookrightarrow X$ a locally closed immersion and $L$ a finite
locally free $\Lambda_S$-module. Let $(K_\alpha^\bullet)$ be a filtered diagram
of complexes of $\Lambda_X$-modules that all vanish below a fixed degree.
Then for every integer $n$ the natural map

$$
\varinjlim_\alpha\Hom(M,K_\alpha^\bullet[n])
\longrightarrow
\Hom\bigl(M,(\varinjlim_\alpha K_\alpha^\bullet)[n]\bigr)
$$

is an isomorphism. The hypothesis on $M$ holds:

1. for every $M\in\Dbc(X,\Lambda)$ if $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, by
   Corollary [sk-cor-coefficient-heart-ii]; in particular, for
   $M\in\Cons(X,\Lambda)$ the functors $\Ext^n_\Lambda(M,-)$ commute with
   filtered colimits of $\Lambda_X$-modules;
2. for every finite extension of sheaves $a_!L_0$ with $L_0$ a finite
   locally free $\mathcal O_{E,S}$-module, if $\Lambda=\mathcal O_E$.
