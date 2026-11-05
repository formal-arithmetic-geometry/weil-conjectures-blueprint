+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--7"
order = 1150014
uses = ["lemma-degree-zero-top-cohomology--5", "lemma-degree-zero-top-cohomology--2", "lemma-filtrations-spectra"]
+++
Apply [lemma-degree-zero-top-cohomology--5] to $\mathcal F^\vee$.
Every global Frobenius eigenvalue has a positive power occurring at a
closed point. The stalk of $\mathcal F^\vee$ is the dual of the stalk
of $\mathcal F$, so this gives purity of
$\Gamma(X,\mathcal F^\vee)$ of weight $-a$. Dualizing gives purity of
$Q(\mathcal F)$ of weight $a$.

For an affine curve, [lemma-degree-zero-top-cohomology--2] identifies
$H_c^2$ with $Q(\mathcal F)(-1)$. The twist raises the weight by two.
The Lean theorem obtains this conclusion by applying
`AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_directImage_two`
to the identity immersion and transporting along $\operatorname{id}_*\mathcal F\simeq\mathcal F$;
unfolding that argument gives precisely the coinvariant calculation
and Tate twist above.
