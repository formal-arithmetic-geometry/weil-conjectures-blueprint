+++
id = "prose-09-32"
kind = "hidden"
title = "The trace map (1)"
order = 803
+++
On a compact oriented manifold of dimension $n$, Poincaré duality
pairs $H^i$ with $H^{n-i}$ by cup product followed by integration
$H^n(M)\to\mathbf R$, which sends the class of a point to $1$. To obtain
the Poincaré pairing of Weil's axiom (c) we need the analogue of
integration. By adjunction we already have a map, the counit
$Rf_!f^!K\to K$, but its source involves $f^!$, which we only know
through its universal property. Composing with $\gamma_f$ replaces
$f^!K$ by the twisted and shifted inverse image, so the result is a map out of
compactly supported cohomology of an explicit complex. For example, for $X$ smooth of
dimension $d$ over an algebraically closed field $k$ and $K=\Lambda$, it is
a map $H_c^{2d}(X_{\mathrm{pro}\acute{e}t},\Lambda_X(d))\to\Lambda$. Here the twist cannot be
dropped, for the reason explained before
Definition [definition-tate-twists]: geometric Frobenius acts on
$H^2(\mathbf P^1_k,\mathbf Z_\ell)$ by $q$, so only the twisted trace map commutes
with Frobenius (Section [sec-Weil-complexes]). The trace map is used in the Poincaré pairing
(Theorem [theorem-poincare-duality]) and the trace isomorphism in top
degree (Theorem [theorem-trace-isomorphism-top-degree]).

Let $f:X\to Y$ be smooth of pure relative dimension $d$, and let
$\Lambda$ be any admissible coefficient ring. We omit $\Lambda$ from
the notation and let $\varepsilon_f(K):Rf_!f^!K\to K$ be the counit
of the adjunction $Rf_!\dashv f^!$ between $D^b_{\mathrm{ctf}}(X,\Lambda)$
and $D^b_{\mathrm{ctf}}(Y,\Lambda)$.
