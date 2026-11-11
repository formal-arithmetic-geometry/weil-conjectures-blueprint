+++
id = "lemma-inverse-image-tensor-product--6"
kind = "lemma"
title = "Open–closed locality"
order = 494012
aliases = ["bp-r149-6"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_of_openClosed"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8"]
+++
Let $\Lambda$ be a commutative condensed ring, let $j:U\hookrightarrow X$
be a quasi-compact open immersion, and let $i:Z\hookrightarrow X$ be a
closed immersion with image $X\setminus j(U)$. If
$K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ satisfies

$$
\mathbf Lj^*K\in\Dbc(U,\Lambda),\qquad
\mathbf Li^*K\in\Dbc(Z,\Lambda),
$$

then $K\in\Dbc(X,\Lambda)$. No Noetherian hypothesis is required.
