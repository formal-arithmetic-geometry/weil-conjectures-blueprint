+++
id = "prose-02-36"
kind = "hidden"
title = "Direct images (1)"
order = 132
+++
Proper base change is proved on the étale site
(Section [chap-Proper-base-change]), while $Rf_!$ is defined by direct
images on the pro-étale site. To transfer proper base change, and to
compute these direct images, we compare direct images on the two sites.

Let $g:X\to Y$ be a morphism of schemes. Base change of objects of the
sites defines a commutative square of topoi

$$
\begin{CD}
X_{\mathrm{pro}\acute{e}t}@>{\nu_X}>>X_{\acute{e}t}\\
@V{g_{\mathrm{pro}\acute{e}t}}VV @VV{g_{\acute{e}t}}V\\
Y_{\mathrm{pro}\acute{e}t}@>{\nu_Y}>>Y_{\acute{e}t}.
\end{CD}
$$

It induces an isomorphism
$g_{\mathrm{pro}\acute{e}t}^*\nu_Y^*\simeq\nu_X^*g_{\acute{e}t}^*$ of functors
$\operatorname{Mod}(Y_{\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$, compatible with
composition. Since all four functors are exact, it is also an
isomorphism of functors $D(Y_{\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
For direct images the comparison needs a hypothesis on $g$. The
comparison map
$\nu_Y^*Rg_{\acute{e}t,*}\to Rg_{\mathrm{pro}\acute{e}t,*}\nu_X^*$ of functors
$D^+(X_{\acute{e}t},\Lambda)\to D^+(Y_{\mathrm{pro}\acute{e}t},\Lambda)$ is defined as the
adjoint of the composite of
$g_{\mathrm{pro}\acute{e}t}^*\nu_Y^*Rg_{\acute{e}t,*}\simeq\nu_X^*g_{\acute{e}t}^*Rg_{\acute{e}t,*}$ with
$\nu_X^*$ applied to the counit of the adjunction $g_{\acute{e}t}^*\dashv Rg_{\acute{e}t,*}$.

Evaluated on a pro-étale affine $V=\varprojlim_iV_i$ over $Y$, the
comparison map is the map from $\varinjlim_iH^q(X\times_YV_i,F)$ to
$H^q(X\times_YV,F)$. So the theorem below is the continuity of étale
cohomology under affine limits, and like it, it needs $g$ to be
quasi-compact. Without this the map fails to be surjective already for $q=0$.
For example, let $Y$ be affine and connected, $X=\coprod_{n\in\mathbf N}Y$ and $F$ the
constant sheaf $\mathbf Z/2$. Then $g_*F$ is the product of countably many
copies of $\mathbf Z/2$ on $Y$. On $V=Y\times S$ with $S$ an infinite
profinite set, the pro-étale side has as sections all sequences of
locally constant functions $S\to\mathbf Z/2$, while the classical side
only has the sequences that factor through a common finite quotient of
$S$.
