+++
id = "lemma-continuity-ext-out-constructible-complex"
kind = "lemma"
title = "Continuity of Ext"
order = 280
lean = ["AlgebraicGeometry.ProEtale.constructible_ext_continuity", "AlgebraicGeometry.ProEtale.bounded_constructible_ext_generated"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-constructible-sheaves", "definition-lisse-sheaves"]
+++
Let $(K_\alpha^\bullet)$ be a filtered diagram of complexes of
$\Lambda_X$-modules that all vanish below a fixed degree, and let $M$ be
one of the following:

1. an object of $\Dbc(X,\Lambda)$, where $\Lambda=E$ or $\overline{\mathbf Q}_\ell$;
2. a finite extension of sheaves $a_!L_0$, with $a:S\hookrightarrow X$
   locally closed and $L_0$ a finite locally free $\mathcal O_{E,S}$-module,
   where $\Lambda=\mathcal O_E$.

Then for every integer $n$ the natural map

$$
\varinjlim_\alpha\Hom(M,K_\alpha^\bullet[n])
\longrightarrow
\Hom\bigl(M,(\varinjlim_\alpha K_\alpha^\bullet)[n]\bigr)
$$

is an isomorphism.
