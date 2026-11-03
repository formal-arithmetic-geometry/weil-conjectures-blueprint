+++
kind = "proof"
of = "sk-thm-sp-qbar"
uses = ["sk-prop-qlbar-two-colimit", "sk-prop-sp-rational", "sk-lem-sp-field-extension", "sk-prop-sf-comp-coherence"]
+++
By Proposition [sk-prop-qlbar-two-colimit], $\Dbc(T,\overline{\mathbf Q}_\ell)$ is the $2$-colimit of the categories
$\Dbc(T,F)$ over finite extensions $F$ of $\Ql$, so its Hom groups are the colimits of
those over $F$. The functors $Rf_!$ and $f^*$ commute with extension of scalars
(Section [sec-n-change]). Choosing models over some $E$, the adjunctions of
Proposition [sk-prop-sp-rational] over the fields $F\supset E$ are compatible with the
transition maps, and their colimit is the asserted bijection.
