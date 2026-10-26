+++
id = "det-sp-purity-coefficient-change"
kind = "proposition"
title = "Purity and the smooth trace under change of coefficients"
order = 2846
uses = ["det-sp-integral-adjunction-bijection", "det-sp-integral-direct-image-tower", "det-sp-normalized-equivalence", "det-sp-tower-gamma", "det-sp-tower-gluing", "det-sp-reduction-compatibilities", "det-sp-rational-localized-hom", "det-sp-rational-adjunction", "det-sp-field-extension-towers", "det-sp-qbar-adjunction"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and $E/\Ql$ finite.
For an admissible $\Lambda$ write $\gamma_{f,\Lambda}$ for the purity
isomorphism of [sk-thm-purity-transport], $\varepsilon_{f,\Lambda}$ for the counit
of $Rf_{!,\Lambda}\dashv f^!_\Lambda$, and
$\operatorname{Tr}_{f,\Lambda}=\varepsilon_{f,\Lambda}\circ Rf_{!,\Lambda}(\gamma_{f,\Lambda})$
for the smooth trace of [sk-def-sp-trace]. All categories are the condensed
categories $\Dbc(-,\Lambda)$ of [def-sf-setting].

1. *Reduction to finite coefficients.* Let $K\in\Dbc(Y,\mathcal O_E)$ and
   $n\ge1$, and write $(-)_n=-\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\ell^n$.
   Let $b_n:(Rf_{!,\mathcal O_E}M)_n\xrightarrow{\sim}Rf_{!,\mathcal O_E/\ell^n}(M_n)$ be the
   isomorphism of [det-sp-integral-direct-image-tower], and let
   $c_n(K):(f^!_{\mathcal O_E}K)_n\to f^!_{\mathcal O_E/\ell^n}(K_n)$ be the
   transpose of $\varepsilon_{f,\mathcal O_E}(K)_n\circ b_n^{-1}$. Then $c_n(K)$ is an
   isomorphism, and, with the sources identified by
   $(f^*K(d)[2d])_n\simeq f^*(K_n)(d)[2d]$,
   $$
   c_n(K)\circ\gamma_{f,\mathcal O_E}(K)_n=\gamma_{f,\mathcal O_E/\ell^n}(K_n),
   \qquad
   \operatorname{Tr}_{f,\mathcal O_E}(K)_n\circ b_n^{-1}=\operatorname{Tr}_{f,\mathcal O_E/\ell^n}(K_n).
   $$
   Moreover $\gamma_{f,\mathcal O_E}(K)$ is, up to these identifications, the
   derived limit of the tower purity isomorphism
   $\gamma_{f,\bullet}(\operatorname{red}_YK)$ of [det-sp-tower-gamma], whose level
   $n$ is $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$. The same holds
   for the reductions to $A_{E,n}=\mathcal O_E/\pi_E^n$, composing with the finite
   coefficient comparisons along $\mathcal O_E/\ell^m\to A_{E,n}$ for
   $\ell^m\in\pi_E^n\mathcal O_E$.
2. *Inverting $\ell$.* Let $K_0\in\Dbc(Y,\mathcal O_E)$ and $K=K_0\otimes_{\mathcal O_E}E$
   in $\Dbc(Y,E)$; every object of $\Dbc(Y,E)$ is of this form. Let
   $b_E:(Rf_{!,\mathcal O_E}M_0)\otimes E\xrightarrow{\sim}Rf_{!,E}(M_0\otimes E)$ be the
   isomorphism of [det-sp-rational-localized-hom], and
   $c_E(K_0):(f^!_{\mathcal O_E}K_0)\otimes E\to f^!_E(K)$ the transpose of
   $(\varepsilon_{f,\mathcal O_E}(K_0)\otimes E)\circ b_E^{-1}$. Then $c_E(K_0)$ is an
   isomorphism and
   $$
   c_E(K_0)\circ\bigl(\gamma_{f,\mathcal O_E}(K_0)\otimes E\bigr)=\gamma_{f,E}(K),
   \qquad
   (\operatorname{Tr}_{f,\mathcal O_E}(K_0)\otimes E)\circ b_E^{-1}=\operatorname{Tr}_{f,E}(K).
   $$
3. *Extension of the coefficient field.* For finite $E\subset F$ inside $\Qlb$ and
   $K\in\Dbc(Y,E)$, the comparisons of [sk-lem-sp-field-extension] carry
   $\gamma_{f,E}(K)\otimes_EF$ to $\gamma_{f,F}(K_F)$ and
   $\operatorname{Tr}_{f,E}(K)\otimes_EF$ to $\operatorname{Tr}_{f,F}(K_F)$. Likewise,
   with the comparisons for $E\subset\Qlb$ (the transposes of the extended
   counits), $\gamma_{f,E}(K)\otimes_E\Qlb$ is carried to $\gamma_{f,\Qlb}(K_{\Qlb})$
   and $\operatorname{Tr}_{f,E}(K)\otimes_E\Qlb$ to $\operatorname{Tr}_{f,\Qlb}(K_{\Qlb})$. Every
   object of $\Dbc(Y,\Qlb)$ is some $K_{\Qlb}$ ([sk-thm-sfb-qlbar-two-colimit]).

In particular, for $f=a_X:X\to\Spec k$ and $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the
identification $\omega_{X,\Lambda}\simeq\Lambda_X(d)[2d]$ and the counit
$R\Gamma_c(X,\Lambda_X(d)[2d])\to\Lambda$ are, through (1)–(3), the derived limit,
the rationalization and the scalar extension of the finite ones.
