+++
id = "sk-prop-sp-exceptional-bc"
kind = "proposition"
title = "Exceptional base change for a smooth map"
order = 1818
uses = ["sk-prop-cohsm", "sk-prop-sp-tensor"]
tags = ["sketch"]
+++
Consider a Cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$

with $f$ smooth of pure relative dimension $d$. For
$K\in\Dctf(Y_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, pulling back the counit
$Rf_!f^!K\to K$ along $v$ and using compact-support base change gives a
morphism $R(f')_!u^*f^!K\to v^*K$ in $\Dctf(Y'_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$. Its
adjoint under $R(f')_!\dashv(f')^!$ is the *exceptional base-change map*
$u^*f^!K\to(f')^!v^*K$, a morphism in $\Dctf(X'_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$.

**Proposition.** For the square above and
$K\in\Dctf(Y_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, the exceptional base-change map is an
isomorphism, compatible with the tensor maps for $f$ and $f'$
([sk-prop-sp-tensor]):

$$
u^*f^!K\xrightarrow{\ \sim\ }(f')^!v^*K.
$$
