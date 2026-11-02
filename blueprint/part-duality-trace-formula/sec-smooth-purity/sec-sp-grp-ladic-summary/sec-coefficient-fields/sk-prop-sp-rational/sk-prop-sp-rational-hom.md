+++
id = "det-sp-rational-localized-hom"
kind = "lemma"
title = "Rational Hom groups from integral models"
order = 3321
uses = ["sk-thm-sfb-rationalization-comparison", "det-def-sfb-dc-lower-shriek", "sk-cor-pe-bounded-continuity", "sk-thm-sfb-proper-base-change"]
+++
Let $E/\Ql$ be finite and $T$ a scheme whose underlying topological space is Noetherian, the scope of
the rationalization theorem [sk-thm-sfb-rationalization-comparison]. Every object of $\Dbc(T,E)$ is
isomorphic to $K_0[1/\ell]$ for some $K_0\in\Dbc(T,\mathcal O_E)$, and for
$K_0,L_0\in\Dbc(T,\mathcal O_E)$ and $q\in\mathbf Z$ the natural map

$$
\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E\xrightarrow{\ \sim\ }
\Hom_{\Dbc(T,E)}\bigl(K_0[1/\ell],L_0[1/\ell][q]\bigr)
$$

is an isomorphism. Moreover, for $f:X\to Y$ separated of finite type,
$f^*(K_0[1/\ell])=(f^*K_0)[1/\ell]$; and for a quasi-compact
quasi-separated compactification $f=\bar f\circ j$ ($j$ an open immersion,
$\bar f$ proper) and $M_0\in\Dbc(X,\mathcal O_E)$,
$R\bar f_*j_!(M_0[1/\ell])\simeq(R\bar f_*j_!M_0)[1/\ell]$ in
$D(Y_{\mathrm{pro}\acute{e}t},E)$. If moreover $X$ and $Y$ are separated of
finite type over a field $k$ that is finite or algebraically closed, with
$\ell\ne\operatorname{char}k$, then
$Rf_{!}(M_0[1/\ell])\simeq(Rf_{!,\mathcal O_E}M_0)[1/\ell]$ in $\Dbc(Y,E)$.
