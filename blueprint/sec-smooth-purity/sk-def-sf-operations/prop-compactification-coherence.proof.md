+++
kind  = "proof"
of    = "prop-compactification-coherence-detailed"
+++
We prove coherence on the full subcategory of complexes
$K=\nu_X^*L$ with $L\in D^+(X_{\Et},A)$, using the comparison
pullback of [def-weil-pbc-site-comparison-morphism].
This includes bounded constructible complexes coming from the etale
site. A refinement satisfies $u j_1=j_2$
by [def-weil-compactifications-refinements]. Use the inverse of
the canonical isomorphism of
[lem-weil-pbc-proper-open-comparison-proetale]:

$$
\alpha_u^{-1}:Ru_*j_{1!}\xrightarrow{\sim}j_{2!}.
$$

The composition isomorphism for derived direct images at finite level,
[lem-weil-derived-direct-image-composition] (1), gives
$R\bar f_{1*,n}\simeq R\bar f_{2*,n}Ru_*$.
Composing with $R\bar f_{2*,n}(\alpha_u^{-1})$ therefore gives the
claimed map of candidates from [def-weil-compact-support-candidate].
It is the identity for an identity refinement, and the composition law
for $\alpha$ makes these maps transitive.

Finally, [prop-compactification-refinement] gives a common
refinement $d$ of any two compactifications. If
$t_i:Rf_{!,n}^{d}\xrightarrow{\sim}Rf_{!,n}^{c_i}$ are its maps,
the comparison from $c_1$ to $c_2$ is $t_2t_1^{-1}$.
Given another choice $d'$, choose a refinement mapping to both.
The two resulting maps to each $c_i$ can be made equal by the
parallel-refinement clause; do this for the two $c_i$ successively.
Transitivity then makes the two expressions $t_2t_1^{-1}$ equal.
For three compactifications choose one common refinement, so that
$(t_3t_2^{-1})(t_2t_1^{-1})=t_3t_1^{-1}$.
This proves independence and the cocycle condition on the indicated
full subcategory.

The statement on all of $D(X_{\mathrm{proet}},A)$ is no longer part of
the claim: the domain declared in
[def-weil-compact-support-candidate] is the subcategory of complexes
coming from the etale site with a witness, which is exactly the domain on
which the comparison above is proved, so the proposition is complete on its
declared domain. A comparison on complexes without an etale origin would
need proper base change for the complex itself; every proper base-change
statement of the proper-base-change chapter assumes either torsion cohomology and boundedness
below on the etale site or an etale-origin witness, so no such extension is
available, and none is used.
