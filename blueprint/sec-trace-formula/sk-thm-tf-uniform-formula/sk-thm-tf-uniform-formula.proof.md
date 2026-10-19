+++
kind = "proof"
of = "sk-thm-tf-uniform-formula"
uses = ["sk-lem-tf-frobenius-convention", "sk-def-pe-derived-completion", "sk-thm-trace-formula", "sk-prop-tf-transport-integral", "sk-lem-tf-rational-model", "sk-p-trace", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-finite", "sk-prop-scalar-six"]
+++
For finite and integral rings, (1) is an identity
of categorical traces of perfect complexes, which makes sense even
when the cohomology modules are not projective.

The Frobenius comparison $\kappa_m$ of
[sk-lem-tf-frobenius-convention] extends to the coefficient rings
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$. For $K\in\Dbc(X,\mathcal O_E)$ with
normalized reduction tower $(K_n)$ modulo $\pi_E^n$
([sk-def-pe-derived-completion]), both $(\Phi_X^m)^*$ and
$\operatorname{Fr}_X^{m*}$ preserve derived completeness and commute
with reduction, so each is the derived limit of its values on the
$K_n$. The finite comparisons $\kappa_m$ come from one functorial
identification on the classical site, hence are compatible with
reduction of coefficients; their derived limit is the integral
$\kappa_m$, with its iteration and adjoint-mate identities, and it
identifies the global operators with the geometric Weil operators.
For $E$ one localizes on integral models, the result being independent
of the model by the localized Hom comparison, and for $\overline{\mathbf Q}_\ell$ one
descends from finite extensions.

For finite $A$ the theorem is [sk-thm-trace-formula]. For
$\mathcal O_E$, compose the Weil structure with the comparison
$\kappa_1$ between scheme and geometric Frobenius to obtain a
Frobenius correspondence $\Phi_X^*K\to K$. Its compact and stalk operators
are those of the Weil structure, so
[sk-prop-tf-transport-integral] gives the identity. Taking
$E=\Ql$ includes $\Zl$.

For coefficients $E$, apply [sk-lem-tf-rational-model] to this
Frobenius correspondence. Apply the identity (1) of
[sk-prop-tf-transport-integral] to $(K_0,\theta)$,
extend scalars to $E$, and multiply by $\pi_E^{-Nm}$. Linearity and
scalar compatibility of categorical traces
([sk-p-trace]), together with the identities (1) of
[sk-lem-tf-rational-model], give the identity for every $m$.
The case $E=\Ql$ gives $\Ql$.

For $\overline{\mathbf Q}_\ell$, [sk-thm-sfb-qlbar-two-colimit] descends $K$, its
Weil map and the inverse of that map to a common finite extension
$E/\Ql$. The two inverse identities hold after a further finite
extension, so this is a Weil complex at a finite stage, and scalar
extension carries its $E$-formula to (1). If
another representative is chosen, an isomorphism respecting the Weil
maps descends to a common finite extension, and the resulting
operators are conjugate. Scalar compatibility and conjugation
invariance of the trace prove independence of the stage and of the
representative.

Point-perfectness is [sk-lem-finite]. Compatibility
with the coefficient comparisons holds because the pullbacks, global
operators and iterated Frobenius correspondences commute with the
comparisons of [sk-prop-scalar-six]. Finally, over a field
the categorical trace is the alternating trace on cohomology, by
[sk-p-trace], which proves (2).

The form of (2) for Weil complexes over $E$ and $\overline{\mathbf Q}_\ell$ in the
notation of the Weil-complex chapter, with the descent of the traces to a
finite coefficient field, is [det-thm-tf-uniform-formula-weil].
