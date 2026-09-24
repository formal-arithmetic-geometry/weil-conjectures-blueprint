+++
id = "rem-ptr-fd-artin-schreier-sheaf-1"
kind = "remark"
title = "Pointer to the properties of [def-fd-artin-schreier-sheaf]"
order = 4141
uses = ["def-fd-artin-schreier-sheaf", "lem-fd-as-characters"]
+++
In the notation of [def-fd-artin-schreier-sheaf], the following holds. The *Artin–Schreier sheaf attached to
$(\psi,f)$* is the $\overline{\mathbf Q}_\ell$-sheaf
associated to the finite etale Artin–Schreier covering

$$
\pi:Y\to X_0,\qquad
Y=\operatorname{Spec}\mathcal O_{X_0}[T]/(T^p-T-f),
$$

whose $\overline{\mathbf Q}_\ell$-pushforward is given the
$\mathbf F_p$-equivariant
structure coming from the translation $T\mapsto T+a$: precisely,
$\mathcal L_{\psi,f}$ is the *$\psi$-isotypic component* of
$\pi_*\overline{\mathbf Q}_\ell$, i.e. the image of the idempotent

$$
e_\psi=\frac1p\sum_{a\in\mathbf F_p}\psi(-a)\,\sigma_a,
\qquad
\sigma_a:\ T\mapsto T+a
\quad\text{on }\pi_*\overline{\mathbf Q}_\ell,
$$

in the group algebra of the $\mathbf F_p$-action of the
Artin–Schreier covering below, so that

$$
\mathcal L_{\psi,f}:=e_\psi\cdot\pi_*\overline{\mathbf Q}_\ell
\;\subseteq\;\pi_*\overline{\mathbf Q}_\ell
$$

(the isotypic decomposition of the pushforward along the finite etale
covering $\pi$, and the fact that every isotypic component is lisse of
rank one, is proved in [lem-fd-as-characters]: the total pushforward
$\pi_*\overline{\mathbf Q}_\ell$ is lisse of rank $p$ and is the
direct sum of the $p$ one-dimensional isotypic components, and the
*Artin–Schreier sheaf* proper is the rank-one isotypic part, with
the sign for which the trace lemma below holds); the line sheaf
$\mathcal L_\psi:=\mathcal L_{\psi,0}$ on the affine line is the
*Artin–Schreier (exponential) sheaf*.
