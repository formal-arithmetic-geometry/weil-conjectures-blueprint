+++
id = "prose-02-02"
kind = "hidden"
title = "Weakly étale morphisms and the pro-étale site"
order = 25
+++
The objects one has in mind are inverse limits of étale $X$-schemes.
Being such a limit is a condition on a presentation, which is awkward to
work with, so we take as objects the weakly étale $X$-schemes of the
following definition. This class is defined by flatness conditions, so it is stable under
base change and composition, and membership in it is local for the
Zariski topology (Lemma [sk-lem-pe-weakly-etale-stability]). Conversely,
after a faithfully flat refinement every weakly étale scheme becomes
a limit of étale schemes (Theorem [sk-thm-pe-indetale-refinement]).

Typical examples are the schemes that the étale site can only reach
through colimits. The strict henselization
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}$ is the limit of
the affine étale neighbourhoods of $\bar x$, and on $X_{\acute{e}t}$ it
appears only through the stalk at $\bar x$; on $X_{\mathrm{pro}\acute{e}t}$ it is an
object. Similarly
$\operatorname{Spec}\overline{\mathbf F}_q=\varprojlim_m\operatorname{Spec}\mathbf F_{q^m}$
is an object over $\operatorname{Spec}\mathbf F_q$, and for a profinite
set $S=\varprojlim S_i$ the scheme $X\times S=\varprojlim_i\coprod_{S_i}X$
is an object over $X$. The last family is what lets the site see
profinite sets, and hence the topology of $\Zl$.
