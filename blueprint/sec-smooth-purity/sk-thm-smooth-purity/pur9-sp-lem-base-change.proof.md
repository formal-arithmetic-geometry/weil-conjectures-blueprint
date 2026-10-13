+++
kind = "proof"
of = "pur9-sp-lem-base-change"
uses = ["pur9-cs-def-bc", "pur9-cs-input-bc-model", "pur9-cs-lem-diagonal-square", "pur9-dnc-lem-base-change"]
+++
The fibre square of $f'$ is the base change of that of $f$, its diagonal is the base change of $\Delta$, and $T_{X'/Y'}=u^*T_{X/Y}$. Each step of $\Pi_f$ is compatible with this base change: the comparisons $\mu$ by the associativity of Lemma “Associativity of the finite-coefficient inverse-image comparison” (`pur713-lem-pull-composition-assoc`); the isomorphism of Lemma [pur9-cs-lem-diagonal-square], which is a map $b$ of Definition [pur9-cs-def-bc], by Input [pur9-cs-input-bc-composition] applied to the two factorizations of the composite Cartesian square $W'\to W\to X$ over $X'\to X\to Y$; $\delta$ by Lemma [pur9-dnc-lem-base-change]; and the vector-bundle step by Input [pur9-cs-input-bc-model] on étale trivializations. Composing these equalities gives the asserted one.
