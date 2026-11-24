+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula"
order = 1020
uses = ["proposition-w-local-components", "definition-pro-etale-base-change-map", "proposition-construction-independence-rf-shriek", "lemma-change-coefficients-compact-support", "definition-frobenius-operator", "proposition-properties-trace", "corollary-trace-functions-direct-image-compact", "proposition-weights-under-usual-operations", "theorem-nagata-s-compactification-theorem"]
+++
In each case we turn the [Weil structure](@definition-weil-structure) into a [Frobenius correspondence](@definition-frobenius-correspondences-their-operators)
by composing with [$\kappa_1$](@lemma-scheme-frobenius-geometric-frobenius), and we use
Lemma [lemma-scheme-frobenius-geometric-frobenius] to see that this does not change
the operators. We then treat the coefficient rings in the order
finite, integral, rational, algebraic, each case using the
previous one.

For finite $A$, we apply Theorem [theorem-trace-formula-frobenius-correspondence]
to $\psi=\phi\href{@lemma-scheme-frobenius-geometric-frobenius}{\kappa_1}$. Then Lemma [lemma-scheme-frobenius-geometric-frobenius] identifies [$T_{c_m}(\psi_m)$](@definition-frobenius-correspondences-their-operators) with [$\operatorname{Frob}_{X,K}^m$](@definition-frobenius-operator) and, at each fixed
point, $\psi_{m,\bar y}$ with $\operatorname{Frob}_{y,m}$. Similarly, for $\mathcal O_E$, composing the [Weil structure](@definition-weil-structure) with
[$\kappa_1$](@lemma-scheme-frobenius-geometric-frobenius) we get a
[Frobenius correspondence](@definition-frobenius-correspondences-their-operators) $\Phi_X^*K\to K$. By the integral form of
Lemma [lemma-scheme-frobenius-geometric-frobenius], the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the [Weil structure](@definition-weil-structure). The identity therefore follows from
Proposition [proposition-integral-trace-formula]. In particular, taking $E=\mathbf Q_\ell$ gives the case of $\mathbf Z_\ell$.

For coefficients $E$, the [Weil structure](@definition-weil-structure) composed with [$\kappa_1$](@lemma-scheme-frobenius-geometric-frobenius) is a
[Frobenius correspondence](@definition-frobenius-correspondences-their-operators) $\psi_E$, and by the rational form of
Lemma [lemma-scheme-frobenius-geometric-frobenius] the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the [Weil structure](@definition-weil-structure). We apply
Lemma [lemma-integral-models-rational-frobenius-correspondences] to $\psi_E$, apply (12.1) to $(K_0,\theta)$,
extend scalars to $E$, and multiply by $\pi_E^{-Nm}$. By linearity of
[categorical traces](@definition-categorical-trace) and their compatibility with extension of scalars
(Proposition [proposition-properties-trace]), together with
(12.2), this gives the identity for every $m$.
The case $E=\mathbf Q_\ell$ gives the case of $\mathbf Q_\ell$.

For $\overline{\mathbf Q}_\ell$, complexes and morphisms are colimits of their versions over
finite extensions, so it is enough to find the [Weil complex](@definition-weil-structure) over some
finite $E$ and to check that the answer does not depend on the choice.
By Proposition [proposition-dctf-x-qbar-2-colimit] the complex $K$, its
[Weil structure](@definition-weil-structure) $\phi$ and $\phi^{-1}$ descend to a common finite extension
$E/\mathbf Q_\ell$. After a further finite extension the two identities saying
that these maps are inverse to each other hold as well. Thus we get a
[Weil complex](@definition-weil-structure) at a finite stage, and by extension
of scalars its formula over $E$ gives (12.3). If we
choose another representative, any isomorphism compatible with the [Weil structures](@definition-weil-structure) descends to a common finite extension, so the resulting
operators are conjugate. Since the trace is compatible with extension of scalars and invariant under conjugation, the result does not depend
on the stage or on the representative.

The complexes are perfect by Lemma [lemma-perfect-complexes-geometric-point]. Compatibility
with the [change-of-coefficients maps](@definition-change-of-coefficients-maps) holds because the pullbacks, the
endomorphisms [$T_{c_m}$](@definition-frobenius-correspondences-their-operators) and the iterated [Frobenius correspondences](@definition-frobenius-correspondences-their-operators) commute with the
comparisons of Proposition [proposition-six-operations-change-coefficients]. Finally, over a field
the [categorical trace](@definition-categorical-trace) is the alternating trace on cohomology by
Proposition [proposition-properties-trace], and this proves
(12.4).
