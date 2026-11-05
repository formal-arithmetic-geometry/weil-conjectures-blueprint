+++
kind = "proof"
of = "proposition-sp-rational"
order = 788
uses = ["proposition-sp-integral-adjunction"]
+++
An adjunction is a natural bijection of Hom groups, and by
(9.21) every Hom group over $E$ is an integral Hom group
tensored with $E$. So we compute both sides on integral models.
Choose integral models $M_0$ and $K_0$, so that $M=M_0[1/\ell]$ and
$K=K_0[1/\ell]$. By (9.21) twice and
Proposition [proposition-sp-integral-adjunction] with $\gamma_{f,\mathcal O_E}$,

$$
\begin{aligned}
\Hom(Rf_{!,E}M,K)&\simeq\Hom(Rf_{!,\mathcal O_E}M_0,K_0)\otimes E\\
&\simeq\Hom(M_0,f^*_{\mathcal O_E}K_0(d)[2d])\otimes E
\simeq\Hom(M,f_E^*K(d)[2d]).
\end{aligned}
$$

These bijections are given by the integral unit and counit with $\ell$ inverted, so they are
natural and do not depend on the models.
