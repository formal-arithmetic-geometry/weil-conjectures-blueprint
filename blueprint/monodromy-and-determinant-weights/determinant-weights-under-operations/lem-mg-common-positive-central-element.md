+++
id = "lem-mg-common-positive-central-element"
kind = "lemma"
title = "A common positive-degree central element"
order = 4116
uses = ["def-wf-geometric-semisimplicity", "lem-mg-degree-component-functoriality", "prop-wf-geometric-monodromy-semisimple", "prop-wf-positive-degree-centre"]
+++
Let $\mathcal F^{(1)}_0,\ldots,\mathcal F^{(a)}_0$ be
geometrically semisimple lisse
Weil sheaves on the same normal geometrically connected curve,
and let $\rho=\bigoplus_i\rho_i$. There are an integer $m>0$ and

$$
z\in Z\bigl(G_{\mathrm{arith}}(\rho)\bigr)\cap G^{[m]}.
$$

Thus all Weil subquotients of all the $\mathcal F^{(i)}_0$ may be
measured using images of one and the same degree-$m$ element, via the
functoriality of [lem-mg-degree-component-functoriality].

## Proof

The direct sum of semisimple geometric representations is semisimple by
the direct-sum definition in [def-wf-geometric-semisimplicity].
Applied to this direct sum, [prop-wf-geometric-monodromy-semisimple]
says that its geometric monodromy identity component is semisimple (the
finite cover in that proposition replaces the dense geometric subgroup by
the inverse image of precisely this identity component). The central
element proposition [prop-wf-positive-degree-centre] now supplies
the displayed $z$ and $m$. Its image on every subquotient has the same
degree and remains central by the functoriality of
[lem-mg-degree-component-functoriality].
