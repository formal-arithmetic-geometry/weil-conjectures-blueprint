+++
id = "sk-prop-sp-purity-bc"
kind = "proposition"
title = "Base change of purity"
order = 1832
uses = ["sk-prop-cohsm", "sk-thm-smooth-purity", "sk-prop-sp-tower-geometric", "sk-prop-sp-integral-adjunction", "sk-prop-sp-rational", "sk-thm-sp-qbar", "sk-lem-sp-reduction"]
tags = ["sketch"]
+++
Fix a Cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
{\scriptstyle f'}\big\downarrow&&\big\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$

with $f$ smooth of pure relative dimension $d$. Let $\Lambda$ be any admissible
coefficient ring and let $K\in\Dctf(Y,\Lambda)$. Identify the sources by
$u_\Lambda^{*}f_\Lambda^{*}\simeq(f')_\Lambda^{*}v_\Lambda^{*}$, as functors
$\Dctf(Y,\Lambda)\to\Dctf(X',\Lambda)$, and the targets by the exceptional base
change isomorphism $u_\Lambda^*f_\Lambda^!K\simeq(f')^!_\Lambda v_\Lambda^*K$ of
[sk-prop-cohsm] (defined by transposing the pulled-back counit
composed with the inverse of compact-support base change). Then

$$
u_\Lambda^{*}\gamma_{f,\Lambda}(K)=\gamma_{f',\Lambda}(v_\Lambda^{*}K)
\quad\text{in }\Dctf(X',\Lambda).
$$
