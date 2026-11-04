+++
id = "theorem-smooth-purity-all-admissible-coefficients"
kind = "theorem"
title = "Smooth purity for all admissible coefficients"
order = 724
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothOrientation"]
uses = ["proposition-composition-open-restriction-compactifications-f", "proposition-six-operations-change-coefficients"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For every
admissible coefficient ring $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$,
with $A$ finite, there are isomorphisms, natural in $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$,

$$
\gamma_f(K):
f^{*}K(d)[2d]\xrightarrow{\sim}f^{!}K,
\tag{9.2}
$$

with the following properties.

1. If $f$ is the projection $p:\mathbf A^1_Y\to Y$, then
   $\varepsilon_p(\Lambda_Y)\circ Rp_!\bigl(\gamma_p(\Lambda_Y)\bigr)$ is the
   trace map (9.1).
2. For $g:Y'\to Y$ as in
   Definition [definition-exceptional-base-change-map], with exceptional
   base change map $\beta:g'^*f^!K\to f'^!g^*K$, we have
   $\beta\circ g'^*\gamma_f(K)=\gamma_{f'}(g^*K)$, the sources being
   identified by $g'^*f^*\simeq f'^*g^*$.
3. For a smooth morphism $h:Y\to Z$ of pure relative dimension $e$ and
   $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$, the map $\gamma_{h\circ f}(K)$ is the composite of
   $f^*(\gamma_h(K))(d)[2d]$ and $\gamma_f(h^!K)$, the sources being identified
   by $(h\circ f)^*\simeq f^*h^*$ and the targets by the composition
   isomorphism $f^!h^!\simeq(h\circ f)^!$ of
   Proposition [proposition-composition-open-restriction-compactifications-f](1).
4. For a coefficient map $\Lambda\to\Lambda'$ of
   Proposition [proposition-six-operations-change-coefficients], the
   change-of-coefficients isomorphism $(f^!K)_{\Lambda'}\to f^!(K_{\Lambda'})$
   of that proposition carries $(\gamma_{f,\Lambda}(K))_{\Lambda'}$ to
   $\gamma_{f,\Lambda'}(K_{\Lambda'})$, the sources being identified by the
   change-of-coefficients isomorphism for $f^*$.
