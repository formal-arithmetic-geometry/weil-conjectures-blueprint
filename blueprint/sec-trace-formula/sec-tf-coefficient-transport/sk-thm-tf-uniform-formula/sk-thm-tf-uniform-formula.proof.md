+++
kind = "proof"
of = "sk-thm-tf-uniform-formula"
uses = ["sk-lem-tf-frobenius-convention", "sk-def-pe-derived-completion", "sk-thm-trace-formula", "sk-prop-tf-transport-integral", "sk-lem-tf-rational-model", "sk-p-trace", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-finite", "sk-prop-scalar-six", "sk-thm-tf-coefficient-morphism-formula", "sk-prop-qlbar-two-colimit"]
+++
For finite $A$, we apply Theorem [sk-thm-tf-coefficient-morphism-formula]
to $\psi=\phi\kappa_1$. Lemma [sk-lem-tf-frobenius-convention] identifies
$T_{c_m}(\psi_m)$ with $\operatorname{Frob}_{X,K}^m$ and, at each fixed
point, $\psi_{m,\bar y}$ with $\operatorname{Frob}_{y,m}$. For
$\mathcal O_E$, composing the Weil structure with the comparison
$\kappa_1$ between the scheme Frobenius and the geometric Frobenius, we get a
Frobenius correspondence $\Phi_X^*K\to K$. The endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure by the integral form of
Lemma [sk-lem-tf-frobenius-convention], so the identity follows from
Proposition [sk-prop-tf-transport-integral]. Taking
$E=\Ql$ gives the case of $\Zl$.

For coefficients $E$, the Weil structure composed with $\kappa_1$ is a
Frobenius correspondence $\psi_E$, and the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure by the rational form of
Lemma [sk-lem-tf-frobenius-convention]. We apply
Lemma [sk-lem-tf-rational-model] to $\psi_E$, apply (13.1) to $(K_0,\theta)$,
extend scalars to $E$, and multiply by $\pi_E^{-Nm}$. By linearity of
categorical traces and their compatibility with extension of scalars
(Proposition [sk-p-trace]), together with
(13.2), this gives the identity for every $m$.
The case $E=\Ql$ gives the case of $\Ql$.

For $\overline{\mathbf Q}_\ell$, by Proposition [sk-prop-qlbar-two-colimit] the complex $K$, its
Weil structure $\phi$ and $\phi^{-1}$ descend to a common finite extension
$E/\Ql$, and after a further finite extension the two identities saying
that these maps are inverse to each other hold as well. Thus we get a
Weil complex at a finite stage, and extension
of scalars carries its formula over $E$ to (13.3). For
another representative, an isomorphism compatible with the Weil
structures descends to a common finite extension, and the resulting
operators are conjugate. Since the trace is compatible with extension
of scalars and invariant under conjugation, the result does not depend
on the stage or on the representative.

The complexes are perfect by Lemma [sk-lem-finite]. Compatibility
with the change-of-coefficients maps holds because the pullbacks, the
endomorphisms $T_{c_m}$ and the iterated Frobenius correspondences commute with the
comparisons of Proposition [sk-prop-scalar-six]. Finally, over a field
the categorical trace is the alternating trace on cohomology by
Proposition [sk-p-trace], and this proves
(13.4).
