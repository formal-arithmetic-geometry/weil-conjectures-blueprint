+++
id = "sk-lem-tf-nearby-mate-coherences"
kind = "lemma"
title = "Coherences of the exchange maps"
order = 2651
uses = ["sk-thm-nagata-compactification"]
tags = ["sketch"]
+++
Let $S$ be an excellent strictly henselian trait with separably closed residue field $k$, generic
point $\eta$ and a chosen geometric generic point $\bar\eta$, and let $A$ be a finite commutative
$\ell$-primary ring with $\ell$ invertible on $S$. For a separated finite-type $S$-scheme $X$
abbreviate $S_X=R\Psi_{X/S}$, the geometric nearby cycles $\bar i^*R\bar j_*$. For a morphism
$f:V\to W$ of separated finite-type $S$-schemes, put

$$
\begin{array}{rcl}
\alpha_f:f_s^*S_W&\longrightarrow&S_Vf_\eta^*,\\
\chi_f:S_WRf_{\eta*}&\longrightarrow&Rf_{s*}S_V,\\
\nu_f:Rf_{s!}S_V&\longrightarrow&S_WRf_{\eta!},\\
\beta_f:S_Vf_\eta^!&\longrightarrow&f_s^!S_W.
\end{array}
$$

The maps $\alpha_f$ and $\beta_f$ are natural transformations of functors
$D^b_c(W_{\eta,\mathrm{\acute et}},A)\to D^b_c(V_{s,\mathrm{\acute et}},A)$, and $\chi_f$ and
$\nu_f$ of functors $D^b_c(V_{\eta,\mathrm{\acute et}},A)\to D^b_c(W_{s,\mathrm{\acute et}},A)$.
The map $\alpha_f$ is the pullback exchange for $\bar i^*R\bar j_*$, and $\chi_f$ is its adjoint
mate for $f_s^*\dashv Rf_{s*}$ and $f_\eta^*\dashv Rf_{\eta*}$. To define $\nu_f$, choose a
relative Nagata compactification $f=ph$ ([sk-thm-nagata-compactification]), with
$h:V\hookrightarrow\overline V$ open and $p$ proper; $\nu_h:h_{s!}S_VM\to S_{\overline V}h_{\eta!}M$
is the map whose adjoint for the open adjunction is
$S_VM=S_Vh_\eta^*h_{\eta!}M\xrightarrow{\alpha_h^{-1}}h_s^*S_{\overline V}h_{\eta!}M$, and
$\nu_f=\chi_p^{-1}\,Rp_{s*}(\nu_h)$ under the composition identifications; it is independent of
the compactification and compatible with composition. In terms of the total families, $\nu_f$ is
the restriction to the special fibre of the map $Rf_!Rj_{V*}\to Rj_{W*}Rf_{\eta!}$ whose
$j_W^*$-adjoint is
$j_W^*Rf_!Rj_{V*}\simeq Rf_{\eta!}j_V^*Rj_{V*}\xrightarrow{Rf_{\eta!}\varepsilon_{j_V}}Rf_{\eta!}$.
The map $\beta_f(M)$ is the exceptional adjoint of

$$
Rf_{s!}S_Vf_\eta^!M\xrightarrow{\nu_f}S_WRf_{\eta!}f_\eta^!M
\xrightarrow{S_W\varepsilon_{f_\eta}}S_WM.
\tag{1}
$$

For proper $f$, $\chi_f$ and $\nu_f$ are inverse isomorphisms after the identification
$Rf_*=Rf_!$. The lax tensor map $\mu_Y:S_YM\dt S_YN\to S_Y(M\dt N)$ of $R\bar j_*$ is adjoint to
the tensor product of the two $j^*Rj_*\to1$ counits. It is associative, symmetric and unital, with
unit $\sigma_Y:A_{Y_s}\to S_YA_{Y_\eta}$; $\alpha_f$ is monoidal. For $f:V\to W$, $g:W\to Z$ this
gives

$$
\alpha_{gf}=\alpha_f(g_\eta^*)\,f_s^*\alpha_g,
\qquad \sigma_V=\alpha_f(A)\,f_s^*\sigma_W,
\qquad\mu(\sigma\otimes1)=1.
\tag{2}
$$

For a structure map $a_Y$, set $\theta_Y=\beta_{a_Y}(A):S_Y\omega_{Y_\eta}\to\omega_{Y_s}$, using
$S_SA=A$.

Write $t_f:f^!M\dt f^*N\to f^!(M\dt N)$ for the projection-formula mate of the exceptional counit.
Then

$$
\beta_f\,S_V(t_{f_\eta})\,\mu_V(1\otimes\alpha_f)=f_s^!\mu_W\ t_{f_s}(\beta_f\otimes1).
\tag{3}
$$

The source is $S_Vf_\eta^!M\dt f_s^*S_WN$. Moreover

$$
\beta_{gf}=f_s^!\beta_g\ \beta_f(g_\eta^!),
\qquad\theta_V=f_s^!\theta_W\ \beta_f(\omega_{W_\eta}).
\tag{4}
$$

On $X\times X$, let $\kappa_M:p_2^*\omega_X\dt p_1^*M\to p_1^!M$ be the normalized
external-duality map. Then

$$
\beta_{p_1}\,S(\kappa_M)\,\mu\,(\alpha_{p_2}\otimes\alpha_{p_1})
=\kappa_{S_XM}(p_{2s}^*\theta_X\otimes1).
\tag{5}
$$

Finally, let $c:C\to X\times_SX$ be a correspondence with fixed scheme $F$, and consider the fixed
square with $r:F\hookrightarrow C$, $d:F\to X$, and closed diagonal
$\Delta:X\hookrightarrow X\times X$; let $B:c^!R\Delta_*\xrightarrow{\sim}Rr_*d^!$ be exceptional
proper base change. Then

$$
Rr_{s*}\beta_d\ \chi_r\ S_C(B_\eta)=B_s\ c_s^!(\chi_\Delta)\ \beta_c(R\Delta_{\eta*}).
\tag{6}
$$
