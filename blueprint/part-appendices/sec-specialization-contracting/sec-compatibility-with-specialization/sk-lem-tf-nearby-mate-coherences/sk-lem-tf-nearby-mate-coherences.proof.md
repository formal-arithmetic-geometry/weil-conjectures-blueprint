+++
kind = "proof"
of = "sk-lem-tf-nearby-mate-coherences"
+++
We prove each identity by taking adjoints until both sides become the
same composite of base change maps and counits, and then using the composition
laws for the base change maps and for the counits. Only
(E.10) needs more than this. Its constant case
(E.12) uses proper base change, and hence we
first prove it for a proper family and then extend it by compactification.

For (E.8) we use that $\nu_f$ is compatible
with the projection formula: for $L$ on $V_\eta$ and $N$ on $W_\eta$,
the composite

$$
Rf_{s!}(\Psi_VL\otimes^{\mathbf L} f_s^*\Psi_WN)\xrightarrow{\mu_V(1\otimes\alpha_f)}
Rf_{s!}\Psi_V(L\otimes^{\mathbf L} f_\eta^*N)\xrightarrow{\nu_f}
\Psi_WRf_{\eta!}(L\otimes^{\mathbf L} f_\eta^*N)\simeq \Psi_W(Rf_{\eta!}L\otimes^{\mathbf L} N)
$$

equals the projection formula on the special fibre followed by
$\mu_W(\nu_f\otimes1)$. To check this, we use the description of
$\nu_f$ on the total families and compare $j_W^*$-adjoints. On both
sides the adjoint is the counit $j_V^*Rj_{V*}\to1$ tensored with the
identity, followed by the projection formula on the generic fibre.

Now we take $Rf_{s!}$-adjoints in
(E.8). After applying the projection
formula, the left side becomes the following composite by the
compatibility just proved, and the right side becomes it by naturality
of $\mu_W$:

$$
\begin{split}
Rf_{s!}\Psi_Vf_\eta^!M\otimes^{\mathbf L} \Psi_WN
&\xrightarrow{\nu_f\otimes1}
\Psi_W(Rf_{\eta!}f_\eta^!M)\otimes^{\mathbf L} \Psi_WN\\
&\xrightarrow{\mu_W}\Psi_W(Rf_{\eta!}f_\eta^!M\otimes^{\mathbf L} N)
\xrightarrow{\Psi_W(\varepsilon_{f_\eta}\otimes1)}\Psi_W(M\otimes^{\mathbf L} N).
\end{split}
$$

The first identity in (E.9) follows by taking
adjoints for the adjunctions $Rh_{s!}\dashv h_s^!$ ($h=f,g,gf$) and using the compatibility of $\nu$ with
composition together with the composition of counits
$\varepsilon_{gf}=\varepsilon_g\,Rg_!\varepsilon_f$. The second is the
case $g=a_W$, $M=A$ of the first, since $a_V=a_Wf$.

For (E.10), recall that
$\kappa_M=t_{p_1}(\xi\otimes1)$, where $\xi:p_2^*\omega_X\to p_1^!A_X$
is the external duality map for the constant complex. We first show that

$$
\beta_{p_1}\Psi(\xi)\alpha_{p_2}
=p_{1s}^!\sigma_X\,\xi_s\,p_{2s}^*\theta_X.
\tag{E.12}
$$

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
counit $a_\eta^*Ra_{\eta*}L\to L$. We substitute this identity into the
$Rp_{1s!}$-adjoint of the left side of
(E.12). By naturality of $\alpha_a$ with
respect to $\varepsilon_{a_\eta}$ and since $\alpha_a(A)=\sigma_X$, this
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
(E.12) for proper $X$.

If $X$ is not proper over $S$, we choose an open immersion
$j:X\hookrightarrow\overline X$ into a proper $S$-scheme and restrict
both factors of the product from $\overline X$ to $X$. Both sides of
(E.12) are compatible with this restriction.
Indeed, the maps $\xi$ are compatible with restriction
by the composition rule for exceptional inverse images, and for $j$ we
have $j^!=j^*$, the map $\alpha_j$ is invertible by
smooth base change, and $\beta_j=\alpha_j^{-1}$. Hence
(E.12) on $\overline X$ implies it on $X$.
Finally, we
apply (E.8) to $p_1$ and use
$\mu(\sigma\otimes1)=1$ to deduce
(E.10).

For (E.11), note that the inverse of the base
change map, $Ri_*d^!\to c^!R\Delta_*$, is adjoint to the explicit map

$$
Rc_!Ri_*d^!=R\Delta_*Rd_!d^!
\xrightarrow{R\Delta_*\varepsilon_d}R\Delta_*.
$$

This identification uses that $i$ and $\Delta$ are proper.
We substitute it in both sides, take $Rc_{s!}$-adjoints, and
replace the comparison maps $\chi_i,\chi_\Delta$ for proper maps by the
inverses of $\nu_i,\nu_\Delta$. Both resulting maps are then the
base change map for the composite $ci=\Delta d$, followed by
$\Psi_X\varepsilon_d$. The equality follows from the composition rules for
the base change maps and for the counits.
