+++
id = "rem-sp-general-base-field"
kind = "remark"
title = "Smooth purity over an arbitrary base field"
order = 3355
uses = ["sk-thm-purity-transport"]
+++
Theorem [sk-thm-purity-transport] is stated in the setting of these notes, where schemes
are of finite type over $k=\overline{\mathbf F}_q$. Nothing in the statement, and nothing
essential in the construction, needs $k$ to be algebraically closed or a finite field:
the theorem and its compatibilities hold verbatim for schemes separated of finite type
over any field $k$ of characteristic $p\neq\ell$. The Lean formalisation states it in that
generality, because the trace formula is applied to schemes $X_0$ over the finite field
$\mathbf F_q$ itself and not only to $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$.

Where a proof step genuinely uses that the base field is algebraically closed (for
instance a computation on geometric points, or a trivialization of $\Lambda(1)$ by roots of
unity), one reduces to that case by base change along $\pi:\operatorname{Spec}\bar k\to
\operatorname{Spec}k$: the map $\gamma_f$ is compatible with base change, and
$\pi_X^*$ is conservative on $D^b_{\mathrm{ctf}}(X,\Lambda)$ because $X_{\bar k}\to X$ is
surjective, so a morphism is an isomorphism as soon as its pullback to $X_{\bar k}$ is.
The convention $k=\overline{\mathbf F}_q$ is a convenience of exposition, not a
restriction of the theorem.
