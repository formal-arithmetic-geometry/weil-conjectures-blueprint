+++
id = "prose-E-08"
kind = "hidden"
title = "Compatibility with specialization"
order = 956
+++
Let $c$ be a correspondence over the trait $S$ and $u$ a cohomological
correspondence on its generic fibre. Applying nearby cycles to $u$ and
composing with base change maps between nearby cycles and the
operations $f^*$, $Rf_*$, $Rf_!$ and $f^!$, we obtain a cohomological
correspondence $u_s$ on the special fibre. We will show in
Proposition [sk-prop-tf-trace-specialization] that the trace of $u_s$ is
the specialization of the trace of $u$. To prove it
we need these base change maps explicitly, together with a few
identities between them.

The formulas below involve many compositions of nearby cycle functors,
so we abbreviate
$\Psi_X=R\Psi_{X/S}$ for a separated $S$-scheme $X$ of finite type.
For a morphism $f:V\to W$ of separated $S$-schemes of finite type, put

$$
\begin{array}{rcl}
\alpha_f:f_s^*\Psi_W&\longrightarrow&\Psi_Vf_\eta^*,\\
\chi_f:\Psi_WRf_{\eta*}&\longrightarrow&Rf_{s*}\Psi_V,\\
\nu_f:Rf_{s!}\Psi_V&\longrightarrow&\Psi_WRf_{\eta!},\\
\beta_f:\Psi_Vf_\eta^!&\longrightarrow&f_s^!\Psi_W.
\end{array}
$$

The map $\alpha_f$ is the base change map for pullback of $\bar i^*R\bar j_*$, and
$\chi_f$ is its adjoint mate for $f_s^*\dashv Rf_{s*}$ and
$f_\eta^*\dashv Rf_{\eta*}$.

To define $\nu_f$, we choose a
relative Nagata compactification $f=ph$, with
$h:V\hookrightarrow\overline V$ open and $p$ proper.
We define $\nu_h:h_{s!}\Psi_VM\to \Psi_{\overline V}h_{\eta!}M$ using the
adjunction for the open immersion, by requiring that its adjoint be

$$
\Psi_VM=\Psi_Vh_\eta^*h_{\eta!}M
\xrightarrow{\alpha_h^{-1}}h_s^*\Psi_{\overline V}h_{\eta!}M.
$$

Since $p$ is proper, $\chi_p$ is invertible, and we put
$\nu_f=\chi_p^{-1}\,Rp_{s*}(\nu_h)$, using
$Rf_{s!}=Rp_{s*}h_{s!}$ and $Rf_{\eta!}=Rp_{\eta*}h_{\eta!}$.
If $q$ is a common proper refinement of two
compactifications, proper base change identifies $Rq_*h'_!$ with
$h_!$ on both fibres. After taking adjoints for the open immersions,
compatibility with this identification reduces to the composition rule
for $\alpha$ and the triangle identity of the ordinary adjunction.
Hence $\nu_f$ does not depend on the compactification, and the same
argument with common refinements shows that $\nu$ is compatible with
composition.

We can also describe $\nu_f$ on the total families. Write $i_V$ and
$j_V$ for the inclusions $\bar i$ and $\bar j$ of the special and
geometric generic fibres of $V$, so that $\Psi_V=i_V^*Rj_{V*}$. By proper
base change, $i_W^*Rf_!\simeq Rf_{s!}i_V^*$ and
$j_W^*Rf_!\simeq Rf_{\eta!}j_V^*$. Hence the restriction by $i_W^*$ of
the map $Rf_!Rj_{V*}\to Rj_{W*}Rf_{\eta!}$ whose $j_W^*$-adjoint is

$$
j_W^*Rf_!Rj_{V*}\simeq Rf_{\eta!}j_V^*Rj_{V*}
\xrightarrow{Rf_{\eta!}\varepsilon_{j_V}}Rf_{\eta!}
$$

is a map $Rf_{s!}\Psi_V\to \Psi_WRf_{\eta!}$, and we claim that it is
$\nu_f$. Both constructions are compatible with composition, so it
suffices to check this for $p$ and for $h$. For proper $p$ the
restricted map is $\chi_p^{-1}$, by proper base change for $i_W^*$.
For the open immersion $h$ we have $h_\eta^*h_{\eta!}=1$, and the
$h_s^*$-adjoint of the restricted map is $\alpha_h^{-1}$, as in the
definition of $\nu_h$.

The map $\beta_f(M)$ is the adjoint, for $Rf_{s!}\dashv f_s^!$, of

$$
Rf_{s!}\Psi_Vf_\eta^!M\xrightarrow{\nu_f}
\Psi_WRf_{\eta!}f_\eta^!M
\xrightarrow{\Psi_W\varepsilon_{f_\eta}}\Psi_WM.
\tag{E.6}
$$

For proper $f$, the maps $\chi_f$ and $\nu_f$ are inverse isomorphisms
after the identification $Rf_*=Rf_!$.

The lax monoidal map
$\mu_Y:\Psi_YM\otimes^{\mathbf L} \Psi_YN\to \Psi_Y(M\otimes^{\mathbf L} N)$ of $R\bar j_*$ is adjoint to the
tensor product of the two counits $j^*Rj_*\to1$. It is associative,
symmetric and unital, with unit $\sigma_Y:A_{Y_s}\to \Psi_YA_{Y_\eta}$,
and $\alpha_f$ is monoidal. For $f:V\to W$ and $g:W\to Z$, we have

$$
\alpha_{gf}=\alpha_f(g_\eta^*)f_s^*\alpha_g,
\qquad \sigma_V=\alpha_f(A)f_s^*\sigma_W,
\qquad\mu(\sigma\otimes1)=1.
\tag{E.7}
$$

For the structure morphism $a_Y:Y\to S$, set
$\theta_Y=\beta_{a_Y}(A):\Psi_Y\omega_{Y_\eta}\to\omega_{Y_s}$,
using $\Psi_SA=A$.

Finally, let $p_1,p_2$ be the projections of $X\times_SX$. On either
fibre, let $\xi:p_2^*\omega_X\to p_1^!A_X$ be the isomorphism of
Lemma [sk-thm-sf-kunneth-verdier] for $K=A_X$, and for a complex $M$ put
$\kappa_M=t_{p_1}(\xi\otimes1):p_2^*\omega_X\otimes^{\mathbf L} p_1^*M\to p_1^!M$, where
$t_{p_1}:p_1^!A_X\otimes^{\mathbf L} p_1^*M\to p_1^!M$ is the projection-formula mate of
the exceptional counit.

In the proof of Proposition [sk-prop-tf-trace-specialization] we move the
base change maps past the projection formula, composition, external
duality and the cartesian square defining the fixed point scheme. The following lemma collects the
identities we need.
