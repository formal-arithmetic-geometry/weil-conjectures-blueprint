+++
kind = "proof"
of = "theorem-poincare-duality"
order = 857
uses = ["proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "proposition-proper-base-change-etale-site", "theorem-global-verdier-duality"]
+++
The theorem is global duality rewritten by means of smooth purity: once
$\omega_X$ and $\mathbb D_XK$ are identified, the pairing of
Theorem [theorem-global-verdier-duality] becomes $\beta_K$.

Corollary [corollary-dualizing-complex-smooth-scheme] identifies $\omega_X$.
Since internal Hom commutes with tensoring its second variable by an
invertible Tate twist and a shift, we get the
displayed description of $\mathbb D_XK$. If $K$ is locally
perfect, then locally $K$ is represented by a bounded complex of finite projective
modules, whose dual is the termwise dual, with the usual evaluation.

Next, $\beta_K$ is the pairing of
Theorem [theorem-global-verdier-duality] for $K$, transported along the
isomorphism $\omega_X\simeq\Lambda_X(d)[2d]$. Indeed, under this isomorphism evaluation
$K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$ becomes evaluation on
coefficients $K\otimes^{\mathbf L}K^\vee(d)[2d]\to\Lambda_X(d)[2d]$.
Moreover, the trace map of Definition [definition-trace-map] is by definition the
counit $\varepsilon_{a_X}$ precomposed with $\gamma_{a_X}$, so the
counit becomes $\operatorname{Tr}_X$. Hence the adjoint of $\beta_K$ is
the isomorphism (10.5), which is
(10.8). By Lemma [lemma-perfect-complexes-geometric-point]
both factors of $\beta_K$ are perfect complexes. Since the adjoint of
$\beta_K$ is an isomorphism, $\beta_K$ is perfect.

For proper $X$ we have $Ra_{X!}=Ra_{X*}$, which gives the
assertion on proper $X$. The last statement holds because the pairing is built from tensor
products, the two direct images, evaluation, the isomorphism $\gamma_{a_X}$ and
the trace map, all of which Proposition [proposition-six-operations-change-coefficients] and
Theorem [theorem-smooth-purity-all-admissible-coefficients] show to be
compatible with every coefficient map.
