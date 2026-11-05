+++
id = "lemma-uniform-ext-bound"
kind = "lemma"
title = "Uniform Ext bound"
order = 446
lean = ["AlgebraicGeometry.ProEtale.HasUniformConstructibleExtBound", "AlgebraicGeometry.ProEtale.CondensedRing.hasUniformConstructibleExtBound_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.hasUniformConstructibleExtBound_padicAlgClRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local"]
+++
For every $C\in\Cons(X,\Lambda)$ there is an integer $d_C\geq0$ such that

$$
\Ext^q(C,N)=0
\qquad\text{for all }q>d_C\text{ and all }N\in\Cons(X,\Lambda).
$$
