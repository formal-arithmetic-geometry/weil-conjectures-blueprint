+++
kind = "proof"
of = "lemma-base-change-maps-external-duality"
order = 1670
+++
Since
$\kappa_M=t_{p_1}(\xi\otimes1)$, the main point is
the case of the constant complex,

$$
\beta_{p_1}\Psi(\xi)\alpha_{p_2}
=p_{1s}^!\sigma_X\,\xi_s\,p_{2s}^*\theta_X,
\tag{C}
$$

and the general case follows from (C) by
Lemma [lemma-compatibilities-base-change-maps]. Since the proof uses
proper base change, we prove (C) for a proper
family and then extend it by compactification.

Suppose first that $a=a_X:X\to S$ is proper. On the fibre over $\eta$,
let

$$
Q_\eta(L):a_\eta^*Ra_{\eta*}L\xrightarrow{\sim}Rp_{1\eta*}p_{2\eta}^*L
$$

be the proper base change isomorphism, and define $Q_s$ in the same way.
On each fibre, the $Rp_{1!}$-adjoint of $\xi$ is $Q(\omega_X)^{-1}$
followed by $a^*\varepsilon_a$. We compare these adjoints using the
identity

$$
\nu_{p_1}Rp_{1s*}(\alpha_{p_2})Q_s(\Psi_XL)
=\Psi_X(Q_\eta(L))\alpha_a(Ra_{\eta*}L)\,a_s^*\nu_a(L).
$$

To prove it, we take adjoints for $p_{1s}^*\dashv Rp_{1s*}$. By the
composition rule for $\alpha$ and $ap_1=ap_2$, both adjoints are the composite of $a_s^*\nu_a$, the base change map
$\alpha_{ap_1}=\alpha_{ap_2}$, and the pullback by $p_{2\eta}$ of the
counit $a_\eta^*Ra_{\eta*}L\to L$. Substituting this identity into the
$Rp_{1s!}$-adjoint of the left side of
(C), and using naturality of $\alpha_a$ with
respect to $\varepsilon_{a_\eta}$ and $\alpha_a(A)=\sigma_X$, we find that this
adjoint is the composite

$$
a_s^*Ra_{s!}\Psi_X\omega_{X_\eta}
\xrightarrow{a_s^*\nu_a}
a_s^*Ra_{\eta!}\omega_{X_\eta}
\xrightarrow{a_s^*\varepsilon_{a_\eta}}A_{X_s}
\xrightarrow{\sigma_X}\Psi_XA_{X_\eta}.
$$

By (E.6) for $a$, this composite equals
$\sigma_X a_s^*(\varepsilon_{a_s}Ra_{s!}\theta_X)$, which is the
$Rp_{1s!}$-adjoint of the right side. This proves
(C) for proper $X$.

If $X$ is not proper over $S$, we choose an open immersion
$j:X\hookrightarrow\overline X$ into a proper $S$-scheme and restrict
both factors of the product from $\overline X$ to $X$. Both sides of
(C) are compatible with this restriction.
For the maps $\xi$ this follows from the composition rule for
exceptional inverse images. For the base change maps it holds because
$j^!=j^*$, the map $\alpha_j$ is invertible by smooth base change, and
$\beta_j=\alpha_j^{-1}$. So
(C) on $\overline X$ implies it on $X$.
Applying Lemma [lemma-compatibilities-base-change-maps] to $p_1$ and using
$\mu(\sigma\otimes1)=1$, we deduce
(E.10).
