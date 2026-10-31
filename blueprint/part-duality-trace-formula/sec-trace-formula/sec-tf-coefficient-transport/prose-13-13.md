+++
id = "prose-13-13"
kind = "hidden"
title = "Integral, rational and algebraic coefficients"
order = 602
+++
We now extend the trace formula from finite coefficient rings to
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$. The steps are those of
Proposition [sk-prop-reduction-to-finite], but the statement is an equality of
traces in $\Lambda$ rather than an isomorphism, so we carry them out
directly. For $\mathcal O_E$ we reduce modulo
$\pi_E^n$. This works because both sides are traces of
perfect complexes, traces commute with reduction, and $\mathcal O_E$
embeds in $\varprojlim_n\mathcal O_E/\pi_E^n$. For $E$ we clear
denominators. A Frobenius correspondence $\psi_E$ with coefficients $E$,
even an invertible one, need not come from an integral one. Only some
multiple $\pi_E^N\psi_E$ does, and its integral model need not be
invertible. Hence this step needs the integral formula, and so the finite
one, for Frobenius correspondences that are not invertible. For $\overline{\mathbf Q}_\ell$ we descend to a finite extension of $\Ql$.

The Frobenius comparison $\kappa_m$ of
Lemma [sk-lem-tf-frobenius-convention] extends to the coefficient rings
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$. For $K\in\Dbc(X,\mathcal O_E)$ with
normalized tower of reductions $(K_n)$ modulo $\pi_E^n$
(Definition [sk-def-pe-derived-completion]), both $(\Phi_X^m)^*$ and
$\operatorname{Fr}_X^{m*}$ preserve derived completeness and commute
with reduction, so each is the derived limit of its values on the
$K_n$. Since the finite comparisons $\kappa_m$ come from a single functorial
identification on the classical site, they are compatible with
reduction of coefficients. Their derived limit is the integral
$\kappa_m$. Since the finite comparisons are compatible with iteration and
with the units of the pullbacks, so is the integral one, and hence it
identifies the endomorphisms $T_{c_m}$ with the geometric Frobenius operators as in
Lemma [sk-lem-tf-frobenius-convention].
For $E$ we localize on integral models, and by the localized Hom
comparison (10.20) the result does not depend on the choice of model. For $\overline{\mathbf Q}_\ell$ we
descend from finite extensions.
