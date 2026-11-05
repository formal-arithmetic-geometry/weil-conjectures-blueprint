+++
id = "prose-12-20"
kind = "hidden"
title = "$\\ell$-adic coefficients (1)"
order = 1010
+++
To pass from finite coefficient rings to $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$
we follow the steps of
Proposition [proposition-isomorphisms-reduce-finite-coefficients]. Since the statement is now an equality of traces in $\Lambda$ rather than an isomorphism, we carry the steps out
directly. First, for $\mathcal O_E$ we reduce modulo $\pi_E^n$. This works because both sides are traces of
perfect complexes, traces commute with reduction, and $\mathcal O_E$
embeds in $\varprojlim_n\mathcal O_E/\pi_E^n$. Next, for $E$ we clear denominators: a Frobenius correspondence $\psi_E$ with coefficients $E$ need not
come from an integral one; only some multiple $\pi_E^N\psi_E$ does, and this
integral model need not be invertible even when $\psi_E$ is
(Lemma [lemma-integral-models-rational-frobenius-correspondences]). This is
why we prove the formula for correspondences that are not invertible. Finally, for $\overline{\mathbf Q}_\ell$ we descend to a finite extension of $\mathbf Q_\ell$.

The Frobenius comparison $\kappa_m$ of
Lemma [lemma-scheme-frobenius-geometric-frobenius] extends to the coefficient rings
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$. Let $K\in\Dbc(X,\mathcal O_E)$ have
tower of reductions $(K_n)$ modulo $\pi_E^n$
(Definition [definition-derived-adic-completeness]). Both $(\Phi_X^m)^*$ and
$\operatorname{Fr}_X^{m*}$ preserve derived completeness and commute
with reduction, so each is the derived limit of its values on the
$K_n$. The finite comparisons $\kappa_m$ come from a single functorial
identification on the classical site. Hence they are compatible with
reduction of coefficients, and their derived limit is the integral
$\kappa_m$. The finite comparisons are compatible with iteration and
with the units of the pullbacks, and therefore so is the integral one. It follows that
the integral $\kappa_m$ identifies the endomorphisms $T_{c_m}$ with the geometric Frobenius operators as in
Lemma [lemma-scheme-frobenius-geometric-frobenius].
For $E$ we localize on integral models. By the localized Hom
comparison (9.21) the result does not depend on the choice of model. For $\overline{\mathbf Q}_\ell$ we
descend from finite extensions.
