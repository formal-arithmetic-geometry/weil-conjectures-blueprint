+++
kind = "proof"
of = "sk-prop-sp-rational"
uses = ["sk-prop-sp-integral-adjunction", "sk-prop-int-compactness", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity"]
+++
Choose integral models $M_0$ and $K_0$. By (10.20) twice and
Proposition [sk-prop-sp-integral-adjunction] with $\gamma_{f,\mathcal O_E}$,

$$
\begin{aligned}
\Hom(Rf_{!,E}M,K)&\simeq\Hom(Rf_{!,\mathcal O_E}M_0,K_0)\otimes E\\
&\simeq\Hom(M_0,f^*_{\mathcal O_E}K_0(d)[2d])\otimes E
\simeq\Hom(M,f_E^*K(d)[2d]).
\end{aligned}
$$

These bijections are given by the integral unit and counit with $\ell$ inverted, so they are
natural and do not depend on the models.
