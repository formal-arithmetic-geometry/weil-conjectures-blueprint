+++
id = "det-sp-rational-adjunction"
kind = "proposition"
title = "The rational purity adjunction and the purity map over $E$"
uses = ["det-sp-rational-localized-hom", "det-sp-integral-adjunction-bijection", "det-sp-unique-right-adjoint"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and $E/\Ql$ finite.

1. For $M\in\Dbc(X,E)$, $K\in\Dbc(Y,E)$ with integral models $M_0,K_0$, the
   composite bijection
   $$
   \operatorname{Hom}(Rf_{!,E}M,K)\simeq\operatorname{Hom}(Rf_{!,\mathcal O_E}M_0,K_0)\otimes E
   \simeq\operatorname{Hom}(M_0,f^!_{\mathcal O_E}K_0)\otimes E\simeq\operatorname{Hom}(M,f^*_EK(d)[2d])
   $$
   is independent of the models and natural in $M$ and $K$, so it defines an
   adjunction $Rf_{!,E}\dashv f^*_E(-)(d)[2d]$ whose unit and counit are the
   scalar extensions of the integral ones transported along
   $\gamma_{f,\mathcal O_E}$.
2. Comparing with the Brown adjoint $f^!_E$ by [det-sp-unique-right-adjoint]
   gives the counit-preserving purity isomorphism
   $\gamma_{f,E}:f^*_E(-)(d)[2d]\xrightarrow{\sim}f^!_E$ of functors
   $\Dbc(Y,E)\to\Dbc(X,E)$.
