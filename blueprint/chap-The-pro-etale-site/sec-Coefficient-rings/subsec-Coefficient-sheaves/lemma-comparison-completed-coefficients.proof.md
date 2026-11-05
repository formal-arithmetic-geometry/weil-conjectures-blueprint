+++
kind = "proof"
of = "lemma-comparison-completed-coefficients"
order = 179
uses = ["proposition-topos-functoriality"]
+++
The functor $p_X^*$ commutes with colimits, so the second and third
isomorphisms reduce to identities on the point. The first is an inverse
limit, and since $p_X^*$ need not commute with inverse limits, we use
instead that $\underline{\mathcal O_E}$ is representable.

On the point, $\underline{\mathcal O_E}$ is represented by the profinite
set $\mathcal O_E=\varprojlim_n\mathcal O_E/\pi_E^n$, so its pullback to
$X$ is represented by the pro-étale $X$-scheme
$\varprojlim_n\coprod_{\mathcal O_E/\pi_E^n}X$. By the Yoneda lemma the
sheaf this scheme represents is $\varprojlim_n(\mathcal O_E/\pi_E^n)_X$,
and the ring structures match.

A continuous map from a profinite set to $E$ has compact image, and hence
lands in $\ell^{-m}\mathcal O_E$ for some $m$. Thus
$\underline E=\underline{\mathcal O_E}[1/\ell]$ on the point. Since
inverting $\ell$ is a filtered colimit and $p_X^*$ commutes with colimits,
we obtain the second isomorphism. In the same way the third follows from
$\underline{\overline{\mathbf Q}_\ell}=\varinjlim_E\underline E$. All three isomorphisms are
obtained by applying $p_X^*$, and $p_Y\circ f=p_X$ for every morphism
$f:X\to Y$, so they are compatible with pullback.
