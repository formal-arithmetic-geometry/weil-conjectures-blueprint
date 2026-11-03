+++
kind = "proof"
of = "det-sfb-dc-restricted-functors-completed-pullback"
+++
*The map.* For every $n$ there is a natural map $g^*K\to g^*K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n=g^*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$
(inverse image is exact and $\mathcal O_E$-linear), compatible in $n$; it induces
$c_K\colon g^*K\to R\varprojlim_ng^*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$. The target is the derived completion of
$g^*K$, so $c_K$ is an isomorphism iff $g^*K$ is derived complete.

*Local models.* If $K=a_!M$ with $M$ locally the completion $\widehat P$ of a bounded complex $P$ of finite free
$\mathcal O_E$-modules, then base change for extension by zero and closed direct image gives
$g^*a_!M=a'_!g_S^*M$ (with $a'$, $g_S$ the base changes), and $g_S^*\widehat P$ is locally the same complex of
finite free $\mathcal O_{E}$-modules over the coefficient sheaf of the new scheme, which is derived complete with
constructible reduction $P/\pi_E$. Hence $g^*a_!M\in\Dbc(X,\mathcal O_E)$ by
[det-sfb-dc-restricted-functors-closed-image], and $c_{a_!M}$ is an isomorphism.

*Dévissage.* By [det-sfb-dc-restricted-functors-closed-image] every $K\in\Dbc(Y,\mathcal O_E)$ is a finite iterated
extension of such $a_!M$. Both $g^*$ and the completed inverse image are exact, and $c$ is a natural
transformation of exact functors; by the five lemma along the finitely many triangles, $g^*K$ is derived
complete with constructible reduction (so lies in $\Dbc(X,\mathcal O_E)$; compare
[lem-sfb-dc-upper-star-preserves]) and $c_K$ is an isomorphism.
