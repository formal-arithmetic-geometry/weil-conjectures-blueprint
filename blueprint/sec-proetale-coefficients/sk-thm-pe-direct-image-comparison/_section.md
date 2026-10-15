+++
id = "sk-thm-pe-direct-image-comparison"
kind = "theorem"
title = "Direct-image comparison"
order = 730
uses = ["sk-prop-pe-comparison-morphism", "sk-cor-pe-classical-derived", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
Let $g\colon X\to Y$ be a morphism of schemes. Base change of site objects gives
the commutative square of topoi

$$
\begin{array}{ccc}
X_{\Proet}&\xrightarrow{\ \nu_X\ }&X_{\Et}\\
{\scriptstyle g_{\Proet}}\downarrow&&\downarrow{\scriptstyle g_{\Et}}\\
Y_{\Proet}&\xrightarrow{\ \nu_Y\ }&Y_{\Et}
\end{array}
$$

and an isomorphism $g_{\Proet}^*\nu_Y^*\simeq\nu_X^*g_{\Et}^*$ of functors
$\Mod(Y_{\Et},\Lambda)\to\Mod(X_{\Proet},\Lambda)$, compatible with composition;
since all four functors are exact, it is also an isomorphism of functors
$D(Y_{\Et},\Lambda)\to D(X_{\Proet},\Lambda)$.

If $g$ is quasi-compact and quasi-separated, the canonical natural
transformation of functors $D^+(X_{\Et},\Lambda)\to D^+(Y_{\Proet},\Lambda)$

$$
\nu_Y^*Rg_{\Et,*}K\longrightarrow Rg_{\Proet,*}\nu_X^*K
$$

is an isomorphism for $K\in D^+(X_{\Et},\Lambda)$. In particular, direct image of
a bounded-below classical pro-étale complex is classical. The isomorphism is
compatible with units, counits and composition.
