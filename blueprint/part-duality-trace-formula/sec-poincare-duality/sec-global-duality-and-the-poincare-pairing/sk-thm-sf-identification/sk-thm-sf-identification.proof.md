+++
kind = "proof"
of = "sk-thm-sf-identification"
uses = ["sk-cor-sp-all-coefficients", "sk-thm-sf-global-duality", "sk-lem-finite"]
+++
Corollary [sk-cor-sp-all-coefficients] identifies $\omega_X$.
Since internal Hom commutes with tensoring its second variable by an
invertible Tate twist and a shift, we get the
displayed description of $\mathbb D_XK$. If $K$ is locally
perfect, then locally $K$ is represented by a bounded complex of finite projective
modules, the dual is its termwise dual, and evaluation is the usual evaluation.

It remains to see that $\beta_K$ is the pairing of
Theorem [sk-thm-sf-global-duality] for $K$, transported along the
isomorphism $\omega_X\simeq\Lambda_X(d)[2d]$. Then the adjoint of $\beta_K$ is
(11.4), which is an isomorphism, and this is
(11.7). Under this isomorphism, evaluation
$K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$ becomes evaluation on
coefficients $K\otimes^{\mathbf L}K^\vee(d)[2d]\to\Lambda_X(d)[2d]$.
The trace map of Definition [sk-def-sp-trace] is by definition the
counit $\varepsilon_{a_X}$ precomposed with $\gamma_{a_X}$, so the
counit becomes $\operatorname{Tr}_X$. By Lemma [sk-lem-finite]
both factors of $\beta_K$ are perfect complexes, and since its adjoint
is an isomorphism, $\beta_K$ is perfect.
If $X$ is proper, then $Ra_{X!}=Ra_{X*}$, which proves the
assertion on proper $X$. Finally, the pairing is built from tensor
products, the two direct images, evaluation, the isomorphism $\gamma_{a_X}$ and
the trace map, and Proposition [sk-prop-scalar-six] and
Theorem [sk-thm-purity-transport] compare all of these for every
coefficient map, which gives the last statement.
