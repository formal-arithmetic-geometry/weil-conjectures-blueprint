+++
kind  = "proof"
of    = "thm-galois-fundamental"
+++
By [lem-fet-galois-category] the pair
$(\mathrm{F\acute Et}(Y),F_{\bar y})$ is a Galois category, so
[thm-galois-abstract-equivalence] applies with
$G=\operatorname{Aut}(F_{\bar y})$, which is profinite by
[lem-galois-aut-profinite]; this is the equivalence for
$\operatorname{Aut}(F_{\bar y})$. For a general fundamental group
$\pi_1(Y,\bar y)$ of [def-galois-fibre-functor], its action defines a
homomorphism $\pi_1(Y,\bar y)\to\operatorname{Aut}(F_{\bar y})$ which is
a continuous bijection of compact Hausdorff groups, hence an isomorphism
of topological groups, and restriction of the action along it identifies
continuous $\operatorname{Aut}(F_{\bar y})$-sets with continuous
$\pi_1(Y,\bar y)$-sets compatibly with the forgetful functors. The
statement for $\mathrm{FLC}(Y)$ follows by composing with the
equivalence of [thm-galois-lc-etale]. An equivalence of categories
preserves all limits and colimits that exist.
