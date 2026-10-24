+++
kind  = "proof"
of    = "thm-fd-transform-well-defined"
uses = ["prop-kernel-lisse", "prop-functor-package", "sk-thm-sf-ctf-stability", "sk-prop-ctf-finite-comparison"]
+++
In both cases the kernel $\mathcal K_\psi$ of [def-fd-kernel] is lisse of
rank one, hence constructible and of finite Tor amplitude
([prop-kernel-lisse]).

*(1).* By [prop-functor-package] the derived pullback $Lp_1^*$, the derived
tensor product with the finite-Tor complex $\mathcal K_\psi$ and the
compact-support direct image $Rp_{2,!}$ along the separated finite-type
morphism $p_2$ are exact triangulated functors on the étale categories with
finite coefficients that preserve bounded constructible objects; hence
$Lp_1^*K\otimes^L_\Lambda\mathcal K_\psi\in D^b_c(V\times_SV',\Lambda)$ and
its image under $Rp_{2,!}$ lies in $D^b_c(V',\Lambda)$, by finiteness of
$Rp_{2,!}$ over the finite-type $k$-scheme $V'$; the shift $[r]$ of
[def-fd-transform] preserves boundedness and constructibility. For finite
admissible $\Lambda$ the pro-étale statement follows, because $\nu^*$
identifies the bounded constructible categories and commutes with the three
operations ([sk-prop-ctf-finite-comparison]).

*(2).* For $\Lambda=\mathcal O_E,E,\Qlb$ one has
$\Dctf(-,\Lambda)=\Dbc(-,\Lambda)$, and the operations $Lf^*$, $Rf_!$ and
$\otimes^{\mathbf L}$ of the condensed six-functor formalism preserve these
categories ([sk-thm-sf-ctf-stability]). Thus $Lp_1^*K$ and
$\mathcal K_\psi$ lie in $\Dbc(V\times_SV',\Lambda)$, so does their derived
tensor product, and $Rp_{2,!}$ of it lies in $\Dbc(V',\Lambda)$. Each of
these functors is exact, so $\operatorname{FT}_\psi$ is an exact functor
$\Dbc(V,\Lambda)\to\Dbc(V',\Lambda)$.
