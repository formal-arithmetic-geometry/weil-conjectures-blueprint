+++
id = "prose-E-15"
kind = "hidden"
title = "Base change for nearby cycles (1)"
order = 1663
+++
Let $c$ be a correspondence over the trait $S$ and $u$ a cohomological
correspondence on its generic fibre. Nearby cycles turn $u$ into a map
between $\Psi$ of $c_2^*K$ and $\Psi$ of $c_1^!K$. To obtain a
cohomological correspondence $u_s$ on the special fibre, we must move
$\Psi$ past $c_2^*$ and $c_1^!$. This needs base change maps between
nearby cycles and the operations $f^*$, $Rf_*$, $Rf_!$ and $f^!$. We
make these maps explicit here. We also prove the identities between them
that Proposition [proposition-specialization-trace-class] uses to
show that the trace of $u_s$ is the specialization of the trace of $u$.

We write
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
The map $\nu_f$ does not depend on the compactification. Indeed, if $q$ is a common
proper refinement of two
compactifications, proper base change identifies $Rq_*h'_!$ with
$h_!$ on both fibres. After taking adjoints for the open immersions,
compatibility with this identification reduces to the composition rule
for $\alpha$ and the triangle identity of the ordinary adjunction.
Common refinements also show that $\nu$ is compatible with
composition.

We can also describe $\nu_f$ on the total families. Write $i_V$ and
$j_V$ for the inclusions $\bar i$ and $\bar j$ of the special and
geometric generic fibres of $V$, so that $\Psi_V=i_V^*Rj_{V*}$. By proper
base change, $i_W^*Rf_!\simeq Rf_{s!}i_V^*$ and
$j_W^*Rf_!\simeq Rf_{\eta!}j_V^*$. Consider the map
$Rf_!Rj_{V*}\to Rj_{W*}Rf_{\eta!}$ whose $j_W^*$-adjoint is

$$
j_W^*Rf_!Rj_{V*}\simeq Rf_{\eta!}j_V^*Rj_{V*}
\xrightarrow{Rf_{\eta!}\varepsilon_{j_V}}Rf_{\eta!}
$$

Its restriction by $i_W^*$ is a map $Rf_{s!}\Psi_V\to \Psi_WRf_{\eta!}$,
and we claim that this map is $\nu_f$. As both constructions are
compatible with composition, it suffices to check this for $p$ and for $h$. For proper $p$ the
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
and $\alpha_f$ is monoidal. For $f:V\to W$ and $g:W\to Y$, we have

$$
\alpha_{gf}=\alpha_f(g_\eta^*)f_s^*\alpha_g,
\qquad \sigma_V=\alpha_f(A)f_s^*\sigma_W,
\qquad\mu(\sigma\otimes1)=1.
\tag{E.7}
$$

For the structure morphism $a_Y:Y\to S$, set
$\theta_Y=\beta_{a_Y}(A):\Psi_Y\omega_{Y_\eta}\to\omega_{Y_s}$,
using $\Psi_SA=A$.

The proof of Proposition [proposition-specialization-trace-class] moves the
base change maps past the projection formula, composition, external
duality and the cartesian square defining the fixed point scheme.
The following four lemmas give the identities it needs. Each is proved by
taking adjoints until both sides become the same composite of base
change maps and counits, and then using the composition laws for the
base change maps and for the counits. For a morphism $f$ on either
fibre, write $t_f:f^!M\otimes^{\mathbf L} f^*N\to f^!(M\otimes^{\mathbf L} N)$
for the projection-formula mate of the exceptional counit.
