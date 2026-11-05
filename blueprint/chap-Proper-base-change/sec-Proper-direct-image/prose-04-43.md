+++
id = "prose-04-43"
kind = "hidden"
title = "Proper direct image"
order = 424
+++
Let $p:X\to Y$ be proper. We need to know, for every admissible
coefficient ring, that $Rp_*$ preserves $D^b_{\mathrm{ctf}}$ and satisfies proper
base change and the projection formula there, because the construction
of $Rf_!=Rp_*\circ j_!$ in Section [sec-Direct-image-with-compact-support] starts from
these facts. For $Y=\operatorname{Spec}k$ with $k$ algebraically closed,
they say that the cohomology groups $H^i(X,\overline{\mathbf Q}_\ell)$ of a proper $X$ are
finite-dimensional and vanish outside a bounded range of degrees.

For finite coefficients, constructibility and the Tor bound are
Proposition [proposition-proper-direct-image-finite-coefficients], and
the other admissible rings reduce to this case.

For $\mathcal O_E$, the complex $Rp_*K$ is derived
complete, and its reduction modulo $\pi_E$ is $Rp_*$ of the reduction of
$K$, so the integral constructibility criterion
(Proposition [proposition-integral-constructibility-criterion]) and derived Nakayama
(Lemma [lemma-reduction-derived-nakayama]) reduce everything to torsion
coefficients. For $E$ and $\overline{\mathbf Q}_\ell$ it suffices to treat the
generators $(a_!L_0)[1/\ell]$. Indeed, on bounded below complexes $Rp_*$
commutes with inverting $\ell$ and with extension of scalars to finite
extensions and to $\overline{\mathbf Q}_\ell$, since both are filtered colimits
(Corollary [corollary-continuity-cohomology]).
