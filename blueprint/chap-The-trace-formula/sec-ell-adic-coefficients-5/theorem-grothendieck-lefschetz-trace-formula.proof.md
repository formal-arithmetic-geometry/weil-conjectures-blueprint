+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula"
order = 1020
uses = ["proposition-w-local-components", "lemma-inverse-image-tensor-product", "definition-categorical-trace", "proposition-properties-trace", "corollary-trace-functions-direct-image-compact", "proposition-function-sheaf-dictionary", "remark-base-change-compactification"]
+++
In each case we turn the Weil structure into a Frobenius correspondence
by composing with $\kappa_1$, and we use
Lemma [lemma-scheme-frobenius-geometric-frobenius] to see that this does not change
the operators. We then treat the coefficient rings in the order
finite, integral, rational, algebraic, each case using the
previous one.

For finite $A$, we apply Theorem [theorem-trace-formula-frobenius-correspondence]
to $\psi=\phi\kappa_1$. Then Lemma [lemma-scheme-frobenius-geometric-frobenius] identifies $T_{c_m}(\psi_m)$ with $\operatorname{Frob}_{X,K}^m$ and, at each fixed
point, $\psi_{m,\bar y}$ with $\operatorname{Frob}_{y,m}$. Similarly, for $\mathcal O_E$, composing the Weil structure with
$\kappa_1$ we get a
Frobenius correspondence $\Phi_X^*K\to K$. By the integral form of
Lemma [lemma-scheme-frobenius-geometric-frobenius], the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure. The identity therefore follows from
Proposition [proposition-integral-trace-formula]. In particular, taking $E=\mathbf Q_\ell$ gives the case of $\mathbf Z_\ell$.

For coefficients $E$, the Weil structure composed with $\kappa_1$ is a
Frobenius correspondence $\psi_E$, and by the rational form of
Lemma [lemma-scheme-frobenius-geometric-frobenius] the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure. We apply
Lemma [lemma-integral-models-rational-frobenius-correspondences] to $\psi_E$, apply (12.1) to $(K_0,\theta)$,
extend scalars to $E$, and multiply by $\pi_E^{-Nm}$. By linearity of
categorical traces and their compatibility with extension of scalars
(Proposition [proposition-properties-trace]), together with
(12.2), this gives the identity for every $m$.
The case $E=\mathbf Q_\ell$ gives the case of $\mathbf Q_\ell$.

For $\overline{\mathbf Q}_\ell$, complexes and morphisms are colimits of their versions over
finite extensions, so it is enough to find the Weil complex over some
finite $E$ and to check that the answer does not depend on the choice.
By Proposition [proposition-dctf-x-qbar-2-colimit] the complex $K$, its
Weil structure $\phi$ and $\phi^{-1}$ descend to a common finite extension
$E/\mathbf Q_\ell$. After a further finite extension the two identities saying
that these maps are inverse to each other hold as well. Thus we get a
Weil complex at a finite stage, and by extension
of scalars its formula over $E$ gives (12.3). If we
choose another representative, any isomorphism compatible with the Weil structures descends to a common finite extension, so the resulting
operators are conjugate. Since the trace is compatible with extension of scalars and invariant under conjugation, the result does not depend
on the stage or on the representative.

The complexes are perfect by Lemma [lemma-perfect-complexes-geometric-point]. Compatibility
with the change-of-coefficients maps holds because the pullbacks, the
endomorphisms $T_{c_m}$ and the iterated Frobenius correspondences commute with the
comparisons of Proposition [proposition-six-operations-change-coefficients]. Finally, over a field
the categorical trace is the alternating trace on cohomology by
Proposition [proposition-properties-trace], and this proves
(12.4).
