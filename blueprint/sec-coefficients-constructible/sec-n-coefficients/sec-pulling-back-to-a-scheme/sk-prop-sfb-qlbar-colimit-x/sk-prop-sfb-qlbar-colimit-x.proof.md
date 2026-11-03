+++
kind = "proof"
of = "sk-prop-sfb-qlbar-colimit-x"
uses = ["sk-prop-pe-condensed-point", "def-sfb-integers-to-subfield"]
+++
On the point, $\underline{\mathcal O_E}$ is represented by the profinite
set $\mathcal O_E=\varprojlim_n\mathcal O_E/\pi_E^n$, so its pullback to
$X$ is represented by the pro-étale $X$-scheme
$\varprojlim_n\coprod_{\mathcal O_E/\pi_E^n}X$. By the Yoneda lemma the
sheaf this scheme represents is $\varprojlim_n(\mathcal O_E/\pi_E^n)_X$,
and the ring structures match. We use the representing scheme here
because $p_X^*$ commutes with colimits but in general not with inverse
limits.

A continuous map from a profinite set to $E$ has compact image, and hence
lands in $\ell^{-m}\mathcal O_E$ for some $m$. Thus
$\underline E=\underline{\mathcal O_E}[1/\ell]$ on the point. Since $p_X^*$
commutes with colimits and inverting $\ell$ is a filtered colimit, this gives
the second isomorphism. The third follows in the same way from
$\underline{\overline{\mathbf Q}_\ell}=\varinjlim_E\underline E$, since $p_X^*$ commutes with
filtered colimits. All three are built
from $p_X^*$, so they are compatible with pullback.
