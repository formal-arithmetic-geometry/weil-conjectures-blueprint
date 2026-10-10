+++
kind  = "proof"
of    = "prop-base-linear"
+++
Write $\pi:V\times_SV^\vee\to S$ for the structure morphism of the Fourier
square, so that $p\circ p_1=\pi=p'\circ p_2$. Pullback is monoidal and
compatible with composition, hence

$$
p_1^*\bigl(K\otimes^L_Ep^*N\bigr)\cong p_1^*K\otimes^L_Ep_1^*p^*N
\cong p_1^*K\otimes^L_E\pi^*N\cong p_1^*K\otimes^L_Ep_2^*{p'}^*N .
$$

Tensoring with the kernel $\mathcal K_\psi$ of [def-fd-kernel] and using
the associativity and commutativity constraints of $\otimes^L_E$ gives

$$
p_1^*\bigl(K\otimes^L_Ep^*N\bigr)\otimes^L_E\mathcal K_\psi\cong
\bigl(p_1^*K\otimes^L_E\mathcal K_\psi\bigr)\otimes^L_Ep_2^*\bigl({p'}^*N\bigr).
$$

The first factor $A:=p_1^*K\otimes^L_E\mathcal K_\psi$ lies in
$D^b_c(V\times_SV^\vee,E)$ ($\mathcal K_\psi$ being lisse of rank one),
and $L:={p'}^*N\in D^b_c(V^\vee,E)$ has finite Tor amplitude because
$E$ is a field. The morphism $p_2$ is separated of finite type, so the
compact-support projection formula, clause (5) of
[prop-functor-package], gives

$$
p_{2,!}\bigl(A\otimes^L_Ep_2^*L\bigr)\cong p_{2,!}(A)\otimes^L_EL .
$$

Finally the shift commutes with tensoring by $L$,
$(X\otimes^L_EL)[r]\cong X[r]\otimes^L_EL$, and by the definition
[def-fd-transform] the two sides are
$\operatorname{FT}_\psi(K\otimes^L_Ep^*N)$ and
$\operatorname{FT}_\psi(K)\otimes^L_E{p'}^*N$. Each isomorphism used is a
natural transformation, whence naturality in $K$ and $N$.

(1) is the case $K=\underline E=E_V$, since $E_V\otimes^L_Ep^*N\cong p^*N$.

(2) Let $E_S(m)$, $E_V(m)$, $E_{V^\vee}(m)$ be the twisting objects of
[def-wf-tate-twist] on $S$, $V$, $V^\vee$. For any morphism $f:X\to Y$
the canonical isomorphisms $f^*\mu_{\ell^n,Y}\cong\mu_{\ell^n,X}$
(both being the sheaf represented by the group scheme $\mu_{\ell^n}$)
are compatible with the $\ell$-th power transition maps; since
$\mathbf Z_\ell(1)_Y$ is pro-etale locally isomorphic to the constant
sheaf $\mathbf Z_\ell$, whose pullback is again $\mathbf Z_\ell$, the
pullback commutes with this limit, and they give
$f^*E_Y(1)\cong E_X(1)$; since $f^*$ is monoidal, this gives
$f^*E_Y(m)\cong E_X(m)$ for $m\ge0$, and, $E_Y(m)$ being invertible
(lisse of rank one) with inverse $E_Y(-m)=R\mathcal Hom_E(E_Y(m),E_Y)$,
pullback commutes with this dual, which gives the case $m<0$. Hence
$K(m)=K\otimes^L_EE_V(m)\cong K\otimes^L_Ep^*E_S(m)$ and
$\operatorname{FT}_\psi(K)(m)\cong\operatorname{FT}_\psi(K)\otimes^L_E{p'}^*E_S(m)$,
and the main isomorphism with $N=E_S(m)$ gives (2). The Frobenius
pullbacks commute with all the canonical isomorphisms used (monoidality
of pullback, the projection-formula map, the pullback of roots of
unity), so a Weil structure on $K$ is carried to the Weil structure on
both sides.
