+++
kind  = "proof"
of    = "lem-wft-kunneth-compatibilities"
+++
*(1).* Each arrow is an isomorphism: the composition isomorphism and the
projection formula by [fix-prop-projection-formula] (the second variable
$v^*L$, resp. $Rb_!L$, lies in $\Dbc$ over a field, hence has finite Tor
amplitude), and the base change $a^*Rb_!L\cong Ru_!v^*L$ by [det-prop-sf-cbc].
The relative Künneth map of [thm-sf-kunneth-relative] is the composite of
the same three kinds of arrows, applied in the other order of the factors
(first to $q=u$ with the variable $K$, then to $g$); the two composites
agree after the symmetry because the projection formula and the
exchange transformation are compatible with the symmetry of $\otimes^L$ and
with composition (the coherences listed in [thm-sf-kunneth-relative]).

*(2).* The geometric Frobenius pullbacks commute with composition
isomorphisms, with projection formulas and with base change morphisms
([prop-pur-weil-equivariance-compatibilities]); hence $\kappa$ intertwines
the Weil structures induced on both sides.

*(3).* The map $u$ is the base change of $b$, hence smooth of relative
dimension $e$, and by the base change of the purity isomorphism
([sk-prop-sp-purity-bc]) the trace $\operatorname{Tr}_u$ corresponds to
$a^*\operatorname{Tr}_b$ under $Ru_!v^*\cong a^*Rb_!$. By transitivity of the
smooth trace ([sk-prop-sp-trace-composition]) for $c=a\circ u$,
$\operatorname{Tr}_c=\operatorname{Tr}_a\circ Ra_!(\operatorname{Tr}_u)$,
and through the projection formula for $a$ this is
$\operatorname{Tr}_a\otimes\operatorname{Tr}_b$.
