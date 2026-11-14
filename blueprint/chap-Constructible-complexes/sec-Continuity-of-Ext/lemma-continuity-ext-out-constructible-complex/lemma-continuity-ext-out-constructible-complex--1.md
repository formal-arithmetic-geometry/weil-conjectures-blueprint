+++
id = "lemma-continuity-ext-out-constructible-complex--1"
kind = "lemma"
title = "Continuity of Ext (1)"
name_showing = false
order = 280001
aliases = ["bp-r084-1"]
lean = ["AlgebraicGeometry.ProEtale.constructible_ext_continuity"]
uses = ["definition-lisse-sheaves", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1"]
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
