+++
kind  = "proof"
of    = "cor-mg-rankone-weight-from-element"
+++
Fix a degree-one lift $s\in W(X_0)$ as in
[def-wf-weil-group], and put $c=\chi(s)$. By
hypothesis the restriction of
$\chi$ to $\pi_1(X)$ has finite image, and by the modulus identity
of [lem-wf-rank-one-component-modulus] applied to the image of
the degree-$m$ coset of $W(X_0)$ in
$G^{[m]}\subseteq G_{\mathrm{arith}}(\rho)$ (an element
$w=\gamma s^m$ with $\gamma\in\pi_1(X)$ has matrix
$\rho(\gamma)\rho(s)^m$), one has

$$
|\iota(\chi(w))|=|\iota(c)|^{m}\qquad\text{for all }w\in W(X_0)
\text{ with }\deg(w)=m.
$$

If $\mathcal L_0$ is punctually $\iota$-pure of weight $w$, then at
a closed point $x$ the eigenvalue $\chi(F_x)$ of the local
geometric Frobenius $F_x$ (of degree $d(x)$) has modulus
$q_x^{w/2}=q^{d(x)w/2}$ by [def-weil-punctual-weights], so the
identity above gives $|\iota(c)|^{d(x)}=q^{d(x)w/2}$, whence
$|\iota(c)|=q^{w/2}$ and
$|\iota(\chi(\sigma))|=|\iota(c)|^{d}=q^{wd/2}$ for every
positive-degree $\sigma$. Conversely, if the displayed equality
holds for one such $\sigma$, then $|\iota(c)|=q^{w/2}$ by the same
identity, and every closed point $x$ satisfies
$|\iota(\chi(F_x))|=|\iota(c)|^{d(x)}=q_x^{w/2}$, which is the
punctual purity of [def-weil-punctual-weights].
