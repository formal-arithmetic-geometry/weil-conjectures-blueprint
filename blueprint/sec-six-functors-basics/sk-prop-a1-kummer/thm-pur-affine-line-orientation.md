+++
id = "thm-pur-affine-line-orientation"
kind = "theorem"
title = "Global orientation and its normalization"
order = 2832
uses = ["def-pur-affine-line-datum", "def-pur-conventions", "def-weil-exceptional-inverse-image", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "lem-exc-open-complement-known", "lem-pur-gysin-structure", "lem-pur-support-localization-triangle", "prop-exc-closed-tor", "prop-pur-gm-relative-kummer", "thm-pur-rank-one-local-calculation", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting), let $Y$ be the separated finite-type $k$-scheme of the
affine-line datum, and let
$\kappa(t)\in H^1(\mathbf G_{m,Y},A(1))$ be the
Kummer class of the global coordinate
$t$. The boundary of $\kappa(t)$, determined through the
identification of [lem-pur-gysin-structure] (which gives the
support object $Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]\in D^b_{ctf}(Y,\Lambda)$
concentrated in degree zero), is the *global orientation* – a
morphism

$$
\operatorname{pur}_s:\Lambda_Y\longrightarrow Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]
$$

in $D^b_{ctf}(Y,\Lambda)$ with $\Lambda=A$, where $Rs^!$ is the
exceptional inverse image
of the zero section $s:Y\hookrightarrow\mathbf A^1_Y$, a closed
immersion whose ambient right adjoint exists unconditionally
([lem-exc-closed-ambient]) and preserves constructibility and
finite Tor amplitude, the open complement
$\mathbf G_{m,Y}\hookrightarrow\mathbf A^1_Y$ satisfying the
open-complement condition of
[lem-exc-closed-amplitude], [prop-exc-closed-tor] by
[lem-exc-open-complement-known],
with the shift $[2]$ and the twist
$(1)$. Its restriction to every geometric point $\bar y\to Y$ is
the normalized class $1\in H^2_{s(\bar y)}(\mathbf A^1_{\bar y},\Lambda(1))$ of
[thm-pur-rank-one-local-calculation].
