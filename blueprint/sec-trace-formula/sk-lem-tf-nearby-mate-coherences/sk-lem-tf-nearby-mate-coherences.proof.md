+++
kind = "proof"
of = "sk-lem-tf-nearby-mate-coherences"
+++
Each identity is proved by taking adjoints until both sides become the same composite of exchanges
and counits, and then using the composition laws for the exchanges and for the counits. Only (5)
needs more: its constant case (7) uses proper base change, so it is first proved for a proper family
and then extended by compactification.

Take $Rf_{s!}$-adjoints in (3). After the projection formula the common composite is

$$
\begin{aligned}
Rf_{s!}S_Vf_\eta^!M\dt S_WN
&\xrightarrow{\nu_f\otimes1}S_W(Rf_{\eta!}f_\eta^!M)\dt S_WN\\
&\xrightarrow{\mu_W}S_W(Rf_{\eta!}f_\eta^!M\dt N)
\xrightarrow{S_W(\varepsilon_{f_\eta}\otimes1)}S_W(M\dt N).
\end{aligned}
$$

The projection formula for $\nu_f$ used here is checked before restricting by $i_W^*$: take
$j_W^*$-adjoints of its defining exchange map. Both adjoints are $j_V^*Rj_{V*}\to1$ tensored with
the identity, followed by the generic projection formula. This proves the projection formula for
$\nu_f$. Composition in (4) follows by taking exceptional adjoints and using the composition of
counits $\varepsilon_{gf}=\varepsilon_g\,Rg_!\varepsilon_f$.

For (5), write $\xi:p_2^*a_X^!A\to p_1^!a_X^*A$, so $\kappa_M=t_{p_1}(\xi\otimes1)$. It suffices
first to show

$$
\beta_{p_1}\,S(\xi)\,\alpha_{p_2}=p_{1s}^!\sigma_X\,\xi_s\,p_{2s}^*\theta_X.
\tag{7}
$$

Suppose $a:\mathcal X\to S$ proper, and let

$$
Q_t(L):a_t^*Ra_{t*}L\xrightarrow{\sim}Rp_{1t*}p_{2t}^*L
$$

be ordinary proper base change. The $Rp_{1!}$-adjoint of $\xi$ is $Q_t(\omega_X)^{-1}$ followed by
$a_t^*\varepsilon_{a_t}$. These adjoints are compared through the identity

$$
\nu_{p_1}\,Rp_{1s*}(\alpha_{p_2})\,Q_s(S_XL)=S_X(Q_\eta(L))\,\alpha_a(Ra_{\eta*}L)\,a_s^*\nu_a(L).
$$

Its ordinary $p_1$-adjoints are equal by the composition rule for $\alpha$, since $ap_1=ap_2$,
followed by the same ordinary counit. Substitute this identity into the adjoint of the left side of
(7). Naturality of $\alpha_a$ against $\varepsilon_{a_\eta}$ and $\alpha_a(A)=\sigma_X$ give

$$
a_s^*Ra_{s!}S_X\omega_{X_\eta}\xrightarrow{a_s^*\nu_a}a_s^*Ra_{\eta!}\omega_{X_\eta}
\xrightarrow{a_s^*\varepsilon_{a_\eta}}A_{X_s}\xrightarrow{\sigma_X}S_XA_{X_\eta}.
$$

By (1), the same map is $\sigma_X\,a_s^*(\varepsilon_{a_s}Ra_{s!}\theta_X)$. This is the adjoint of
the right side. For a nonproper family compactify $\mathcal X$ properly and restrict both product
factors. The maps $\xi$ restrict by composition of exceptional inverse images; for the open
immersion $j$, $j^!=j^*$, $\alpha_j$ is invertible by smooth exchange and $\beta_j=\alpha_j^{-1}$.
Extend a generic coefficient $M$ by $j_{\eta!}M$ before restricting. Thus the calculation applies on
the original open family. Finally apply (3) to $p_1$ and use $\mu(\sigma\otimes1)=1$ to deduce
(5).

For (6), the inverse base-change map $Rr_*d^!\to c^!R\Delta_*$ is adjoint to the explicit map

$$
Rc_!Rr_*d^!=R\Delta_*Rd_!d^!\xrightarrow{R\Delta_*\varepsilon_d}R\Delta_*.
$$

This identification uses properness of $r$ and $\Delta$. Substitute it in both sides and take
$Rc_{s!}$-adjoints. Replace the proper comparisons $\chi_r,\chi_\Delta$ by the inverses of
$\nu_r,\nu_\Delta$. Both resulting maps are the exchange for the equal composite $cr=\Delta d$,
followed by $S_X\varepsilon_d$. Composition of the exchanges and the composition of counits prove
equality.
