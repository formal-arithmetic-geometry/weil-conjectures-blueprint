+++
kind = "proof"
of = "lemma-flat-models-generators"
order = 256
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The flat model exists on the étale site by a classical result, and we
pull it back. The generators then come from two filtrations: the stupid
filtration of the model, and the filtration of each term by strata.

By Corollary [corollary-finite-tor-amplitude-under-comparison], $C=\nu_X^*C_{\acute{e}t}$ with
$C_{\acute{e}t}\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$, where
$\nu_X^*:D(X_{\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ is the comparison inverse
image. By [Stacks, [0F4M](https://stacks.math.columbia.edu/tag/0F4M)] the complex $C_{\acute{e}t}$ has a bounded flat model, and
since $\nu_X^*$ is exact on sheaves, its pullback is a
bounded flat constructible model on $X_{\mathrm{pro}\acute{e}t}$. We choose a common stratification on
which its finitely many terms are locally constant. Their stalks are
finite projective, because a finite flat
module over the Noetherian ring $A$ is finite projective. If $F$ is a flat
constructible sheaf, then the exact sequences for the successive open and closed
strata express $F$ as a finite extension of the sheaves $a_!L$ attached to its
strata. Similarly, the stupid filtration of the bounded flat complex expresses
$C$ as a finite extension of shifts of its *terms*. Shifts and finite
extensions preserve finite Tor amplitude. The same argument proves the
corresponding statement on $X_{\acute{e}t}$, which we use in the proof of
Proposition [proposition-compactness-finite-coefficients] before passing to the pro-étale site.
