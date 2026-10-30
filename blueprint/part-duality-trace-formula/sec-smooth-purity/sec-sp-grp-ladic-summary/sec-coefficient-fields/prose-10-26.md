+++
id = "prose-10-26"
kind = "hidden"
title = "Coefficient fields (2)"
order = 476
+++
Every object of $\Dbc(T,E)$ is $K_0[1/\ell]$ for some $K_0\in\Dbc(T,\mathcal O_E)$, called an
integral model, and for integral models

$$
\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E
\xrightarrow{\sim}\Hom_{\Dbc(T,E)}\bigl(K_0[1/\ell],L_0[1/\ell][q]\bigr).
\tag{10.20}
$$

To see this, note that the target is $\Hom(K_0,L_0[1/\ell][q])$ by adjunction, and
$L_0[1/\ell]$ is the colimit of $L_0\xrightarrow{\ell}L_0\xrightarrow{\ell}\cdots$. By
dévissage we may take $K_0=a_!C$ with $C$ dualizable on a stratum
(Lemma [sk-lem-int-integral-heart](3)). The stratum formula of
Lemma [sk-lem-formal-closed-support](2), whose proof uses only that $C$ is dualizable,
turns Hom out of $a_!C$ into cohomology on a quasi-compact quasi-separated scheme, and
this commutes with the colimit by Corollary [sk-cor-pe-bounded-continuity]. Models exist by
Lemma [sk-lem-integral-models](4) together with (10.20), and on
models $f^*$ and $Rf_!$ are the integral functors with $\ell$ inverted, again because
$R\bar f_*$ commutes with the colimit along $\ell$.
