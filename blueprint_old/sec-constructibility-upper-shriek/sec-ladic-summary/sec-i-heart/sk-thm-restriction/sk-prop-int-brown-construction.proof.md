+++
kind = "proof"
of = "det-prop-int-brown-construction"
+++
The construction of [sk-prop-sf-existence] is uniform in the coefficient
ring and needs, for $\Lambda=\mathcal O_E$, the hypotheses listed in
[sk-lem-brown-hypotheses]: proper direct image and extension by zero preserve
the localizing categories and direct sums there and preserve
$\Dctf=\Dbc$, and the projection and base change identifications used in
comparing compactifications hold on $\Dbc$. These are verified as follows.

- $j_!$: [det-cor-int-compactness-ii] ($j$ is quasi-compact, our schemes being
  Noetherian) gives that $j_!$ preserves $\Dbc(-,\mathcal O_E)$, the
  localizing categories and direct sums.
- $Rp_*$ for proper $p$: [sk-prop-int-compactness] gives the same three
  properties.
- Proper base change and the comparison $Rp_*j_!\simeq Rp'_*j'_!$ for two
  compactifications dominated by a third: on $\Dbc(-,\mathcal O_E)$ these are
  the integral case of [sk-thm-sfb-proper-base-change].

So the composite $Rp_*j_!$ is exact, preserves direct sums and maps
$\Dbc(X,\mathcal O_E)$ into $\Dbc(Y,\mathcal O_E)$. The comparison isomorphisms
between compactifications, the composition isomorphisms and the base change
isomorphisms are first constructed on $\Dbc$ by [sk-prop-sf-existence], then
extended to the localizing categories: natural transformations between exact
direct-sum preserving functors that are isomorphisms on the generators are
isomorphisms everywhere, since the objects on which they are isomorphisms
form a localizing subcategory.
