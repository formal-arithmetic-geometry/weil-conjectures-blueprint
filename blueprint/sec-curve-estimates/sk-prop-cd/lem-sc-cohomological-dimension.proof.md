+++
kind  = "proof"
of    = "lem-sc-cohomological-dimension"
+++
Work on one of the finitely many disjoint integral components
of the smooth curve. By [lem-sc-generic-cohomology-comparison]
it suffices to treat $\eta_*M$. At a closed point the strict
local ring of $C$ is a discrete valuation ring, by
[lem-sc-smooth-regular], [lem-sc-regular-dim1-dvr] and preservation
of regularity and dimension under etale localization.
Its fraction field is algebraic over $k(C)$: a strict
henselization is a filtered union of etale neighborhoods and
their fraction fields are finite separable extensions.
By [prop-weil-pbc-strict-henselization-stalk-formula]
and [lem-sc-function-field-cd-one],
$R^q\eta_*M=0$ for $q>1$.
The sheaf $R^1\eta_*M$ has zero generic restriction, hence
is acyclic by [lem-sc-zero-generic-acyclic].

The ordinary Grothendieck spectral sequence of
[thm-sp-grothendieck] for sections composed with $\eta_*$
has terms $H^a(C,R^b\eta_*M)$ and converges to
$H^{a+b}(k(C),M)$. Direct image takes injectives to injectives
because its left adjoint is exact, so the required acyclicity
holds. The only row above $b=0$ is $b=1$, and its only
possibly nonzero term is at $a=0$. For total degree $q>2$
there are thus no differentials into or out of $H^q(C,\eta_*M)$.
It equals $H^q(k(C),M)=0$, by
[lem-sc-function-field-cd-one].
