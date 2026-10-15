+++
id = "det-sf-mate-open-restriction"
kind = "lemma"
title = "Open immersions and open restriction for $f^!$"
uses = ["lem-sf-mate", "det-sf-existence-brown", "sk-prop-proper-image-localizing"]
+++
Let $\Lambda$ be admissible.

1. For an open immersion $j:U\to X$ (quasi-compact, $X$ qcqs), the functor
$j_!:\Loc(\Dctf(U,\Lambda))\to\Loc(\Dctf(X,\Lambda))$ is left adjoint to
$j^*:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(U,\Lambda))$, and $j^!\simeq j^*$
canonically, compatibly with the adjunctions.
2. For $f:X\to Y$ separated of finite type, an open immersion $v:V\to Y$,
$X_V=f^{-1}(V)$, $u:X_V\to X$ and $f_V:X_V\to V$, there is a canonical
isomorphism $u^*f^!\simeq f_V^!v^*$, and for an open $j:U\to X$ a canonical
isomorphism $j^*f^!\simeq(fj)^!$.
3. Consequently, a morphism in $\Loc(\Dctf(X,\Lambda))$ is an isomorphism as
soon as its restrictions to the members of an open covering $X=\bigcup_aU_a$
are, and $f^!$ is computed locally on $X$ and on $Y$: $j_a^*f^!\simeq(fj_a)^!$
and, over an open covering $Y=\bigcup_bV_b$, $u_b^*f^!\simeq f_{V_b}^!v_b^*$.
