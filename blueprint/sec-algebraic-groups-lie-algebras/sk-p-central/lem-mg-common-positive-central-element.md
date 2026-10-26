+++
id = "lem-mg-common-positive-central-element"
kind = "lemma"
title = "A common positive-degree central element"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_pos_mem_center_mem_degreeComponent"]
order = 3751
uses = ["d-central", "d-monodromy", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "def-wf-semisimple-module", "lem-mg-degree-component-functoriality", "lem-mg-normal-restriction-semisimple", "lem-wf-degree-component-image", "p-central"]
+++
Let $\rho_1,\ldots,\rho_a$ be semisimple Weil representations
([def-wf-semisimple-module]) of one and the same degree datum
([d-monodromy]) over an algebraically closed field $k$ of characteristic
zero (such representations are geometrically semisimple by
[lem-mg-normal-restriction-semisimple]), and let
$\rho=\bigoplus_i\rho_i$, a semisimple represented degree datum. There
are an integer $m>0$ and

$$
z\in Z\bigl(G_{\mathrm{arith}}(\rho)\bigr)\cap G^{[m]}
$$

whose matrix under $(h,n)\mapsto hF^n$ lies in the centre $Z(G)(k)$.
Thus all $W$-stable subquotients of all the $\rho_i$ may be measured
using images of one and the same degree-$m$ element, via the
functoriality of [lem-mg-degree-component-functoriality].
