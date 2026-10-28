+++
kind = "proof"
of = "sk-prop-sp-rational"
uses = ["sk-prop-sp-integral-adjunction", "sk-prop-int-compactness", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity"]
+++
Every object of $\Dbc(T,E)$ is $K_0[1/\ell]$ for some $K_0\in\Dbc(T,\mathcal O_E)$
([sk-lem-integral-models]), and Hom groups are the integral ones with $\ell$
inverted: $\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E\xrightarrow{\sim}
\Hom_{\Dbc(T,E)}(K_0[1/\ell],L_0[1/\ell][q])$, because $L_0[1/\ell]$ is the colimit
of $L_0\xrightarrow{\ell}L_0\xrightarrow{\ell}\cdots$ and Hom out of $K_0$ commutes
with this colimit ([det-lem-int-ext]). On integral models $f^*$ and $Rf_!$ are
the integral functors with $\ell$ inverted: $f^*(K_0[1/\ell])=(f^*K_0)[1/\ell]$, and
$Rf_!(M_0[1/\ell])\simeq(Rf_{!,\mathcal O_E}M_0)[1/\ell]$ because
$Rf_{!,\mathcal O_E}M_0=R\bar f_*j_!M_0$ and $R\bar f_*$ commutes with the colimit
along $\ell$ ([sk-cor-pe-bounded-continuity]).

Choose integral models $M_0,K_0$. By these comparisons and the integral purity
isomorphism $\gamma_{f,\mathcal O_E}$, the two functors are the scalar extensions
of $Rf_{!,\mathcal O_E}$ and $f^!_{\mathcal O_E}$, so the localized Hom formula twice
and the $\mathcal O_E$-linear adjunction of [sk-prop-sp-integral-adjunction] give

$$
\begin{aligned}
\operatorname{Hom}(Rf_{!,E}M,K)
&\simeq\operatorname{Hom}(Rf_{!,\mathcal O_E}M_0,K_0)\otimes E\\
&\simeq\operatorname{Hom}(M_0,f_{\mathcal O_E}^!K_0)\otimes E
\simeq\operatorname{Hom}(M,f_E^*K(d)[2d]),
\end{aligned}
$$

with Hom groups taken in $\Dbc(Y,E)$, $\Dbc(Y,\mathcal O_E)$, $\Dbc(X,\mathcal O_E)$
and $\Dbc(X,E)$ respectively. The unit and counit are the scalar extensions of
the integral ones, transported along $\gamma_{f,\mathcal O_E}$, and the triangle
identities are images of the integral ones.
