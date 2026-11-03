+++
kind = "proof"
of = "det-nearby-structural-product"
uses = ["det-nearby-exchange-maps", "det-nearby-exceptional-tensor", "det-sp-nearby-cycles-exchanges", "thm-weil-pbc-bounded-below"]
+++
*Constant case for a proper family.* Suppose $a\colon\mathcal X\to S$ proper, and for $t\in\{s,\eta\}$
let

$$
Q_t(L):a_t^*Ra_{t*}L\xrightarrow{\sim}Rp_{1t*}p_{2t}^*L
$$

be ordinary proper base change [thm-weil-pbc-bounded-below]. The $Rp_{1!}$-adjoint of $\xi$ is
$Q_t(\omega_X)^{-1}$ followed by $a_t^*\varepsilon_{a_t}$. These adjoints are compared through the
identity

$$
\nu_{p_1}\,Rp_{1s*}(\alpha_{p_2})\,Q_s(S_XL)=S_X(Q_\eta(L))\,\alpha_a(Ra_{\eta*}L)\,a_s^*\nu_a(L).
$$

Its ordinary $p_1$-adjoints are equal by the composition rule for $\alpha$, since $ap_1=ap_2$,
followed by the same ordinary counit. Substitute this identity into the adjoint of the left side of
the first equation. Naturality of $\alpha_a$ against $\varepsilon_{a_\eta}$ and $\alpha_a(A)=\sigma_X$
give

$$
a_s^*Ra_{s!}S_X\omega_{X_\eta}\xrightarrow{a_s^*\nu_a}a_s^*Ra_{\eta!}\omega_{X_\eta}
\xrightarrow{a_s^*\varepsilon_{a_\eta}}A_{X_s}\xrightarrow{\sigma_X}S_XA_{X_\eta}.
$$

By the definition of $\theta_X=\beta_{a_X}(A)$ as an exceptional adjoint, the same map is
$\sigma_X\,a_s^*(\varepsilon_{a_s}Ra_{s!}\theta_X)$, which is the adjoint of the right side.

*General family.* For a nonproper family compactify $\mathcal X$ properly and restrict both product
factors. The maps $\xi$ restrict by composition of exceptional inverse images. For the open
immersion $j$, $j^!=j^*$, $\alpha_j$ is invertible by the smooth exchange of
[det-sp-nearby-cycles-exchanges], and $\beta_j=\alpha_j^{-1}$. Extend a generic coefficient $M$ by
$j_{\eta!}M$ before restricting. Thus the calculation applies on the original open family.

*Twisted case.* Apply part (2) of [det-nearby-exceptional-tensor] to $p_1$, with
$\kappa_M=t_{p_1}(\xi\otimes1)$, insert the constant case, and use $\mu(\sigma\otimes1)=1$; this
gives the second equation.
