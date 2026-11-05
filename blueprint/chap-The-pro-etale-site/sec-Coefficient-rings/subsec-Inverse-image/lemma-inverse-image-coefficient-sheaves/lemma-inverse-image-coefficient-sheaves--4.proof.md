+++
kind = "proof"
of = "lemma-inverse-image-coefficient-sheaves--4"
order = 187008
uses = ["prose-02-50", "prose-02-51"]
+++
Choose an $E$-basis $e_1,\ldots,e_d$ of $E'$, with $d=[E':E]$.
Its coordinate functions are continuous, since they are
$\mathbf Q_\ell$-linear maps between finite-dimensional normed
$\mathbf Q_\ell$-spaces. Thus

$$
\underline E^{\oplus d}\longrightarrow\underline{E'},
\qquad (a_i)\longmapsto\sum_i e_i a_i,
$$

is an isomorphism of condensed abelian groups, whose inverse consists of
the coordinate functions. The additive strong monoidal functor $p_X^*$
of [prose-02-51] carries this to the corresponding basis map
$E_X^{\oplus d}\to E'_X$. The map is $E_X$-linear, and the forgetful
functor from $E_X$-modules reflects isomorphisms. Taking its inverse gives
the displayed isomorphism, with the same $d$ for every $X$.
