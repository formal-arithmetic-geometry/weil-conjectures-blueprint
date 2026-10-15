+++
kind = "proof"
of = "det-sp-tower-exceptional-bc"
+++
(1) Choose a compactification of $f$ and pull it back. Extension by zero
commutes with pullback, and the proper base change map for towers is defined
as the transpose of the counit of the levelwise adjunction; by
[det-sp-tower-shriek-levels] it evaluates at each level to the finite proper base
change map, an isomorphism, so it is an isomorphism of towers.

(2) The transpose exists by the tower adjunction $R(f')_{!,\bullet}\dashv(f')^!_\bullet$
of [det-sp-tower-gluing]. Evaluation at $n$ carries $\beta_{f,\bullet}$ and
$\varepsilon_{f,\bullet}$ to $\beta_{f,\mathcal O_E/\ell^n}$ and the finite counit, and the
tower adjunction to the finite one (same lemma), so it carries $e_{f,\bullet}$ to
the transpose of $v^*(\varepsilon_f)\circ\beta_f^{-1}$, i.e. the finite exceptional
base change, which is an isomorphism; hence $e_{f,\bullet}$ is an isomorphism. The
reduction maps of $u_\bullet^*f^!_\bullet K_\bullet$ and $(f')^!_\bullet v^*_\bullet K_\bullet$ are
built from the coefficient comparisons $c^f_{n,m}$, $c^{f'}_{n,m}$ and those of
$K_\bullet$; the second identity of [det-sp-mixed-base-change] for
$\mathcal O_E/\ell^n\to\mathcal O_E/\ell^m$ says that $e_{f,n}$ and $e_{f,m}$ intertwine
them. So $e_{f,\bullet}$ commutes with reduction maps, and since $u^*_\bullet f^!_\bullet$
preserves normalized towers, so does $(f')^!_\bullet v^*_\bullet$ on their images.

(3) The reduction formulas for inverse image and for $f^!_{\Zl}$
([det-sp-integral-adjunction-bijection]) write both sides as $R\varprojlim_n$ of
the finite-level terms for $K_n=K\otimes^{\mathbf L}_{\mathbf Z_{\ell,Y}}(\mathbf Z/\ell^n)_Y$;
i.e. $\operatorname{red}_{X'}(u^*f^!_{\Zl}K)\simeq u^*_\bullet f^!_\bullet\operatorname{red}_YK$ and
$\operatorname{red}_{X'}((f')^!_{\Zl}v^*K)\simeq(f')^!_\bullet v^*_\bullet\operatorname{red}_YK$. Under the
equivalence of normalized towers with $\Dbc(-,\Zl)$, $e_{f,\bullet}$ gives an
isomorphism, which is $R\varprojlim e_{f,\bullet}$. It is the integral exceptional
base change because its transpose is the derived limit of the transposes, i.e.
$v^*(\varepsilon_{f,\Zl})\circ\beta_{f,\Zl}^{-1}$.
