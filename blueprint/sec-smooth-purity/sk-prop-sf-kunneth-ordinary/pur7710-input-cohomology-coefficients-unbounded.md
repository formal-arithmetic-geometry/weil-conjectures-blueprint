+++
id = "pur7710-input-cohomology-coefficients-unbounded"
kind = "remark"
title = "Forgetting coefficient actions for unbounded complexes"
order = 2020
tags = ["latex:bpinput"]
uses = ["pur7710-lem-finite-type-module-cd"]
+++
Let $W$ be a $k$-scheme of finite type and $\rho:\mathcal O_E/\varpi^n\to\mathcal O_E/\varpi$ the reduction homomorphism. For every $K\in D(W_{\Et},\mathcal O_E/\varpi)$, unbounded, the comparison
$\operatorname{Res}_\rho R\Gamma_{W,\Et,\mathcal O_E/\varpi}K\to R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}\operatorname{Res}_\rho K$,
obtained from a K-injective resolution by the construction of Input “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]) with $\operatorname{Res}_\rho$ in place of $\operatorname{For}$, is an isomorphism in $D(\mathsf{Mod}_{\mathcal O_E/\varpi^n})$. *Status:* this is the unbounded form of Input “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]), expected because $W$ has finite cohomological dimension (Lemma [pur7710-lem-finite-type-module-cd]); it is the comparison used by `lem-pur-ordinary-kunneth-finite-ring`. Since $\rho$ is not flat for $n\geq2$, restriction of scalars need not preserve K-injective complexes, and this is not a consequence of the adjunction alone. It is imported; a formalization must provide the comparison for unbounded complexes, not only its cohomology in bounded degrees.
