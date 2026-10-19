+++
id = "sk-lem-as-properties"
kind = "lemma"
title = "The Artin–Schreier sheaf is a lisse character sheaf"
order = 3023
uses = ["sk-def-as", "sk-def-fourier-set"]
tags = ["sketch"]
+++
$\pi$ is finite étale of degree $p$, and the translations $\sigma_a$
($a\in\Fp$) act simply transitively on its geometric fibres: they make $Y$
an $\Fp$-torsor over $X_0$. The automorphisms of $Y$ *as an
$\Fp$-torsor* (those commuting with the $\sigma_a$) form $\Gamma(X_0,\Fp)$,
which is $\Fp$ when $X_0$ is connected; and $\Fp\to\operatorname{Aut}(Y/X_0)$
is an isomorphism when $Y$ is connected, but not in general (for $f=0$ the
cover $Y=\coprod_{a\in\Fp}X_0$ is split, and e.g. for $p=3$,
$X_0=\Spec\mathbf F_3$ its full automorphism group over $X_0$ is $S_3$).
Over $\Aone_{k_0}$ the covering is $y\mapsto x=y^p-y$. Its pushforward
decomposes as
$\pi_*\Qlb\cong\bigoplus_{\chi\in\widehat{\Fp}}\mathcal L_\chi$ with each
$\mathcal L_\chi$ lisse of rank one and $\mathcal L_0=1$ (for $\chi\ne0$,
$\mathcal L_\chi$ may or may not be constant, e.g. all are constant when $f=0$);
consequently $\mathcal L_{\psi,f}$ is lisse of rank one,

$$
\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,g}\cong\mathcal L_{\psi,f+g},
\qquad
(\mathcal L_{\psi,f})^{-1}\cong\mathcal L_{\psi,-f}.
$$

At a closed point $u$ the geometric Frobenius acts on $\mathcal L_{\psi,f}$ by
$\Psi(\Tr_{\kappa(u)/\Fp}f(u))=\psi(\Tr_{\kappa(u)/k_0}f(u))$; so its trace
function on $\Aone_{k_0}$ is
$t_{\mathcal L_{\psi,ax}}(u)=\psi(\Tr_{\kappa(u)/k_0}(au))$; and
$H^q(\Aone_{\bar k},\mathcal L_{\psi_a})=0$ for $(q,a)\neq(0,0)$, while
$H^0(\Aone_{\bar k},\Qlb)=\Qlb$ and $H^q(\Aone_{\bar k},\Qlb)=0$ for $q>0$.
