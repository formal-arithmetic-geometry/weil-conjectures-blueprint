+++
kind = "proof"
of = "theorem-sp-qbar"
order = 792
uses = ["proposition-exceptional-inverse-image-smooth-morphism", "lemma-change-coefficients-compact-support", "proposition-isomorphisms-reduce-finite-coefficients", "theorem-smooth-base-change-all-admissible", "definition-exceptional-base-change-map", "lemma-passing-schematic-closure"]
+++
As for $E$, we compare Hom groups, now as colimits over finite extensions
instead of after inverting $\ell$.
By Proposition [proposition-dctf-x-qbar-2-colimit], $\Dbc(T,\overline{\mathbf Q}_\ell)$ is the $2$-colimit of the categories
$\Dbc(T,F)$ over finite extensions $F$ of $\mathbf Q_\ell$, so its Hom groups are the colimits of
those over $F$. The functors $Rf_!$ and $f^*$ commute with extension of scalars
(Section [sec-Change-of-coefficients]). Choosing models over some $E$, the adjunctions of
Proposition [proposition-sp-rational] over the fields $F\supset E$ are compatible with the
transition maps, and their colimit is the asserted bijection.
